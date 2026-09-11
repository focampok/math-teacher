# -*- coding: utf-8 -*-
"""Ensambla los 3 HTML de Matemática IV en un único index.html (Netlify)."""
from pathlib import Path
import re

DIR = Path(__file__).resolve().parent
OUT = DIR / "index.html"

PRACTICA = DIR / "IV Matemática 2026 - Práctica interactiva.html"
FORMULAS = DIR / "IV Matemática 2026 - Tablas y fórmulas.html"
EXPRES = DIR / "IV Matemática 2026 - Hoja exprés.html"


def extraer(html: str, start: str, end: str) -> str:
    i = html.find(start)
    if i < 0:
        raise SystemExit(f"No se encontró {start!r}")
    j = html.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"No se encontró {end!r} tras {start!r}")
    return html[i + len(start) : j]


def extraer_incluido(html: str, start: str, end: str) -> str:
    i = html.find(start)
    if i < 0:
        raise SystemExit(f"No se encontró {start!r}")
    j = html.find(end, i)
    if j < 0:
        raise SystemExit(f"No se encontró {end!r}")
    return html[i : j + len(end)]


def scope_css(css: str, scope: str) -> str:
    """Prefija selectores con el contenedor. Respeta @media/@keyframes/@page."""
    out = []
    i = 0
    n = len(css)
    while i < n:
        brace = css.find("{", i)
        if brace < 0:
            out.append(css[i:])
            break
        prelude = css[i:brace].strip()
        depth = 0
        j = brace
        while j < n:
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        body = css[brace + 1 : j]
        low = prelude.lower()
        if low.startswith("@keyframes") or low.startswith("@-") or low.startswith("@page") or low.startswith("@font-face"):
            out.append(prelude + "{" + body + "}")
        elif low.startswith("@media") or low.startswith("@supports"):
            out.append(prelude + "{" + scope_css(body, scope) + "}")
        else:
            sels = [s.strip() for s in prelude.split(",") if s.strip()]
            nuevos = []
            for sel in sels:
                if sel in (":root", "html", "body", "html body"):
                    nuevos.append(scope)
                elif sel.startswith(":root") or sel.startswith("html") or sel.startswith("body"):
                    rest = re.sub(r"^(:root|html|body)\s*", "", sel).strip()
                    nuevos.append((scope + " " + rest).strip() if rest else scope)
                else:
                    nuevos.append(scope + " " + sel)
            out.append(",".join(nuevos) + "{" + body + "}")
        i = j + 1
    return "\n".join(out)


KIT_CSS = r"""
/* ========== Kit unificado: cromo de la app ========== */
html{height:100%;}
body{
  padding-bottom:calc(68px + env(safe-area-inset-bottom,0px));
}
body.sheet-mode{
  background:#dfe6f2;
  color:#1c2333;
}
.kit-skip{position:fixed;left:-999px;top:8px;z-index:3000;background:var(--accent);color:var(--accent-ink);
  font-weight:800;padding:12px 18px;border-radius:12px;}
.kit-skip:focus{left:10px;}

.kit-bar{
  position:sticky;top:0;z-index:80;
  background:rgba(11,18,32,.92);backdrop-filter:blur(12px);
  border-bottom:1px solid var(--line);
  padding:8px 12px calc(8px + env(safe-area-inset-top,0px));
}
.kit-row{
  max-width:1100px;margin:0 auto;display:flex;align-items:center;gap:10px;flex-wrap:wrap;
}
.kit-brand{
  display:flex;align-items:center;gap:10px;background:none;border:none;color:var(--text);
  cursor:pointer;text-align:left;padding:4px 6px;border-radius:12px;
}
.kit-brand:hover{background:rgba(255,255,255,.06);}
.kit-logo{
  width:42px;height:42px;border-radius:13px;display:grid;place-items:center;flex:none;
  background:linear-gradient(135deg,var(--accent),#fb923c);box-shadow:0 4px 14px rgba(245,158,11,.35);color:#111;
}
.kit-brand h1{font-size:1.02rem;line-height:1.15;font-weight:800;margin:0;}
.kit-brand h1 small{display:block;font-weight:600;color:var(--muted);font-size:.7rem;letter-spacing:.3px;}
.kit-nav{
  display:none;margin-left:auto;gap:6px;flex-wrap:wrap;
}
.kit-nav button{
  border:1px solid var(--line);background:var(--panel2);color:var(--text);
  font:inherit;font-weight:800;font-size:.82rem;padding:8px 14px;border-radius:999px;
  min-height:42px;cursor:pointer;display:inline-flex;align-items:center;gap:7px;
}
.kit-nav button.on{background:var(--accent);color:var(--accent-ink);border-color:var(--accent);}
.kit-nav button:hover:not(.on){background:var(--panel3);}

.kit-tabs{
  position:fixed;left:0;right:0;bottom:0;z-index:90;
  display:grid;grid-template-columns:repeat(4,1fr);gap:2px;
  background:rgba(15,23,42,.96);backdrop-filter:blur(12px);
  border-top:1px solid var(--line);
  padding:6px 6px calc(6px + env(safe-area-inset-bottom,0px));
}
.kit-tabs button{
  border:none;background:transparent;color:var(--muted);font:inherit;font-weight:800;
  font-size:.68rem;padding:6px 4px 4px;border-radius:12px;cursor:pointer;
  display:flex;flex-direction:column;align-items:center;gap:2px;min-height:52px;
}
.kit-tabs button svg{width:22px;height:22px;}
.kit-tabs button.on{color:#fff;background:rgba(245,158,11,.16);}
.kit-tabs button.on svg{color:var(--accent);}

.app-view{display:none;}
.app-view.activa{display:block;animation:kitIn .28s var(--ease) both;}
@keyframes kitIn{from{opacity:0;}to{opacity:1;}}
@media (prefers-reduced-motion:reduce){
  .app-view.activa{animation:none;}
}

#view-practica header.prac-head{position:sticky;top:58px;z-index:40;}
#pracMain{padding-bottom:24px;}

/* Subnavegación de fichas: va DENTRO del kit-bar (un solo encabezado, ancho completo, centrada) */
.kit-sub{
  display:none;
  flex-direction:column;align-items:center;justify-content:center;
  gap:8px;padding:0 12px 10px;
}
body[data-vista="formulas"] #subFormulas,
body[data-vista="expres"] #subExpres{display:flex;}
.kit-sub .chip-nav{
  display:flex;gap:6px;flex-wrap:wrap;justify-content:center;
  width:100%;max-width:210mm;
}
.kit-sub .chip-nav a{
  flex:none;white-space:nowrap;text-decoration:none;font-size:.75rem;font-weight:800;
  padding:8px 12px;border-radius:999px;min-height:40px;
  display:inline-flex;align-items:center;color:#fff;border:2px solid transparent;
}
.kit-sub .chip-nav a.cn1{background:#1d4ed8;}
.kit-sub .chip-nav a.cn2{background:#15803d;}
.kit-sub .chip-nav a.cn3{background:#a16207;}
.kit-sub .chip-nav a.cn4{background:#c2410c;}
.kit-sub .chip-nav a.cn5{background:#6d28d9;}
.kit-sub .chip-nav a.cnx{background:#334155;}
.kit-sub .chip-nav a:hover{filter:brightness(1.12);}
.kit-sub .chip-nav a.on{border-color:#f59e0b;box-shadow:0 0 0 3px rgba(245,158,11,.35);}
.kit-sub .sheet-actions{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;}
.kit-sub button.ghost, .kit-sub .btn-print{
  border:none;cursor:pointer;font:inherit;font-weight:800;
  padding:10px 16px;border-radius:999px;min-height:44px;
}
.kit-sub button.ghost{
  background:#1e293b;color:#eef2ff;border:1px solid #475569;
}
.kit-sub .btn-print{background:#f59e0b;color:#111;}
.sheet-hint{
  max-width:210mm;margin:10px auto 0;padding:10px 14px;
  background:#fff7ed;border:1px solid #fdba74;border-radius:12px;
  font-size:.86rem;color:#9a3412;
}
body.sheet-mode .kit-row{max-width:210mm;}

/* Inicio del kit */
.hero{
  max-width:980px;margin:0 auto;padding:22px 14px 10px;
}
.hero-card{
  background:linear-gradient(135deg,rgba(99,102,241,.22),var(--panel));
  border:1px solid rgba(129,140,248,.45);border-radius:22px;padding:22px 20px 18px;
  box-shadow:0 10px 30px rgba(0,0,0,.28);position:relative;overflow:hidden;
}
.hero-card::after{
  content:"";position:absolute;right:-60px;top:-60px;width:200px;height:200px;pointer-events:none;
  background:radial-gradient(circle,rgba(245,158,11,.28),transparent 70%);
}
.hero-card .kicker{font-size:.75rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#c4b5fd;}
.hero-card h2{font-size:clamp(1.45rem,4vw,2rem);margin:6px 0 8px;line-height:1.15;}
.hero-card p{color:var(--muted);margin:0;max-width:36em;}
.hero-pills{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px;}
.hero-pills span{
  background:rgba(15,23,42,.55);border:1px solid var(--line);border-radius:999px;
  padding:4px 12px;font-size:.78rem;font-weight:700;
}
.hero-pills b{color:var(--accent);}

.kit-grid{
  max-width:980px;margin:0 auto;padding:8px 14px 20px;
  display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;
}
.kit-card{
  text-align:left;cursor:pointer;color:var(--text);font:inherit;
  background:linear-gradient(180deg,var(--panel),var(--panel2));
  border:1px solid var(--line);border-radius:20px;padding:18px 18px 16px;
  box-shadow:0 8px 24px rgba(0,0,0,.25);
  transition:transform .18s var(--ease),box-shadow .18s;
  display:flex;flex-direction:column;gap:8px;min-height:210px;
}
.kit-card:hover{transform:translateY(-3px);box-shadow:0 14px 30px rgba(0,0,0,.4);}
.kit-card:active{transform:scale(.99);}
.kit-card .ico{
  width:48px;height:48px;border-radius:14px;display:grid;place-items:center;color:#111;
}
.kit-card.c1 .ico{background:linear-gradient(135deg,#38bdf8,#6366f1);}
.kit-card.c2 .ico{background:linear-gradient(135deg,#34d399,#22c55e);}
.kit-card.c3 .ico{background:linear-gradient(135deg,#f59e0b,#fb923c);}
.kit-card h3{font-size:1.18rem;margin:4px 0 0;}
.kit-card p{font-size:.88rem;color:var(--muted);margin:0;line-height:1.45;flex:1;}
.kit-card .go{
  display:inline-flex;align-items:center;gap:6px;font-weight:800;font-size:.88rem;color:var(--accent);
}
.kit-mini{
  max-width:980px;margin:0 auto 28px;padding:0 14px;
}
.kit-mini h3{font-size:1rem;margin:0 0 10px;}
.bloques-row{display:flex;gap:8px;flex-wrap:wrap;}
.bloques-row a{
  text-decoration:none;color:#fff;font-weight:800;font-size:.8rem;
  padding:10px 12px;border-radius:12px;min-height:44px;display:inline-flex;align-items:center;
}
.bbk1{background:#1d4ed8;} .bbk2{background:#15803d;} .bbk3{background:#a16207;}
.bbk4{background:#c2410c;} .bbk5{background:#6d28d9;}

#view-formulas, #view-expres{min-height:60vh;padding-bottom:24px;}
#view-formulas *, #view-expres *{box-sizing:border-box;}
#f-b1,#f-b2,#f-b3,#f-b4,#f-b5,#f-expres{scroll-margin-top:128px;}
@media screen and (max-width:720px){
  #view-formulas .toc{grid-template-columns:1fr 1fr;}
}
@media screen and (max-width:420px){
  #view-formulas .toc{grid-template-columns:1fr;}
}
.toast{bottom:calc(78px + env(safe-area-inset-bottom,0px)) !important;}
button{touch-action:manipulation;}

/* Tablas que no quepan: scroll horizontal en móvil */
#view-formulas table, #view-expres table{
  max-width:100%;
}
#view-formulas .doc, #view-expres .doc{overflow-x:auto;}

/* Modo recitar: tapa las fórmulas; toca para ver */
#view-expres.recitando .eq,
#view-expres.recitando td .eq,
#view-expres.recitando .recite p{
  background:#1c2333;color:#1c2333;border-radius:6px;user-select:none;
}
#view-expres.recitando .eq:active,
#view-expres.recitando .recite p:active{
  background:#eef1f7;color:inherit;
}
.recite-banner{
  max-width:210mm;margin:8px auto 0;padding:8px 12px;border-radius:10px;
  background:#0f172a;color:#eef2ff;font-size:.84rem;font-weight:700;
}

.kit-foot{
  max-width:980px;margin:28px auto 12px;padding:16px 18px 8px;
  border-top:1px solid var(--line);
  color:var(--muted);font-size:.78rem;line-height:1.5;text-align:center;
}
.kit-foot p{margin:0 0 8px;}
.kit-foot a{color:var(--accent);font-weight:800;text-decoration:underline;text-underline-offset:2px;}
.kit-foot a:hover{filter:brightness(1.12);}
body.sheet-mode .kit-foot{
  max-width:210mm;color:#3d4a63;border-top-color:#c5cedc;
}
body.sheet-mode .kit-foot a{color:#c2410c;}

@media (min-width:840px){
  body{padding-bottom:12px;}
  .kit-nav{display:flex;}
  .kit-tabs{display:none;}
  #view-practica header.prac-head{top:60px;}
  .kit-sub{flex-direction:row;flex-wrap:wrap;padding:4px 12px 10px;}
  .toast{bottom:22px !important;}
}
@media (max-width:560px){
  .kit-brand h1{font-size:.92rem;}
  .kit-logo{width:36px;height:36px;border-radius:10px;}
  .hero-card{padding:18px 14px;}
  .kit-card{min-height:0;}
  #view-practica .prac-head .brand{display:none;}
  #view-practica .prac-head .stats{margin-left:0;}
}

@media print{
  .kit-bar, .kit-tabs, .kit-skip, .kit-foot, .kit-sub, #view-inicio, #view-practica,
  #dialog, #toast, .sheet-hint, .recite-banner{display:none !important;}
  body{padding:0 !important;background:#fff !important;}
  .app-view{display:none !important;animation:none !important;}
  body[data-vista="formulas"] #view-formulas,
  body[data-vista="expres"] #view-expres{display:block !important;}
  #view-formulas, #view-expres{padding:0 !important;}
}
"""

KIT_INICIO = r"""
<section id="view-inicio" class="app-view activa" aria-labelledby="heroTitle">
  <div class="hero">
    <div class="hero-card">
      <div class="kicker">Examen de admisión 2026</div>
      <h2 id="heroTitle">Tu kit de refuerzo de Matemática IV</h2>
      <p>Tres herramientas en un solo lugar: practica con puntos y rachas, consulta las fórmulas y recita la hoja exprés. Funciona en el celular, la tablet y la computadora — sin instalar nada.</p>
      <div class="hero-pills" aria-label="Tu progreso">
        <span>Puntos <b id="homePts">0</b></span>
        <span>Aciertos <b id="homeHit">0/0</b></span>
        <span>5 bloques · 100 pts</span>
      </div>
    </div>
  </div>
  <div class="kit-grid">
    <button type="button" class="kit-card c1" onclick="irA('practica')">
      <span class="ico" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4.5 13.5H11L9.5 22 19 9.5h-6.5z"/></svg></span>
      <h3>Practicar</h3>
      <p>8 retos por bloque o un simulacro de 20 preguntas (nota /100). Respuesta al instante, pistas y logros.</p>
      <span class="go">Empezar práctica →</span>
    </button>
    <button type="button" class="kit-card c2" onclick="irA('formulas')">
      <span class="ico" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></svg></span>
      <h3>Fórmulas</h3>
      <p>Tablas, dibujos y conversiones de los 5 bloques. Lo que el examen no te va a dar. También se puede imprimir.</p>
      <span class="go">Abrir ficha →</span>
    </button>
    <button type="button" class="kit-card c3" onclick="irA('expres')">
      <span class="ico" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg></span>
      <h3>Hoja exprés</h3>
      <p>Las 18 fórmulas en 2 páginas. Activa el modo recitar, tápate la respuesta y dilas en voz alta.</p>
      <span class="go">Recitar ahora →</span>
    </button>
  </div>
  <div class="kit-mini">
    <h3>Saltar a un bloque de fórmulas</h3>
    <div class="bloques-row">
      <a class="bbk1" href="#f-b1">1 Geometría</a>
      <a class="bbk2" href="#f-b2">2 Factorización</a>
      <a class="bbk3" href="#f-b3">3 Desigualdades</a>
      <a class="bbk4" href="#f-b4">4 Recta</a>
      <a class="bbk5" href="#f-b5">5 Funciones</a>
    </div>
  </div>
</section>
"""

SVG_HOME = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11.5 12 4l9 7.5"/><path d="M5 10.5V20h14v-9.5"/></svg>'
SVG_PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4.5 13.5H11L9.5 22 19 9.5h-6.5z"/></svg>'
SVG_BOOK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></svg>'
SVG_EDIT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>'


KIT_JS = r"""
/* ============================================================
   KIT UNIFICADO — vistas, hash, recitar
============================================================ */
(function(){
  const VISTAS=["inicio","practica","formulas","expres"];

  function enJuego(){
    return document.body.dataset.vista==="practica" && typeof view==="string" && view==="game";
  }

  window.actualizarInicio=function(){
    const pts=document.getElementById("homePts");
    const hit=document.getElementById("homeHit");
    if(pts) pts.textContent=state.pts;
    if(hit) hit.textContent=state.hit+"/"+state.tot;
  };

  function aplicarVista(nombre, ancla){
    if(!VISTAS.includes(nombre)) nombre="inicio";
    document.body.dataset.vista=nombre;
    document.body.classList.toggle("sheet-mode", nombre==="formulas"||nombre==="expres");
    document.querySelectorAll(".app-view").forEach(el=>{
      el.classList.toggle("activa", el.id==="view-"+nombre);
    });
    document.querySelectorAll("[data-vista]").forEach(el=>{
      const on=el.getAttribute("data-vista")===nombre;
      el.classList.toggle("on", on);
      if(el.tagName==="BUTTON") el.setAttribute("aria-current", on?"page":"false");
    });
    const hash=ancla ? "#"+ancla : "#"+nombre;
    if(location.hash!==hash){
      try{history.replaceState(null,"",hash);}catch(e){location.hash=hash;}
    }
    if(nombre==="practica"){ renderStats(); }
    if(nombre==="inicio") actualizarInicio();
    const tema=document.querySelector('meta[name="theme-color"]');
    if(tema) tema.setAttribute("content", (nombre==="formulas"||nombre==="expres")?"#dfe6f2":"#0b1220");
    if(!ancla) window.scrollTo({top:0,behavior:reduceMotion()?"auto":"smooth"});
    if(ancla){
      const t=document.getElementById(ancla);
      if(t) setTimeout(()=>t.scrollIntoView({behavior:reduceMotion()?"auto":"smooth",block:"start"}),40);
    }
  }

  window.irA=function(nombre, ancla){
    if(enJuego() && nombre!=="practica"){
      openDialog("¿Salir de la práctica?",
        "Si cambias de sección ahora, se termina esta práctica. Conservarás los puntos ya ganados.",
        "Sí, salir",
        function(){ goHome(); aplicarVista(nombre, ancla); },
        "Seguir practicando");
      return;
    }
    aplicarVista(nombre, ancla);
  };

  function leerHash(){
    const h=(location.hash||"#inicio").replace(/^#/,"");
    if(h.startsWith("f-")) return {vista:"formulas", ancla:h};
    if(VISTAS.includes(h)) return {vista:h};
    if(h==="home"||h==="") return {vista:"inicio"};
    return {vista:"inicio"};
  }

  window.addEventListener("hashchange", function(){
    const {vista, ancla}=leerHash();
    if(enJuego() && vista!=="practica"){
      try{history.replaceState(null,"","#practica");}catch(e){}
      irA(vista, ancla);
      return;
    }
    aplicarVista(vista, ancla);
  });

  const btnF=document.getElementById("btnIntroFormulas");
  if(btnF) btnF.addEventListener("click", function(){
    const id=current.block ? "f-"+current.block.id : "f-b1";
    irA("formulas", id);
  });
  const btnFF=document.getElementById("btnFullFormulas");
  if(btnFF) btnFF.addEventListener("click", function(){ irA("formulas"); });
  const btnRF=document.getElementById("btnResFormulas");
  if(btnRF) btnRF.addEventListener("click", function(){
    const id=current.block ? "f-"+current.block.id : "f-b1";
    irA("formulas", current.mode==="full"?undefined:id);
  });

  const btnRec=document.getElementById("btnRecitar");
  const viewEx=document.getElementById("view-expres");
  const banner=document.getElementById("reciteBanner");
  if(btnRec && viewEx){
    btnRec.addEventListener("click", function(){
      const on=viewEx.classList.toggle("recitando");
      btnRec.textContent=on?"Dejar de recitar":"Modo recitar";
      btnRec.setAttribute("aria-pressed", on?"true":"false");
      if(banner) banner.classList.toggle("hidden", !on);
    });
  }

  (function observarBloques(){
    const chips=document.querySelectorAll("#subFormulas .chip-nav a");
    if(!chips.length || !("IntersectionObserver" in window)) return;
    const map={};
    chips.forEach(function(a){
      const id=(a.getAttribute("href")||"").replace("#","");
      map[id]=a;
    });
    const io=new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(!en.isIntersecting) return;
        chips.forEach(function(c){ c.classList.remove("on"); });
        if(map[en.target.id]) map[en.target.id].classList.add("on");
      });
    },{rootMargin:"-25% 0px -55% 0px", threshold:0});
    ["f-b1","f-b2","f-b3","f-b4","f-b5","f-expres"].forEach(function(id){
      const el=document.getElementById(id);
      if(el) io.observe(el);
    });
  })();

  const _rh=renderHome;
  renderHome=function(){ _rh(); actualizarInicio(); };

  const arr=leerHash();
  aplicarVista(arr.vista, arr.ancla);
  actualizarInicio();
})();
"""


def parchear_practica_css(css: str) -> str:
    css = css.replace("header{position:sticky", "header.prac-head{position:sticky", 1)
    css = css.replace("main{max-width:980px", "#pracMain{max-width:980px", 1)
    css = css.replace("a.skip{", "a.skip-prac{", 1)
    css = css.replace("a.skip:focus", "a.skip-prac:focus", 1)
    # Las tarjetas .block / .go de la práctica no deben pintar las fichas
    for viejo, nuevo in (
        (".block:hover .go{", "#blocksGrid .block:hover .go{"),
        (".block:hover{", "#blocksGrid .block:hover{"),
        (".block:active{", "#blocksGrid .block:active{"),
        (".block .top{", "#blocksGrid .block .top{"),
        (".block .chip{", "#blocksGrid .block .chip{"),
        (".block h3{", "#blocksGrid .block h3{"),
        (".block .desc{", "#blocksGrid .block .desc{"),
        (".block .pts{", "#blocksGrid .block .pts{"),
        (".block{", "#blocksGrid .block{"),
        (".go{", "#blocksGrid .go{"),
    ):
        css = css.replace(viejo, nuevo)
    return css


def parchear_practica_html(header: str, main: str) -> tuple[str, str]:
    header = header.replace("<header>", '<header class="prac-head">', 1)
    header = header.replace(
        "<h1>Matemática IV <small>Práctica interactiva · Admisión</small></h1>",
        "<h1>Práctica <small>8 retos o simulacro /100</small></h1>",
        1,
    )
    main = main.replace('<main id="main">', '<main id="pracMain">', 1)
    main = main.replace(
        '<button class="btn secondary" id="btnIntroBack">Volver al inicio</button>',
        '<button class="btn ghost" id="btnIntroFormulas" type="button">Ver fórmulas</button>\n'
        '        <button class="btn secondary" id="btnIntroBack">Volver a bloques</button>',
        1,
    )
    main = main.replace(
        '<button class="btn secondary" id="btnFullBack">Volver al inicio</button>',
        '<button class="btn ghost" id="btnFullFormulas" type="button">Repasar fórmulas</button>\n'
        '        <button class="btn secondary" id="btnFullBack">Volver a bloques</button>',
        1,
    )
    main = main.replace(
        '<button class="btn secondary" id="btnHomeResult">Volver a bloques</button>',
        '<button class="btn ghost" id="btnResFormulas" type="button">Repasar fórmulas</button>\n'
        '        <button class="btn secondary" id="btnHomeResult">Volver a bloques</button>',
        1,
    )
    return header, main


def parchear_formulas_html(html: str) -> str:
    html = html.replace('id="contenido"', 'id="f-contenido"')
    html = html.replace('id="b1"', 'id="f-b1"')
    html = html.replace('id="b2"', 'id="f-b2"')
    html = html.replace('id="b3"', 'id="f-b3"')
    html = html.replace('id="b4"', 'id="f-b4"')
    html = html.replace('id="b5"', 'id="f-b5"')
    html = html.replace('id="expres"', 'id="f-expres"')
    html = html.replace('href="#b1"', 'href="#f-b1"')
    html = html.replace('href="#b2"', 'href="#f-b2"')
    html = html.replace('href="#b3"', 'href="#f-b3"')
    html = html.replace('href="#b4"', 'href="#f-b4"')
    html = html.replace('href="#b5"', 'href="#f-b5"')
    html = html.replace('href="#expres"', 'href="#f-expres"')
    return html


def main() -> None:
    prac = PRACTICA.read_text(encoding="utf-8")
    form = FORMULAS.read_text(encoding="utf-8")
    expr = EXPRES.read_text(encoding="utf-8")

    prac_css = parchear_practica_css(extraer(prac, "<style>", "</style>"))
    form_css = scope_css(extraer(form, "<style>", "</style>"), "#view-formulas")
    expr_css = scope_css(extraer(expr, "<style>", "</style>"), "#view-expres")

    prac_header = extraer_incluido(prac, "<header>", "</header>")
    prac_main = extraer_incluido(prac, '<main id="main">', "</main>")
    prac_header, prac_main = parchear_practica_html(prac_header, prac_main)
    prac_dialog = extraer_incluido(prac, '<div class="dialog hidden"', "</div>\n</div>")
    # el diálogo tiene anidación; extraer de forma más segura
    d0 = prac.find('<div class="dialog hidden"')
    # toma hasta el toast exclusive
    t0 = prac.find('<div class="toast"')
    prac_dialog = prac[d0:t0].rstrip()
    prac_toast = extraer_incluido(prac, '<div class="toast"', "</div>")
    prac_js = extraer(prac, "<script>", "</script>")

    form_main = parchear_formulas_html(extraer_incluido(form, '<main id="contenido"', "</main>"))
    expr_main = extraer_incluido(expr, '<main id="ficha"', "</main>")

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#0b1220">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="description" content="Kit de refuerzo de Matemática IV: práctica interactiva, ficha de fórmulas y hoja exprés. Para celular, tablet y computadora.">
<title>Matemática IV — Kit de refuerzo 2026</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect rx='8' width='32' height='32' fill='%23f59e0b'/%3E%3Cpath d='M8 22V10M8 22h16' stroke='%23111' stroke-width='2.4' fill='none' stroke-linecap='round'/%3E%3Cpath d='M8 22l4-6 3 3 5-7 4 4' stroke='%23111' stroke-width='2.2' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800&display=swap" rel="stylesheet">
<style>
{prac_css}
{KIT_CSS}
{form_css}
{expr_css}
</style>
</head>
<body data-vista="inicio">
<a class="kit-skip" href="#kitMain">Saltar al contenido</a>

<header class="kit-bar">
  <div class="kit-row">
    <button class="kit-brand" type="button" onclick="irA('inicio')" aria-label="Ir al inicio del kit">
      <span class="kit-logo" aria-hidden="true">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V5M4 19h16M4 19l4-6 3 3 5-7 4 4"/></svg>
      </span>
      <span><h1>Matemática IV <small>Kit de refuerzo · Admisión 2026</small></h1></span>
    </button>
    <nav class="kit-nav" aria-label="Secciones del kit">
      <button type="button" data-vista="inicio" onclick="irA('inicio')">{SVG_HOME} Inicio</button>
      <button type="button" data-vista="practica" onclick="irA('practica')">{SVG_PLAY} Practicar</button>
      <button type="button" data-vista="formulas" onclick="irA('formulas')">{SVG_BOOK} Fórmulas</button>
      <button type="button" data-vista="expres" onclick="irA('expres')">{SVG_EDIT} Exprés</button>
    </nav>
  </div>
  <div class="kit-sub" id="subFormulas">
    <nav class="chip-nav" aria-label="Ir a un bloque">
      <a class="cn1" href="#f-b1">1 Geometría</a>
      <a class="cn2" href="#f-b2">2 Factorización</a>
      <a class="cn3" href="#f-b3">3 Desigualdades</a>
      <a class="cn4" href="#f-b4">4 Recta</a>
      <a class="cn5" href="#f-b5">5 Funciones</a>
      <a class="cnx" href="#f-expres">★ Exprés</a>
    </nav>
    <div class="sheet-actions">
      <button class="btn-print" type="button" onclick="window.print()">Imprimir ficha</button>
    </div>
  </div>
  <div class="kit-sub" id="subExpres">
    <div class="sheet-actions">
      <button class="ghost" id="btnRecitar" type="button" aria-pressed="false">Modo recitar</button>
      <button class="btn-print" type="button" onclick="window.print()">Imprimir 2 páginas</button>
    </div>
  </div>
</header>

<div id="kitMain">
{KIT_INICIO}

<section id="view-practica" class="app-view" aria-label="Práctica interactiva">
{prac_header}
{prac_main}
</section>

<section id="view-formulas" class="app-view" aria-label="Ficha de fórmulas">
{form_main}
</section>

<section id="view-expres" class="app-view" aria-label="Hoja exprés">
  <p class="recite-banner hidden no-print" id="reciteBanner">Las fórmulas están tapadas. Toca una para verla un momento. Vuelve a pulsar «Dejar de recitar» cuando termines.</p>
{expr_main}
</section>

<footer class="kit-foot">
  <p>Esta es una <b>herramienta de refuerzo</b>. No se garantizan resultados sin el compromiso del alumno.</p>
  <p>Desarrollada por <a href="https://focampo.com" target="_blank" rel="noopener noreferrer">Francisco Ocampo</a>.</p>
</footer>
</div>

<nav class="kit-tabs" aria-label="Secciones del kit">
  <button type="button" data-vista="inicio" onclick="irA('inicio')">{SVG_HOME} Inicio</button>
  <button type="button" data-vista="practica" onclick="irA('practica')">{SVG_PLAY} Practicar</button>
  <button type="button" data-vista="formulas" onclick="irA('formulas')">{SVG_BOOK} Fórmulas</button>
  <button type="button" data-vista="expres" onclick="irA('expres')">{SVG_EDIT} Exprés</button>
</nav>

{prac_dialog}
{prac_toast}

<script>
{prac_js}
{KIT_JS}
</script>
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    kb = OUT.stat().st_size / 1024
    print(f"Escrito {OUT.name} ({kb:.1f} KB, {html.count(chr(10))+1} líneas)")


if __name__ == "__main__":
    main()
