# 🎓 Guía de Estudio — Matemática IV Bachillerato
### Examen de Admisión · Jornada intensiva de 6.5 horas

> **Para:** estudiante de ~15 años (Secundaria / IV Bachillerato)
> **Objetivo:** repasar los 5 bloques del temario de forma **activa** (Enseño → Ejemplo → Practico)
> **Fuente:** [`IV Matemática 2026.pdf`](../../datos/pdf/IV Matemática 2026.pdf)

---

## ⏱️ Cronograma de la jornada (6h 30m)

| # | Bloque | Tiempo | Punteo en examen |
|---|--------|--------|------------------|
| 1 | Geometría y Trigonometría | 1 h 30 m | /20 puntos |
| 2 | Factorización de expresiones algebraicas | 1 h | /10 puntos |
| 3 | Desigualdades lineales, polinomiales y racionales | 1 h 15 m | /25 puntos |
| 4 | Ecuación de la recta y geometría de coordenadas | 1 h 15 m | /25 puntos |
| 5 | Introducción a las funciones | 1 h | /20 puntos |
| — | **Total de estudio** | **6 h** | **/100** |
| — | 🧠 Repaso exprés + examen simulado | **30 m** | — |

> **Nota:** los bloques con más peso (3 y 4) reciben más tiempo que su proporción simple,
> y el bloque 1 —aunque pesa 20— es el más denso en fórmulas, por eso lleva 1h30.

---

## 🧭 Cómo usar esta guía (metodología "Enseño → Ejemplo → Practico")

Cada tema dentro de los bloques sigue **siempre** el mismo patrón de 3 pasos:

1. **👨‍🏫 Enseño** — Explicación breve y clara del concepto (qué es, para qué sirve, cuándo se usa).
2. **✏️ Ejemplo** — Un ejercicio **resuelto paso a paso**, como se espera que lo resuelvas en el examen.
3. **💪 Practico** — Ejercicios para que los intentes **tú solo** (sin mirar la solución). Después revisa.

**Reglas de oro durante la jornada:**
- 🚫 Nada de solo *leer*: **cada ejemplo resuelto debes replicarlo en tu cuaderno**.
- ✅ Cuando falles un ejercicio, **vuelve al ejemplo** y detecta en qué paso te equivocaste.
- 📝 Usa papel y lápiz: las matemáticas del examen se hacen a mano.
- ⏰ En los ejercicios de práctica, **ponte límite de tiempo** (el examen total es de 2 horas / 100 puntos).
- 🧮 **Calculadora:** en la prueba pueden no dejarla, así que **practica el cálculo manual** (fracciones, cuadrados, operaciones básicas) hasta que salgan fluidos.

> **Herramientas complementarias:**
> - **Kit web (todo en uno, para celular / tablet / computadora o Netlify):**
>   [`index.html`](../html/index.html) — práctica + fórmulas + hoja exprés.
> - Tablas de conversión y fórmulas (para memorizar):
>   [`IV Matemática 2026 - Tablas y fórmulas.md`](IV Matemática 2026 - Tablas y fórmulas.md)
> - Ficha visual para imprimir:
>   PDF: [`IV Matemática 2026 - Tablas y fórmulas.pdf`](../pdf/IV Matemática 2026 - Tablas y fórmulas.pdf)
> - Hoja exprés (2 páginas, para pegar en el cuaderno):
>   PDF: [`IV Matemática 2026 - Hoja exprés.pdf`](../pdf/IV Matemática 2026 - Hoja exprés.pdf)

---

# 🟦 BLOQUE 1 — Geometría y Trigonometría  (20 puntos · 1h30)

**Temas del examen:** hallar ángulos con variables · teoremas de ángulos (opuestos por el vértice, complementarios, suplementarios, paralelas cortadas por transversal, suma de ángulos de un triángulo) · resolver triángulo rectángulo · teorema de Pitágoras y razones trigonométricas (seno, coseno, tangente) con problemas de aplicación.

---

## 1.1 Ángulos y sus relaciones

### 👨‍🏫 Enseño
- **Ángulos complementarios:** dos ángulos suman **90°**. → si uno vale `x`, el otro es `90 − x`.
- **Ángulos suplementarios:** dos ángulos suman **180°**. → si uno vale `x`, el otro es `180 − x`.
- **Ángulos opuestos por el vértice:** son **iguales**.
- **Dos rectas paralelas cortadas por una transversal** generan 8 ángulos:
  - Los **alternos internos** son iguales.
  - Los **correspondientes** son iguales.
  - Los **internos del mismo lado** suman 180°.
- **Suma de ángulos internos de un triángulo:** siempre **180°**.
  - Si dos ángulos miden `a` y `b`, el tercero mide `180 − a − b`.

### ✏️ Ejemplo 1 — "Ángulos con variables"
Dos ángulos son **complementarios** y uno mide el **doble** del otro. ¿Cuánto mide cada uno?

**Solución paso a paso:**
1. Llamemos `x` al ángulo pequeño. El grande mide `2x`.
2. Como son complementarios: `x + 2x = 90`.
3. Sumamos: `3x = 90` → `x = 90 ÷ 3 = 30`.
4. Entonces: ángulo pequeño = **30°**, ángulo grande = **60°**. ✅ *(Verifica: 30 + 60 = 90)*

### ✏️ Ejemplo 2 — "Teoremas de ángulos con paralelas"
Dos rectas paralelas son cortadas por una transversal. Uno de los ángulos internos mide **65°**. ¿Cuánto miden los otros?

**Solución paso a paso:**
1. Haz el dibujo: dos líneas horizontales paralelas y una línea diagonal que las cruce.
2. Marca el ángulo de 65° en una esquina interna.
3. El ángulo **opuesto por el vértice** a 65° también mide **65°**.
4. El ángulo **adyacente** (interno del mismo lado) es suplementario: `180 − 65 = 115°`.
5. Por el teorema de **alternos internos**, el ángulo "del otro lado" y abajo mide **65°**.
6. Siguiendo la misma lógica: la figura queda con ángulos de **65°, 115°, 65°, 115°** alternados. ✅

### ✏️ Ejemplo 3 — "Suma de ángulos del triángulo"
Un triángulo tiene ángulos de `2x`, `3x` y `4x`. Halla cada ángulo.

**Solución paso a paso:**
1. La suma debe ser 180: `2x + 3x + 4x = 180`.
2. `9x = 180` → `x = 20`.
3. Ángulos: `2·20 = 40°`, `3·20 = 60°`, `4·20 = 80°`. ✅ *(Verifica: 40+60+80 = 180)*

### 💪 Practico
1. Dos ángulos son **suplementarios** y su diferencia es de **40°**. Halla ambos ángulos. *(pista: plantea `x − y = 40` y `x + y = 180`)*
2. En dos paralelas cortadas por una transversal, un ángulo correspondiente mide `3x + 10` y su pareja `x + 50`. Halla `x` y el valor del ángulo.
3. Un triángulo isósceles tiene su ángulo del vértice en `50°`. ¿Cuánto miden los ángulos de la base? *(los de la base son iguales)*
4. Dos ángulos son complementarios y uno es `22°` mayor que el otro. ¿Cuánto mide cada uno?

<details>
<summary>🔎 Ver soluciones</summary>

1. `x = 110°, y = 70°` (suma 180, diferencia 40).
2. Como son correspondientes son iguales: `3x + 10 = x + 50` → `2x = 40` → `x = 20`; ángulo = `70°`.
3. Base: `(180 − 50) ÷ 2 = 65°` cada uno.
4. `x + (x+22) = 90` → `2x = 68` → `x = 34°` y `56°`.
</details>

---

## 1.2 Teorema de Pitágoras

### 👨‍🏛️ Enseño
En un **triángulo rectángulo** (uno de sus ángulos mide 90°):
- La **hipotenusa** `c` es el lado **opuesto al ángulo recto** (el más largo).
- Los **catetos** `a` y `b` forman el ángulo recto.
- **Fórmula:** `a² + b² = c²`
- **Para hallar la hipotenusa:** `c = √(a² + b²)`
- **Para hallar un cateto:** `a = √(c² − b²)`

> 🛑 **Error común:** la hipotenusa **siempre** va sola en la fórmula (`c² = a² + b²`). No la pongas como cateto.

### ✏️ Ejemplo — "Usar Pitágoras"
Un triángulo rectángulo tiene catetos de **6 cm** y **8 cm**. ¿Cuánto mide la hipotenusa?

**Solución paso a paso:**
1. Identifica: `a = 6`, `b = 8`, buscamos `c`.
2. `c² = 6² + 8² = 36 + 64 = 100`.
3. `c = √100 = 10 cm`. ✅

### ✏️ Ejemplo — "Pitágoras inverso"
Un triángulo rectángulo tiene hipotenusa **13** y un cateto **5**. Halla el otro cateto.

**Solución paso a paso:**
1. `b² = c² − a² = 13² − 5² = 169 − 25 = 144`.
2. `b = √144 = 12`. ✅

### 💪 Practico
1. Catetos de **9 y 12**. Halla la hipotenusa.
2. Hipotenusa **25**, cateto **7**. Halla el otro cateto.
3. Una escalera de **5 m** apoyada en una pared toca el suelo a **3 m** de la base. ¿A qué altura llega sobre la pared?
4. Un rectángulo mide **8 cm × 15 cm**. ¿Cuánto mide su diagonal? *(pista: la diagonal es la hipotenusa)*

<details>
<summary>🔎 Ver soluciones</summary>

1. `c = √(81 + 144) = √225 = 15`.
2. `b = √(625 − 49) = √576 = 24`.
3. `h = √(25 − 9) = √16 = 4 m`.
4. `d = √(64 + 225) = √289 = 17 cm`.
</details>

---

## 1.3 Razones trigonométricas (seno, coseno, tangente)

### 👨‍🏫 Enseño
En un triángulo rectángulo, para un ángulo agudo `θ`:
- **sen θ** = cateto **opuesto** ÷ hipotenusa = `op / hip`
- **cos θ** = cateto **adyacente** ÷ hipotenusa = `ady / hip`
- **tan θ** = cateto **opuesto** ÷ cateto **adyacente** = `op / ady`

**Frase para recordar:** *"SOH-CAH-TOA"* → **S**en = **O**puesto/**H**ipotenusa, **C**oseno = **A**dyacente/**H**ipotenusa, **T**angente = **O**puesto/**A**dyacente.

**Cuándo usar cada una:**
- Tengo **opuesto y hipotenusa** → `seno`
- Tengo **adyacente y hipotenusa** → `coseno`
- Tengo **opuesto y adyacente** → `tangente`
- Para **hallar un ángulo** usa la inversa: `θ = sen⁻¹(...)`, `θ = cos⁻¹(...)`, `θ = tan⁻¹(...)`

### ✏️ Ejemplo — "Resolver un triángulo rectángulo"
Dado un triángulo rectángulo con ángulo `θ = 30°` e hipotenusa de **10**. Halla los dos catetos.

**Solución paso a paso:**
1. Para hallar el cateto opuesto al ángulo de 30°: `sen 30° = op / 10`.
2. Como `sen 30° = 0.5` → `0.5 = op / 10` → `op = 0.5 × 10 = 5`.
3. Para hallar el cateto adyacente: `cos 30° = ady / 10`.
4. `cos 30° ≈ 0.866` → `ady ≈ 8.66`.
5. *(Verificación con Pitágoras: 5² + 8.66² ≈ 25 + 75 ≈ 100 = 10²)* ✅

### ✏️ Ejemplo — "Problema de aplicación"
Un observador mira la punta de un árbol con un ángulo de elevación de **45°**. Está a **12 m** de la base. ¿Qué altura tiene el árbol?

**Solución paso a paso:**
1. Dibuja: triángulo rectángulo, base `12 m`, ángulo en el observador `45°`, altura = cateto opuesto.
2. Usamos tangente (tenemos adyacente y queremos opuesto): `tan 45° = altura / 12`.
3. `tan 45° = 1` → `altura = 1 × 12 = 12 m`. ✅

> 💡 **Dato clave de memoria:** `tan 45° = 1`, `sen 30° = 0.5`, `cos 60° = 0.5`. Saber estos tres ahorra mucho tiempo.

### 💪 Practico
1. Un ángulo `θ` tiene cateto opuesto **6** e hipotenusa **10**. Halla `sen θ`, `cos θ` y `tan θ`. *(pista: primero halla el adyacente con Pitágoras: es 8)*
2. Un triángulo rectángulo tiene ángulo de **60°** y cateto adyacente de **4**. Halla la hipotenusa. *(pista: `cos 60° = 0.5`)*
3. Desde lo alto de un edificio de **30 m**, el ángulo de depresión hacia un auto es de **45°**. ¿A qué distancia horizontal está el auto?
4. Una rampa mide **8 m** y sube con una inclinación de **30°**. ¿A qué altura llega?

<details>
<summary>🔎 Ver soluciones</summary>

1. `sen θ = 6/10 = 0.6`; ady = 8 → `cos θ = 0.8`; `tan θ = 6/8 = 0.75`.
2. `cos 60° = ady/hip` → `0.5 = 4/hip` → `hip = 8`.
3. `tan 45° = 30/d` → `1 = 30/d` → `d = 30 m`.
4. `sen 30° = h/8` → `0.5 = h/8` → `h = 4 m`.
</details>

---

# 🟩 BLOQUE 2 — Factorización  (10 puntos · 1h)

**Temas del examen:** factorizar completamente usando todos los casos: factor común, agrupación, diferencia de cuadrados, suma y diferencia de cubos, trinomio cuadrado perfecto, trinomio `x²+bx+c` y `ax²+bx+c`.

---

## 2.1 Factor común y agrupación

### 👨‍🏫 Enseño
- **Factor común:** busca lo que se repite en **todos** los términos (número y/o letra) y sácalo.
  `ax + ay = a(x + y)`
- **Agrupación:** cuando hay 4 términos, agrupa de a pares y saca factor común de cada grupo, para que quede un paréntesis repetido.
  `ax + ay + bx + by = a(x+y) + b(x+y) = (a+b)(x+y)`

### ✏️ Ejemplo — "Factor común"
Factoriza: `15x² − 10x`

**Solución paso a paso:**
1. El factor común de `15` y `10` es `5`; la `x` está en ambos (mínimo exponente 1). Factor común = `5x`.
2. Divide cada término: `15x² ÷ 5x = 3x`; `10x ÷ 5x = 2`.
3. Resultado: `5x(3x − 2)`. ✅ *(Verifica multiplicando: 5x·3x = 15x² y 5x·2 = 10x)*

### ✏️ Ejemplo — "Agrupación"
Factoriza: `6x³ + 4x² + 9x + 6`

**Solución paso a paso:**
1. Agrupa: `(6x³ + 4x²) + (9x + 6)`.
2. Factor común del 1er grupo: `2x²`. → `2x²(3x + 2)`.
3. Factor común del 2º grupo: `3`. → `3(3x + 2)`.
4. Nota que `(3x + 2)` se repite: `(3x + 2)(2x² + 3)`. ✅

### 💪 Practico
1. Factoriza: `12a³ − 18a²`.
2. Factoriza: `x² + xy − 3x − 3y` *(agrupa)*.
3. Factoriza: `24m⁴n − 36m³n²`.

<details>
<summary>🔎 Ver soluciones</summary>

1. Factor común `6a²`: `6a²(2a − 3)`.
2. `x(x+y) − 3(x+y) = (x+y)(x−3)`.
3. Factor común `12m³n`: `12m³n(2m − 3n)`.
</details>

---

## 2.2 Diferencia de cuadrados

### 👨‍🏫 Enseño
- Solo se factoriza cuando hay **una resta** entre dos **cuadrados perfectos**.
- **Fórmula:** `a² − b² = (a + b)(a − b)`
- **Ojo:** una **suma** de cuadrados `a² + b²` **NO** se factoriza con números reales (déjala así).

### ✏️ Ejemplo — "Diferencia de cuadrados"
Factoriza: `x² − 49`

**Solución paso a paso:**
1. Identifica los cuadrados: `x² = (x)²` y `49 = (7)²`.
2. Aplica la fórmula: `(x + 7)(x − 7)`. ✅

### ✏️ Ejemplo — "Factorizar completamente"
Factoriza: `3x² − 27`

**Solución paso a paso:**
1. Primero saca factor común `3`: `3(x² − 9)`.
2. Ahora `x² − 9` es diferencia de cuadrados: `(x + 3)(x − 3)`.
3. Resultado final (completamente factorizado): `3(x + 3)(x − 3)`. ✅
> 🛑 **"Completamente"** significa que debes seguir factorizando hasta que no quede ningún caso aplicable.

### 💪 Practico
1. Factoriza: `y² − 81`.
2. Factoriza: `16x² − 25`.
3. Factoriza completamente: `2x² − 32`.

<details>
<summary>🔎 Ver soluciones</summary>

1. `(y + 9)(y − 9)`.
2. `(4x + 5)(4x − 5)`.
3. `2(x² − 16) = 2(x + 4)(x − 4)`.
</details>

---

## 2.3 Suma y diferencia de cubos

### 👨‍🏫 Enseño
- **Suma de cubos:** `a³ + b³ = (a + b)(a² − ab + b²)`
- **Diferencia de cubos:** `a³ − b³ = (a − b)(a² + ab + b²)`
- **Recordar el signo:** el primer paréntesis copia el signo (más o menos); en el segundo, el **primer** término va positivo, el **del medio lleva el signo contrario**, y el último siempre `+`.

### ✏️ Ejemplo — "Diferencia de cubos"
Factoriza: `x³ − 27`

**Solución paso a paso:**
1. `27 = 3³`, así que `a = x` y `b = 3`.
2. Aplica `a³ − b³ = (a − b)(a² + ab + b²)`.
3. Resultado: `(x − 3)(x² + 3x + 9)`. ✅

### ✏️ Ejemplo — "Suma de cubos"
Factoriza: `8x³ + 1`

**Solución paso a paso:**
1. `8x³ = (2x)³` y `1 = 1³`, así que `a = 2x` y `b = 1`.
2. Aplica `a³ + b³ = (a + b)(a² − ab + b²)`.
3. Resultado: `(2x + 1)(4x² − 2x + 1)`. ✅

### 💪 Practico
1. Factoriza: `y³ + 8`.
2. Factoriza: `27 − m³`.
3. Factoriza: `64x³ − 125`.

<details>
<summary>🔎 Ver soluciones</summary>

1. `(y + 2)(y² − 2y + 4)`.
2. `(3 − m)(9 + 3m + m²)`.
3. `(4x − 5)(16x² + 20x + 25)`.
</details>

---

## 2.4 Trinomio cuadrado perfecto (TCP)

### 👨‍🏫 Enseño
Un trinomio es **cuadrado perfecto** si tiene la forma:
- `a² + 2ab + b² = (a + b)²`
- `a² − 2ab + b² = (a − b)²`

**Cómo reconocerlo:**
1. El 1er y 3er término son **cuadrados perfectos** (con signo +).
2. El término del medio es **el doble** de la raíz del primero por la raíz del tercero: `2·√(1º)·√(3º)`.

### ✏️ Ejemplo — "Reconocer y factorizar un TCP"
Factoriza: `x² + 10x + 25`

**Solución paso a paso:**
1. `√(x²) = x` y `√25 = 5`.
2. Verifica el medio: `2 · x · 5 = 10x` ✓ (coincide).
3. Como el signo del medio es `+`: `(x + 5)²`. ✅

### ✏️ Ejemplo — "TCP con signo negativo"
Factoriza: `x² − 12x + 36`

**Solución paso a paso:**
1. `√(x²) = x`, `√36 = 6`, y `2·x·6 = 12x` ✓.
2. Signo del medio `−`: `(x − 6)²`. ✅

### 💪 Practico
1. Factoriza: `y² + 14y + 49`.
2. Factoriza: `9x² − 24x + 16`.
3. Factoriza: `x² + 6x + 9`.

<details>
<summary>🔎 Ver soluciones</summary>

1. `(y + 7)²` (2·y·7 = 14y ✓).
2. `(3x − 4)²` (√9x² = 3x, √16 = 4, 2·3x·4 = 24x ✓).
3. `(x + 3)²`.
</details>

---

## 2.5 Trinomio de la forma x² + bx + c

### 👨‍🏫 Enseño
Para factorizar `x² + bx + c` (coeficiente de `x²` = 1):
- Busca **dos números** que **multipliquen** para dar `c` y que **sumen** para dar `b`.
- Resultado: `(x + p)(x + q)` donde `p·q = c` y `p+q = b`.

### ✏️ Ejemplo — "x² + bx + c"
Factoriza: `x² + 7x + 12`

**Solución paso a paso:**
1. Busco dos números que multiplicados den **12** y sumados den **7**.
2. Pares de 12: (1,12) suma 13 ✗ · (2,6) suma 8 ✗ · (3,4) suma **7** ✓.
3. Resultado: `(x + 3)(x + 4)`. ✅

### ✏️ Ejemplo — "Con signos negativos"
Factoriza: `x² − 5x + 6`

**Solución paso a paso:**
1. Dos números que **multipliquen** +6 y **sumen** −5. Ambos deben ser negativos.
2. (−2, −3): multiplican `+6` ✓ y suman `−5` ✓.
3. Resultado: `(x − 2)(x − 3)`. ✅

### 💪 Practico
1. Factoriza: `x² + 9x + 20`.
2. Factoriza: `x² − 7x + 12`.
3. Factoriza: `x² + 2x − 15`. *(pista: uno positivo, uno negativo)*

<details>
<summary>🔎 Ver soluciones</summary>

1. `(x + 4)(x + 5)` (4·5=20, 4+5=9).
2. `(x − 3)(x − 4)` (−3·−4=12, −7).
3. `(x + 5)(x − 3)` (5·−3=−15, 5−3=2).
</details>

---

## 2.6 Trinomio de la forma ax² + bx + c

### 👨‍🏫 Enseño
Cuando el coeficiente de `x²` **no es 1** (forma `ax² + bx + c`), el método más confiable para el examen es el **método del ac**:
1. Multiplica `a · c`.
2. Busca dos números que **multipliquen** `a·c` y **sumen** `b`.
3. Parte el término del medio con esos dos números y **agrupa**.
4. Saca factor común por grupos (igual que en 2.1).

> **Alternativa (ensayo-error):** prueba binomios `(px + q)(rx + s)` tal que `p·r = a` y `q·s = c`, ajustando hasta que el término del medio dé `b`.

### ✏️ Ejemplo — "Método del ac"
Factoriza: `2x² + 7x + 3`

**Solución paso a paso:**
1. `a·c = 2·3 = 6`. Busco dos números que multiplicados den 6 y sumados den **7**: (1, 6) ✓.
2. Parte el término del medio: `2x² + 1x + 6x + 3`.
3. Agrupa: `(2x² + x) + (6x + 3)`.
4. Factor común de cada grupo: `x(2x + 1) + 3(2x + 1)`.
5. Saco el paréntesis común: `(2x + 1)(x + 3)`. ✅

### ✏️ Ejemplo — "Con negativo"
Factoriza: `6x² − 11x − 10`

**Solución paso a paso:**
1. `a·c = 6·(−10) = −60`. Dos números que multipliquen `−60` y sumen `−11`: (−15, 4) ✓.
2. Parte el medio: `6x² − 15x + 4x − 10`.
3. Agrupa y factoriza: `3x(2x − 5) + 2(2x − 5)`.
4. Resultado: `(2x − 5)(3x + 2)`. ✅

### 💪 Practico
1. Factoriza: `3x² + 10x + 8`.
2. Factoriza: `2x² − x − 6`.
3. Factoriza: `4x² + 12x + 9`. *(pista: ¿será un TCP disfrazado?)*

<details>
<summary>🔎 Ver soluciones</summary>

1. `a·c=24`, números (6,4): `3x²+6x+4x+8` → `3x(x+2)+4(x+2)` = `(x+2)(3x+4)`.
2. `a·c=−12`, números (−4, 3): `2x²−4x+3x−6` → `2x(x−2)+3(x−2)` = `(x−2)(2x+3)`.
3. Es TCP: `(2x + 3)²` (2·2x·3 = 12x ✓).
</details>

---

# 🟨 BLOQUE 3 — Desigualdades  (25 puntos · 1h15)

**Temas del examen:** notación conjuntista/de desigualdad/gráfica · lineales con varias ocurrencias de la variable y signos de agrupación · valor absoluto · polinómicas · racionales.

---

## 3.1 Notación: conjuntos, desigualdad y gráfica

### 👨‍🏫 Enseño
Existen **3 formas** de expresar la solución de una desigualdad, y en el examen pueden pedirte cualquiera (o pasar de una a otra):
- **Notación de desigualdad:** `x > 3`
- **Notación de intervalo / conjuntista:** `(3, ∞)` y se lee "todos los x desde 3 hasta infinito, sin incluir el 3".
- **Gráfica en la recta numérica:** dibuja la recta y una **flecha** hacia la derecha (para `>`) desde un **punto hueco** (○ = no incluye) o **relleno** (● = incluye).

**Tipos de paréntesis:**
- `(` o `)` = **no incluye** el extremo (desigualdad `>` o `<`).
- `[` o `]` = **sí incluye** el extremo (desigualdad `≥` o `≤`).

**Símbolos de conjuntos:** `∪` (unión, "o") y `∩` (intersección, "y").

| Desigualdad | Intervalo | Gráfica (extremo) |
|-------------|-----------|-------------------|
| `x > 3` | `(3, ∞)` | ○ hueco → derecha |
| `x ≥ 3` | `[3, ∞)` | ● relleno → derecha |
| `x < 3` | `(−∞, 3)` | ○ hueco → izquierda |
| `−2 < x ≤ 5` | `(−2, 5]` | ○ en −2, ● en 5 |

### ✏️ Ejemplo — "Traducir entre notaciones"
Expresa `x ≥ −1` en notación de intervalo y dibuja su gráfica.

**Solución paso a paso:**
1. Como es `≥`, incluye el `−1`: intervalo `[−1, ∞)`.
2. Gráfica: punto **relleno** en `−1` y flecha hacia la **derecha**.

### 💪 Practico
1. Escribe en intervalo y dibuja: `x < 2`.
2. Escribe en desigualdad e intervalo: "desde −3 hasta 4, incluyendo el 4 pero no el −3".
3. Escribe en desigualdad: `(−∞, 7]`.

<details>
<summary>🔎 Ver soluciones</summary>

1. `(−∞, 2)`, punto hueco en 2, flecha a la izquierda.
2. `−3 < x ≤ 4` → intervalo `(−3, 4]`.
3. `x ≤ 7`.
</details>

---

## 3.2 Desigualdades lineales

### 👨‍🏫 Enseño
Se resuelven como las ecuaciones, con **una diferencia crítica**:
> ⚠️ **Cuando multiplicas o divides por un número NEGATIVO, invierte el sentido de la desigualdad.**

Ejemplos de la regla: si `−x > 5`, al multiplicar por `−1` queda `x < −5`.

**Pasos:**
1. Elimina signos de agrupación (paréntesis, corchetes) distribuyendo.
2. Junta las `x` de un lado y los números del otro.
3. Despeja, cuidando **invertir** si divides por negativo.

### ✏️ Ejemplo — "Con varias ocurrencias de x y signos de agrupación"
Resuelve: `3(2x − 4) > x + 7 − 2x`

**Solución paso a paso:**
1. Distribuye: `6x − 12 > x + 7 − 2x`.
2. Reduce del lado derecho: `x − 2x = −x`, así que `6x − 12 > −x + 7`.
3. Suma `x` a ambos lados: `7x − 12 > 7`.
4. Suma 12: `7x > 19`.
5. Divide entre 7 (positivo, no cambia): `x > 19/7` ≈ `2.71`.

**Respuesta:** `x > 19/7`, intervalo `(19/7, ∞)`.

### ✏️ Ejemplo — "Invertir por negativo"
Resuelve: `5 − 2x ≥ 11`

**Solución paso a paso:**
1. Resta 5: `−2x ≥ 6`.
2. Divide entre `−2` → **invierte**: `x ≤ −3`.
3. Intervalo `(−∞, −3]`. ✅

### 💪 Practico
1. Resuelve y expresa en intervalo: `2x − 5 < 4x + 1`.
2. Resuelve: `4(3 − x) ≥ 2(x + 6)`.
3. Resuelve: `7 − 3x < 2 − 5x + 6`.

<details>
<summary>🔎 Ver soluciones</summary>

1. `2x − 5 < 4x + 1` → `−6 < 2x` → `x > −3` → `(−3, ∞)`.
2. `12 − 4x ≥ 2x + 12` → `−6x ≥ 0` → **invierte** → `x ≤ 0` → `(−∞, 0]`.
3. `7 − 3x < 8 − 5x` → `2x < 1` → `x < 1/2` → `(−∞, 1/2)`.
</details>

---

## 3.3 Desigualdades con valor absoluto

### 👨‍🏫 Enseño
El valor absoluto `|X|` es la **distancia** de `X` al cero, siempre ≥ 0. Hay **dos casos**:

**Caso 1 — Menor que:** `|X| < a` (con `a > 0`)
- Significa que `X` está **entre** `−a` y `a`.
- Se convierte en: `−a < X < a`

**Caso 2 — Mayor que:** `|X| > a` (con `a > 0`)
- Significa que `X` está **lejos** de 0 (más allá de `−a` o más allá de `a`).
- Se convierte en **dos** desigualdades unidas por `o` (unión `∪`):
  `X < −a` **o** `X > a`

> 🛑 El caso `≤` se maneja igual que `<` (con extremos incluidos), y `≥` igual que `>`.

### ✏️ Ejemplo — "Caso menor que"
Resuelve: `|x − 3| ≤ 5`

**Solución paso a paso:**
1. Como es `≤`, escribimos doble desigualdad: `−5 ≤ x − 3 ≤ 5`.
2. Suma 3 a los tres lados: `−5 + 3 ≤ x ≤ 5 + 3` → `−2 ≤ x ≤ 8`.
3. Intervalo: `[−2, 8]`. ✅

### ✏️ Ejemplo — "Caso mayor que"
Resuelve: `|2x + 1| > 7`

**Solución paso a paso:**
1. Como es `>`, se separa en **dos** casos:
   - Caso A: `2x + 1 < −7` → `2x < −8` → `x < −4`.
   - Caso B: `2x + 1 > 7` → `2x > 6` → `x > 3`.
2. Solución (unión): `x < −4` **o** `x > 3`.
3. En intervalo: `(−∞, −4) ∪ (3, ∞)`. ✅

### 💪 Practico
1. Resuelve: `|x| < 4` y expresa en intervalo.
2. Resuelve: `|x + 2| ≥ 3`.
3. Resuelve: `|3x − 6| ≤ 9`.

<details>
<summary>🔎 Ver soluciones</summary>

1. `−4 < x < 4` → `(−4, 4)`.
2. Dos casos: `x + 2 ≤ −3` → `x ≤ −5` **o** `x + 2 ≥ 3` → `x ≥ 1` → `(−∞, −5] ∪ [1, ∞)`.
3. `−9 ≤ 3x − 6 ≤ 9` → `−3 ≤ 3x ≤ 15` → `−1 ≤ x ≤ 5` → `[−1, 5]`.
</details>

---

## 3.4 Desigualdades polinómicas

### 👨‍🏫 Enseño
**Método de los puntos de prueba (o del signo):**
1. Lleva todo a un lado (déjalo en `f(x) > 0` o `< 0`).
2. Factoriza `f(x)` (¡usa el bloque 2!).
3. Halla las **raíces** (valores donde cada factor vale 0).
4. Ubica las raíces en la recta → dividen la recta en **intervalos**.
5. Toma un **número de prueba** en cada intervalo y evalúa el signo del producto.
6. Elige los intervalos donde el signo cumple la desigualdad.

### ✏️ Ejemplo — "Polinómica con producto"
Resuelve: `(x − 2)(x + 1) > 0`

**Solución paso a paso:**
1. Ya está factorizada. Raíces: `x = 2` y `x = −1`.
2. La recta queda dividida en 3 intervalos: `(−∞, −1)`, `(−1, 2)`, `(2, ∞)`.
3. Prueba un número en cada uno:
   - En `(−∞,−1)` prueba `x = −2`: `(−2−2)(−2+1) = (−4)(−1) = +` → cumple `> 0` ✓
   - En `(−1,2)` prueba `x = 0`: `(0−2)(0+1) = (−2)(1) = −` → no cumple ✗
   - En `(2,∞)` prueba `x = 3`: `(3−2)(3+1) = (1)(4) = +` → cumple ✓
4. Solución: `x < −1` **o** `x > 2` → `(−∞, −1) ∪ (2, ∞)`. ✅

### ✏️ Ejemplo — "Necesita factorizar primero"
Resuelve: `x² − 5x + 6 ≤ 0`

**Solución paso a paso:**
1. Factoriza: `(x − 2)(x − 3) ≤ 0` (del bloque 2.5).
2. Raíces: `x = 2`, `x = 3`. Intervalos: `(−∞, 2)`, `(2, 3)`, `(3, ∞)`.
3. Prueba signos:
   - `x = 0`: `(−)(−) = +` ✗
   - `x = 2.5`: `(+)(−) = −` ✓ (cumple `≤ 0`)
   - `x = 4`: `(+)(+) = +` ✗
4. Como es `≤`, **incluye** las raíces: `[2, 3]`. ✅

### 💪 Practico
1. Resuelve: `(x + 1)(x − 4) < 0`.
2. Resuelve: `x² − 9 ≥ 0` *(pista: factoriza como diferencia de cuadrados)*.
3. Resuelve: `x² + x − 12 > 0`.

<details>
<summary>🔎 Ver soluciones</summary>

1. Raíces −1 y 4. Pruebas: `x=0` → `(+)·(−)=−` ✓. Solución `(−1, 4)`.
2. `(x+3)(x−3) ≥ 0`. `x=0`→`−` ✗; `x=−4`→`+` ✓; `x=4`→`+` ✓. Solución `(−∞, −3] ∪ [3, ∞)`.
3. `(x+4)(x−3) > 0`. `x=0`→`−` ✗. Solución `(−∞, −4) ∪ (3, ∞)`.
</details>

---

## 3.5 Desigualdades racionales

### 👨‍🏫 Enseño
Son del tipo `(numerador)/(denominador) > 0` (o `<`, `≥`, `≤`).
1. Lleva todo a un lado.
2. Factoriza numerador y denominador.
3. Halla las **raíces** del numerador **y** las del denominador.
4. ⚠️ **Las raíces del denominador NUNCA se incluyen en la solución** (dividir entre 0 no existe); si es `≥` o `≤`, las del numerador sí se incluyen.
5. Haz la tabla de signos y elige intervalos.

> 💡 **Atajo del signo:** el signo de `A/B` es el mismo que el signo de `A·B` (solo importa el producto de los signos), así que puedes tratarlo como una polinómica, cuidando el punto del denominador.

### ✏️ Ejemplo — "Racional"
Resuelve: `(x − 1) / (x + 2) > 0`

**Solución paso a paso:**
1. Numerador cero en `x = 1`; denominador cero en `x = −2` (¡no incluir!).
2. Intervalos: `(−∞, −2)`, `(−2, 1)`, `(1, ∞)`.
3. Prueba signos:
   - `x = −3`: `(−)/(−) = +` ✓
   - `x = 0`: `(−)/(+) = −` ✗
   - `x = 2`: `(+)/(+) = +` ✓
4. Solución: `(−∞, −2) ∪ (1, ∞)`. ✅ *(el `−2` queda excluido aunque sea `>`)*

### ✏️ Ejemplo — "Con ≥"
Resuelve: `(x + 3)/(x − 1) ≤ 0`

**Solución paso a paso:**
1. Numerador cero en `x = −3`; denominador cero en `x = 1` (excluido).
2. Intervalos: `(−∞, −3)`, `(−3, 1)`, `(1, ∞)`.
3. Prueba signos:
   - `x = −4`: `(−)/(−) = +` ✗
   - `x = 0`: `(+)/(−) = −` ✓
   - `x = 2`: `(+)/(+) = +` ✗
4. Como es `≤`, incluyo el `−3` (numerador) pero **no** el `1` (denominador): `[−3, 1)`. ✅

### 💪 Practico
1. Resuelve: `(x + 2)/(x − 3) < 0`.
2. Resuelve: `(2x − 4)/(x + 1) ≥ 0`.
3. Resuelve: `(x² − 1)/(x − 2) > 0`. *(pista: factoriza el numerador como `(x+1)(x−1)`)*

<details>
<summary>🔎 Ver soluciones</summary>

1. Raíces −2 y 3 (excluido). `x=0` → `(+)/(−)=−` ✓. Solución `(−2, 3)`.
2. Numerador: `2x−4=0 → x=2`; denominador `x=−1` (excluido). `x=0`→`(−)/(+)=−` ✗; `x=3`→`(+)/(+)=+` ✓; `x=−2`→`(−)/(−)=+` ✓. Solución `(−∞, −1) ∪ [2, ∞)`.
3. `(x+1)(x−1)/(x−2) > 0`. Raíces −1, 1 y 2(excl). `x=0`→`(+)(−)/(−)=+` ✓; `x=1.5`→`(−)... `(−1,1)` no cumple. Solución `(−1, 1) ∪ (2, ∞)`.
</details>

---

# 🟧 BLOQUE 4 — Ecuación de la recta y geometría de coordenadas  (25 puntos · 1h15)

**Temas del examen:** distancia entre dos puntos · punto medio · graficar una recta (forma estándar o pendiente-intersección) · determinar ecuación (2 puntos, pendiente+punto, intersecciones) · paralelas y perpendiculares · modelar situaciones reales.

---

## 4.1 Distancia y punto medio

### 👨‍🏫 Enseño
Dados dos puntos `A(x₁, y₁)` y `B(x₂, y₂)`:
- **Distancia:** `d = √[(x₂ − x₁)² + (y₂ − y₁)²]` *(es Pitágoras disfrazado)*.
- **Punto medio:** `M = ( (x₁+x₂)/2 , (y₁+y₂)/2 )`.

### ✏️ Ejemplo — "Distancia"
Halla la distancia entre `A(1, 2)` y `B(4, 6)`.

**Solución paso a paso:**
1. `x₂ − x₁ = 4 − 1 = 3`; `y₂ − y₁ = 6 − 2 = 4`.
2. `d = √(3² + 4²) = √(9 + 16) = √25 = 5`. ✅

### ✏️ Ejemplo — "Punto medio"
Halla el punto medio entre `A(1, 2)` y `B(4, 6)`.

**Solución paso a paso:**
1. `x = (1 + 4)/2 = 5/2 = 2.5`; `y = (2 + 6)/2 = 8/2 = 4`.
2. `M = (2.5, 4)`. ✅

### 💪 Practico
1. Distancia entre `(−2, 3)` y `(3, 7)`.
2. Punto medio entre `(0, 0)` y `(8, 6)`.
3. Distancia entre `(5, 1)` y `(5, 9)`. *(pista: ¿qué pasa cuando la x no cambia?)*

<details>
<summary>🔎 Ver soluciones</summary>

1. `d = √((3−(−2))² + (7−3)²) = √(25 + 16) = √41`.
2. `M = (4, 3)`.
3. `d = √(0 + 8²) = 8` (segmento vertical).
</details>

---

## 4.2 Pendiente y formas de la ecuación de la recta

### 👨‍🏫 Enseño
- **Pendiente** entre `(x₁, y₁)` y `(x₂, y₂)`: `m = (y₂ − y₁)/(x₂ − x₁)` = "subida entre avance".
- **Forma pendiente-intersección:** `y = mx + b`, donde `m` = pendiente y `b` = intersección con el eje **y**.
- **Forma punto-pendiente:** `y − y₁ = m(x − x₁)`.
- **Forma estándar:** `Ax + By = C` (con A, B, C enteros).
- Para **graficar** `y = mx + b`: marca el punto `(0, b)` y desde ahí usa la pendiente como "sube `m`, avanza 1" (o sube/avanza con la fracción).

### ✏️ Ejemplo — "Pendiente entre dos puntos"
Halla la pendiente de la recta por `(2, 3)` y `(5, 9)`.

**Solución paso a paso:**
1. `m = (9 − 3)/(5 − 2) = 6/3 = 2`. ✅

### ✏️ Ejemplo — "Graficar con pendiente e intersección"
Grafica `y = 2x − 1`.

**Solución paso a paso:**
1. Intersección con `y`: `b = −1` → punto `(0, −1)`.
2. Pendiente `m = 2 = 2/1` → desde `(0, −1)` sube 2 y avanza 1 → llega a `(1, 1)`.
3. Otro punto: sigue subiendo: `(2, 3)`. Une los puntos → la recta.

### 💪 Practico
1. Pendiente entre `(1, 4)` y `(3, 10)`.
2. Grafica `y = −x + 2` *(pista: pendiente negativa baja al avanzar)*.
3. Pendiente entre `(3, 5)` y `(7, 5)` *(pista: ¿qué tipo de recta es?)*

<details>
<summary>🔎 Ver soluciones</summary>

1. `m = (10 − 4)/(3 − 1) = 6/2 = 3`.
2. Intersección `(0, 2)`, pendiente −1: baja 1 y avanza 1 → `(1, 1)`, `(2, 0)`. Recta descendente.
3. `m = 0/4 = 0` → recta **horizontal** (pendiente 0).
</details>

---

## 4.3 Determinar la ecuación de una recta

### 👨‍🏫 Enseño — según los datos que te den
- **Dos puntos:** calcula `m`, luego usa punto-pendiente con cualquiera de los dos.
- **Pendiente y un punto:** usa directo `y − y₁ = m(x − x₁)`.
- **Intersecciones:** si corta el eje x en `a` y el eje y en `b`, los puntos son `(a, 0)` y `(0, b)`; escribe la recta en forma **interceptos**: `x/a + y/b = 1`.

### ✏️ Ejemplo — "Dos puntos dados"
Halla la ecuación de la recta que pasa por `(1, 2)` y `(3, 8)`.

**Solución paso a paso:**
1. Pendiente: `m = (8 − 2)/(3 − 1) = 6/2 = 3`.
2. Con punto `(1, 2)`: `y − 2 = 3(x − 1)`.
3. Despeja a forma `y = mx + b`: `y − 2 = 3x − 3` → `y = 3x − 1`. ✅

### ✏️ Ejemplo — "Pendiente y punto"
Halla la recta con pendiente `−2` que pasa por `(4, 1)`.

**Solución paso a paso:**
1. `y − 1 = −2(x − 4)`.
2. `y − 1 = −2x + 8` → `y = −2x + 9`. ✅

### 💪 Practico
1. Ecuación de la recta por `(0, 3)` y `(2, 7)`.
2. Ecuación con pendiente `1/2` que pasa por `(−2, 5)`.
3. Ecuación de la recta con intersecciones `x = 4` y `y = 6`. *(pista: puntos `(4,0)` y `(0,6)`)*

<details>
<summary>🔎 Ver soluciones</summary>

1. `m = (7−3)/(2−0) = 2` → `y − 3 = 2(x − 0)` → `y = 2x + 3`.
2. `y − 5 = ½(x + 2)` → `y = ½x + 6`.
3. `m = (6−0)/(0−4) = −1.5` → `y = −1.5x + 6` (o `3x + 2y = 12`).
</details>

---

## 4.4 Paralelas y perpendiculares

### 👨‍🏫 Enseño
- **Paralelas:** misma pendiente `m`. (Solo cambia el `b`.)
- **Perpendiculares:** sus pendientes son **recíprocas negativas**: si `m₁ = a/b`, entonces `m₂ = −b/a`. El producto `m₁·m₂ = −1`.
  - Ejemplo: si `m₁ = 2`, una perpendicular tiene `m₂ = −1/2`.
  - Si `m₁ = −3/4`, perpendicular es `m₂ = 4/3`.

### ✏️ Ejemplo — "Paralela por un punto"
Halla la recta **paralela** a `y = 2x + 5` que pasa por `(1, 3)`.

**Solución paso a paso:**
1. Pendiente de la original: `m = 2`. La paralela usa la misma `m = 2`.
2. Punto-pendiente con `(1, 3)`: `y − 3 = 2(x − 1)`.
3. `y − 3 = 2x − 2` → `y = 2x + 1`. ✅

### ✏️ Ejemplo — "Perpendicular por un punto"
Halla la recta **perpendicular** a `y = 2x + 5` que pasa por `(1, 3)`.

**Solución paso a paso:**
1. Pendiente original `m₁ = 2`. Perpendicular: `m₂ = −1/2` (recíproco negativo).
2. `y − 3 = −½(x − 1)`.
3. `y − 3 = −½x + ½` → `y = −½x + 3.5`. ✅

### 💪 Practico
1. Recta paralela a `y = 3x − 2` que pase por `(0, 4)`.
2. Recta perpendicular a `y = 3x − 2` que pase por `(0, 4)`.
3. ¿Son paralelas, perpendiculares o ninguna? `y = 2x + 1` y `y = −½x + 3`.

<details>
<summary>🔎 Ver soluciones</summary>

1. `y = 3x + 4` (misma m=3).
2. `m₂ = −1/3` → `y = −⅓x + 4`.
3. `2 · (−½) = −1` → **perpendiculares**.
</details>

---

## 4.5 Modelar situaciones del mundo real

### 👨‍🏫 Enseño
**Receta para problemas de aplicación:**
1. **Identifica las variables:** qué representa `x` y qué representa `y`.
2. Encuentra el **punto de partida** (cuando `x = 0`) → es `b`.
3. Encuentra la **razón de cambio** (cuánto cambia `y` por cada unidad de `x`) → es `m`.
4. Escribe `y = mx + b` y responde lo que piden.

### ✏️ Ejemplo — "Situación real"
Un servicio de taxi cobra **Q5** de arranque más **Q2.50** por kilómetro. Escribe la ecuación del costo y calcula el costo de un viaje de **8 km**.

**Solución paso a paso:**
1. Variables: `x` = kilómetros, `y` = costo en quetzales.
2. Arranque (x=0): `b = 5`.
3. Razón de cambio: `m = 2.50` por km.
4. Ecuación: `y = 2.5x + 5`.
5. Para `x = 8`: `y = 2.5·8 + 5 = 20 + 5 = 25`.
6. **Respuesta: Q25.** ✅

### 💪 Practico
1. Una planta mide **12 cm** y crece **3 cm** por semana. (a) Escribe la ecuación; (b) ¿cuánto medirá a las 6 semanas?
2. Una cuenta de celular cobra **Q40** fijos más **Q0.80** por minuto. ¿Cuánto costará una llamada de **25 min**?
3. Una tina con **80 litros** se vacía a razón de **10 litros por minuto**. Escribe la ecuación del agua restante y halla cuándo se vacía.

<details>
<summary>🔎 Ver soluciones</summary>

1. `y = 3x + 12`; a las 6 semanas: `y = 3·6 + 12 = 30 cm`.
2. `y = 0.8x + 40`; `x=25` → `y = 20 + 40 = Q60`.
3. `y = 80 − 10x`; se vacía cuando `y=0` → `80 − 10x = 0` → `x = 8 min`.
</details>

---

# 🟪 BLOQUE 5 — Introducción a las funciones  (20 puntos · 1h)

**Temas del examen:** evaluación de funciones (lineal, cuadrática, valor absoluto, racional, radical) · prueba de la recta vertical · dominio y rango desde pares ordenados · desde gráfica continua · gráfica por trozos.

---

## 5.1 Evaluación de funciones

### 👨‍🏫 Enseño
Una función `f(x)` es una **máquina**: metes un valor de entrada `x` y sale un valor `f(x)`.
Para **evaluar** `f(3)`, **sustituye** cada `x` por `3` y simplifica.

**Cuida el caso de las racionales:** el denominador **no puede ser 0** → si la entrada anula el denominador, `f` no está definida ahí.
**Cuida el caso de las radicales:** dentro de una raíz **par** no puede haber negativo (en los reales).

### ✏️ Ejemplo — "Varios tipos de funciones"
Dadas las funciones, evalúa:
1. `f(x) = 2x + 5` → `f(3) = 2(3) + 5 = 6 + 5 = 11`.
2. `g(x) = x² − 4` → `g(−2) = (−2)² − 4 = 4 − 4 = 0`.
3. `h(x) = |x − 7|` → `h(2) = |2 − 7| = |−5| = 5`.
4. `r(x) = 3/(x − 1)` → `r(4) = 3/(4 − 1) = 3/3 = 1`; y `r(1)` **no existe** (denominador 0).
5. `v(x) = √(x + 6)` → `v(3) = √9 = 3`.

### ✏️ Ejemplo — "Valor absoluto y función cuadrática combinadas"
`f(x) = x² − 2|x|`. Calcula `f(−3)` y `f(0)`.

**Solución paso a paso:**
1. `f(−3) = (−3)² − 2·|−3| = 9 − 2·3 = 9 − 6 = 3`.
2. `f(0) = 0² − 2·|0| = 0 − 0 = 0`. ✅

### 💪 Practico
1. `f(x) = 3x − 7` → halla `f(4)`.
2. `f(x) = x² + 2x` → halla `f(−1)`.
3. `f(x) = |5 − 2x|` → halla `f(6)`.
4. `f(x) = 4/(x + 2)` → halla `f(2)` y di para qué `x` **no existe**.
5. `f(x) = √(x − 9)` → halla `f(25)`.

<details>
<summary>🔎 Ver soluciones</summary>

1. `f(4) = 12 − 7 = 5`.
2. `f(−1) = 1 − 2 = −1`.
3. `f(6) = |5 − 12| = |−7| = 7`.
4. `f(2) = 4/4 = 1`; no existe en `x = −2` (denominador 0).
5. `f(25) = √16 = 4`.
</details>

---

## 5.2 Prueba de la recta vertical

### 👨‍🏫 Enseño
¿Cómo saber si una gráfica es una **función**?
- Traza **líneas verticales imaginarias** sobre la gráfica.
- Si **cualquier** recta vertical toca la gráfica en **más de un punto** → **NO es función** (una entrada `x` tendría dos salidas).
- Si **toda** recta vertical toca como máximo **un punto** → **SÍ es función**.

**Criterio rápido por ecuación:**
- `y = ...` despejada → casi siempre función.
- Si al despejar aparece `±√` (como `x = y²`, o un círculo `x² + y² = r²`) → **no es función**.

### ✏️ Ejemplo — "Aplicar la recta vertical"
¿La parábola horizontal `x = y²` es una función?

**Solución paso a paso:**
1. Piensa en la gráfica: es una parábola abierta hacia la derecha.
2. Para `x = 4`, hay **dos** valores de `y`: `y = 2` y `y = −2`.
3. Una recta vertical en `x = 4` toca la gráfica en 2 puntos → **NO es función**. ✅

### ✏️ Ejemplo — "Identificar funciones"
¿Cuáles son funciones?
- (a) `y = x²` → cada `x` da un solo `y` → **función**.
- (b) `x² + y² = 25` (círculo) → cada `x` interior da dos `y` → **no es función**.
- (c) `y = 2x + 1` → recta (no vertical) → **función**.
- (d) `x = 3` (recta vertical) → TODAS las rectas verticales coinciden → **no es función**.

### 💪 Practico
1. ¿`x = y² − 1` es una función? *(pista: cada x da dos y)*
2. ¿`y = |x|` es una función?
3. ¿Un círculo completo es la gráfica de una función?

<details>
<summary>🔎 Ver soluciones</summary>

1. No (parábola horizontal, falla la recta vertical).
2. Sí (cada x tiene una sola salida).
3. No, falla la recta vertical.
</details>

---

## 5.3 Dominio y rango

### 👨‍🏫 Enseño
- **Dominio:** todos los valores de **entrada** `x` posibles.
- **Rango:** todos los valores de **salida** `y` (o `f(x)`) posibles.

**Reglas rápidas por tipo de función:**
- **Lineal / valor absoluto / polinómica:** dominio = todos los reales `ℝ`.
- **Racional `1/(x−a)`:** dominio = todos los reales **menos** el valor que anula el denominador (`x ≠ a`).
- **Radical par `√(x−a)`:** lo de adentro debe ser `≥ 0` → dominio `x ≥ a`.

### ✏️ Ejemplo — "Dominio desde pares ordenados"
Sea el conjunto de pares `{ (1, 5), (2, 7), (3, 5), (4, 9) }`.
- **Dominio:** primeros valores `= {1, 2, 3, 4}`.
- **Rango:** segundos valores (sin repetir) `= {5, 7, 9}`.
- ¿Es función? Cada `x` aparece una sola vez → **sí**.

### ✏️ Ejemplo — "Dominio de tipos especiales"
Halla el dominio:
1. `f(x) = 1/(x − 5)` → denominador `x − 5 = 0` en `x = 5` → dominio: `ℝ − {5}` (todo menos 5).
2. `f(x) = √(x − 2)` → `x − 2 ≥ 0` → `x ≥ 2` → dominio `[2, ∞)`.

### 💪 Practico
1. Pares `{ (0, 1), (2, 3), (0, 5) }`: ¿es función? ¿cuál es el dominio?
2. Halla el dominio de `f(x) = 5/(x + 7)`.
3. Halla el dominio de `f(x) = √(x − 4)`.

<details>
<summary>🔎 Ver soluciones</summary>

1. No es función: la entrada `0` tiene dos salidas (1 y 5). Dominio `{0, 2}`.
2. `x ≠ −7`.
3. `x ≥ 4` → `[4, ∞)`.
</details>

---

## 5.4 Dominio y rango desde la gráfica (continua y por trozos)

### 👨‍🏫 Enseño
Cuando tienes una **gráfica continua**:
- **Dominio** = todos los valores de `x` que la curva "recorre" (mira el eje x, de izquierda a derecha).
- **Rango** = todos los valores de `y` que alcanza (mira el eje y, de abajo arriba).
- Fíjate en los **extremos**: si un extremo es un punto **relleno** (●) se incluye; si es **hueco** (○), no.

**Función por trozos:** se define con **distintas fórmulas** según el intervalo de `x`. Para evaluar, primero **revisa en qué intervalo** cae tu `x` y usa la fórmula de ese intervalo. Para dominio/rango, junta lo que aporta cada trozo.

### ✏️ Ejemplo — "Evaluar función por trozos"
Sea:
```
f(x) = 2x + 1   si  x < 0
f(x) = x²       si  0 ≤ x ≤ 3
f(x) = 5        si  x > 3
```
Evalúa `f(−1)`, `f(2)`, `f(5)`.

**Solución paso a paso:**
1. `x = −1` está en `x < 0` → usa `2x + 1`: `f(−1) = 2(−1) + 1 = −1`.
2. `x = 2` está en `0 ≤ x ≤ 3` → usa `x²`: `f(2) = 4`.
3. `x = 5` está en `x > 3` → usa `5`: `f(5) = 5`. ✅

### ✏️ Ejemplo — "Dominio y rango de una función continua"
Una gráfica es una curva que va desde `x = −2` hasta `x = 4` (extremos incluidos), y sus valores de `y` van de `−1` a `3` (incluidos).
- **Dominio:** `[−2, 4]`.
- **Rango:** `[−1, 3]`.

### 💪 Practico
1. Con la función por trozos del ejemplo, evalúa `f(0)` y `f(−5)`.
2. Una recta continua de `x = −3` a `x = 3` sube desde `y = 2` hasta `y = 8`. ¿Dominio y rango?
3. Una parábola abre hacia arriba con vértice en `(0, −4)` y se extiende en toda la recta. ¿Cuál es el rango?

<details>
<summary>🔎 Ver soluciones</summary>

1. `f(0)` cae en `0 ≤ x ≤ 3` → `0² = 0`. `f(−5)` cae en `x < 0` → `2(−5)+1 = −9`.
2. Dominio `[−3, 3]`, rango `[2, 8]`.
3. Como abre hacia arriba desde el vértice, rango `[−4, ∞)`.
</details>

---

# 🧠 Cierre: Repaso exprés + examen simulado (30 min)

## 📋 Checklist de fórmulas (revisa que las recuerdes de memoria)

> Versión completa en tablas: [`IV Matemática 2026 - Tablas y fórmulas.md`](IV Matemática 2026 - Tablas y fórmulas.md)
- Ángulos: complementarios `90°`, suplementarios `180°`, triángulo `180°`.
- Pitágoras: `a² + b² = c²`.
- Trigonometría: SOH-CAH-TOA; `tan 45° = 1`, `sen 30° = cos 60° = 0.5`.
- Factorización: `a²−b²=(a+b)(a−b)`; `a³±b³=(a±b)(...)`; TCP `(a±b)²`.
- Desigualdad: invertir sentido al multiplicar/dividir por negativo.
- Valor absoluto: `|X|<a → −a<X<a`; `|X|>a → X<−a o X>a`.
- Recta: `m=(y₂−y₁)/(x₂−x₁)`; `y=mx+b`; perpendiculares → `m₁·m₂ = −1`.
- Distancia y punto medio: `d=√(Δx²+Δy²)`, `M=(promedio de x, promedio de y)`.
- Dominio: denom ≠ 0 en racionales; radicando ≥ 0 en radicales pares.

## 🕐 Simula el examen (2 horas, como el real)
1. Imprime (o copia) la hoja de puntos del PDF original.
2. Cronométrate **120 minutos** para los **100 puntos**.
3. Resuelve **en silencio y a mano**, sin ayuda.
4. Al terminar, **autoevalúa** con las soluciones de esta guía y las de la herramienta interactiva.

> 💪 **Regla de la jornada:** si en el simulacro fallas un tema, esa es tu **señal** de qué repasar mañana. No lo ignores: vuelve al bloque correspondiente y repite solo los "Practico" que fallaste.

---

## ✅ Resumen de puntajes por bloque
| Bloque | Punteo | Estatus de tu práctica |
|--------|--------|------------------------|
| Geometría y Trigonometría | /20 | ☐ |
| Factorización | /10 | ☐ |
| Desigualdades | /25 | ☐ |
| Ecuación de la recta | /25 | ☐ |
| Introducción a las funciones | /20 | ☐ |
| **TOTAL** | **/100** | ☐ |

¡Éxito en tu examen de admisión! 🎓🚀
