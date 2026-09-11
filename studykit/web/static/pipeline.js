(function () {
  const TOKEN_KEY = "studykit.token";

  function saveToken(value) {
    if (!value) return;
    try {
      sessionStorage.setItem(TOKEN_KEY, value);
    } catch (_err) {
      /* private mode */
    }
  }

  function readToken() {
    try {
      return sessionStorage.getItem(TOKEN_KEY) || "";
    } catch (_err) {
      return "";
    }
  }

  document.querySelectorAll("form[data-remember-token]").forEach((form) => {
    const input = form.querySelector("input[name='token']");
    if (input && !input.value) input.value = readToken();
    form.addEventListener("submit", () => {
      if (input) saveToken(input.value);
      const btn = form.querySelector("[type='submit']");
      if (btn) {
        btn.disabled = true;
        const label = btn.getAttribute("data-busy") || "Trabajando…";
        btn.innerHTML = '<span class="spin" aria-hidden="true"></span>' + label;
      }
    });
  });

  const fileInput = document.querySelector("[data-file-input]");
  const fileBox = document.querySelector("[data-file-box]");
  if (fileInput && fileBox) {
    const label = fileBox.querySelector("[data-file-label]");
    fileInput.addEventListener("change", () => {
      const name = fileInput.files && fileInput.files[0] ? fileInput.files[0].name : "";
      fileBox.classList.toggle("has-file", Boolean(name));
      if (label) label.textContent = name || "Elige un .md, .txt o .json";
    });
  }

  document.querySelectorAll("[data-toggle-pw]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = btn.getAttribute("data-toggle-pw");
      const input = id ? document.getElementById(id) : null;
      if (!input) return;
      const show = input.type === "password";
      input.type = show ? "text" : "password";
      btn.textContent = show ? "Ocultar" : "Mostrar";
    });
  });

  document.querySelectorAll("[data-copy]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const sel = btn.getAttribute("data-copy");
      const el = sel ? document.querySelector(sel) : null;
      const raw = el && el.getAttribute("href")
        ? new URL(el.getAttribute("href"), window.location.origin).href
        : (el ? el.textContent : "");
      const label = btn.textContent;
      try {
        await navigator.clipboard.writeText((raw || "").trim());
        btn.textContent = "Copiado";
      } catch (_err) {
        btn.textContent = "No se pudo copiar";
      }
      window.setTimeout(() => {
        btn.textContent = label;
      }, 1600);
    });
  });

  const preview = document.querySelector("[data-preview]");
  if (preview) {
    const token = readToken();
    if (token) {
      const url = new URL(preview.getAttribute("href"), window.location.origin);
      url.searchParams.set("token", token);
      preview.setAttribute("href", url.pathname + url.search);
    }
  }

  const poll = document.querySelector("[data-poll]");
  if (poll) {
    const kitId = poll.getAttribute("data-poll");
    const expected = poll.getAttribute("data-status");
    const tick = async () => {
      try {
        const res = await fetch("/kits/" + kitId, { headers: { Accept: "application/json" } });
        if (!res.ok) return;
        const body = await res.json();
        if (body.status && body.status !== expected) {
          window.location.reload();
        }
      } catch (_err) {
        /* keep polling */
      }
    };
    setInterval(tick, 2000);
  }
})();
