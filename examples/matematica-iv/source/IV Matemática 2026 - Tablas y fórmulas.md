# 📐 Tablas de conversión y fórmulas
### Hoja de repaso · Matemática IV Bachillerato · Examen de Admisión

> **Para qué sirve:** memorizar lo que en el examen no te van a dar.
> **Fuente:** [`IV Matemática 2026 - Guía de estudio intensiva.md`](IV Matemática 2026 - Guía de estudio intensiva.md)
> **Uso:** imprímela o tenla abierta al lado mientras resuelves. El día del examen debe estar **en tu cabeza**.
> **Ficha para imprimir y entregar:**
> - Kit web (práctica + fórmulas + exprés): [`index.html`](../html/index.html)
> - PDF listo: [`IV Matemática 2026 - Tablas y fórmulas.pdf`](../pdf/IV Matemática 2026 - Tablas y fórmulas.pdf)
> - **Hoja exprés (2 páginas, para el cuaderno):**
>   PDF: [`IV Matemática 2026 - Hoja exprés.pdf`](../pdf/IV Matemática 2026 - Hoja exprés.pdf)

---

## Índice rápido

| Bloque | Qué memorizar aquí |
|--------|-------------------|
| [1. Geometría y trigonometría](#-bloque-1--geometría-y-trigonometría) | Ángulos, Pitágoras, SOH-CAH-TOA, valores exactos |
| [2. Factorización](#-bloque-2--factorización) | Casos, cuadrados/cubos perfectos, signos |
| [3. Desigualdades](#-bloque-3--desigualdades) | Intervalos, valor absoluto, tabla de signos |
| [4. Recta y coordenadas](#-bloque-4--ecuación-de-la-recta) | Distancia, pendiente, formas, paralelas |
| [5. Funciones](#-bloque-5--funciones) | Evaluación, dominio, recta vertical |

---

# 🟦 BLOQUE 1 — Geometría y trigonometría

## 1.1 Conversión de ángulos (relaciones)

| Relación | Conversión | Recuerda |
|----------|------------|----------|
| Complementarios | `β = 90° − α` | juntos forman esquina |
| Suplementarios | `β = 180° − α` | juntos forman línea |
| Opuestos por el vértice | `β = α` | **iguales** |
| Adyacentes (sobre una recta) | `β = 180° − α` | suplementarios |
| Tercer ángulo de un triángulo | `γ = 180° − α − β` | siempre suman 180° |
| Base de isósceles (vértice `α`) | cada base = `(180° − α) / 2` | los de la base son iguales |

### Paralelas cortadas por una transversal

Si un ángulo mide `α`, los 8 ángulos se convierten así:

| Tipo | Valor | Cómo reconocerlo |
|------|-------|------------------|
| Correspondientes | `α` (iguales) | misma “esquina” en cada cruce |
| Alternos internos | `α` (iguales) | en Z, entre las paralelas |
| Alternos externos | `α` (iguales) | en Z, fuera de las paralelas |
| Internos del mismo lado | `180° − α` | juntos “llenan” el espacio entre paralelas |
| Opuestos por el vértice | `α` | cruzados en el mismo vértice |
| Adyacentes | `180° − α` | juntos forman línea |

> **Atajo:** en la figura solo hay **dos medidas**: `α` y `180° − α`, intercaladas.

---

## 1.2 Teorema de Pitágoras

| Qué buscas | Fórmula | Conversión |
|------------|---------|------------|
| Hipotenusa `c` | `c = √(a² + b²)` | suma de cuadrados, luego raíz |
| Cateto `a` | `a = √(c² − b²)` | resta de cuadrados, luego raíz |
| Verificar rectángulo | `a² + b² ≟ c²` | si coincide, hay 90° |

> 🛑 La hipotenusa **siempre** va sola: `c² = a² + b²`. Nunca la pongas como cateto.

### Ternas pitagóricas (conviértelas de memoria)

Si reconoces la terna, **no calculas raíz**.

| Cateto | Cateto | Hipotenusa | Múltiplos útiles |
|--------|--------|------------|------------------|
| 3 | 4 | 5 | 6-8-10 · 9-12-15 · 12-16-20 |
| 5 | 12 | 13 | 10-24-26 |
| 6 | 8 | 10 | es 2×(3-4-5) |
| 7 | 24 | 25 | — |
| 8 | 15 | 17 | — |
| 9 | 12 | 15 | es 3×(3-4-5) |
| 9 | 40 | 41 | — |
| 20 | 21 | 29 | — |

### Triángulos especiales (conversión de lados)

**45°-45°-90°** (isósceles rectángulo)

| Lado | En términos del cateto `a` | En términos de la hipotenusa `c` |
|------|----------------------------|----------------------------------|
| Catetos | `a` y `a` | `c / √2` = `(c√2)/2` |
| Hipotenusa | `a√2` | `c` |

**30°-60°-90°**

| Lado | Relación | Si el corto (opuesto a 30°) es `a` |
|------|----------|-------------------------------------|
| Opuesto a 30° | 1 parte | `a` |
| Opuesto a 60° | `√3` partes | `a√3` |
| Hipotenusa (opuesto a 90°) | 2 partes | `2a` |

---

## 1.3 Razones trigonométricas — SOH-CAH-TOA

| Razón | Fórmula | Cuándo usarla |
|-------|---------|---------------|
| `sen θ` | opuesto / hipotenusa | tienes op e hip |
| `cos θ` | adyacente / hipotenusa | tienes ady e hip |
| `tan θ` | opuesto / adyacente | tienes op y ady |

### Despejes (conversión: razón → lado)

| Quieres | Tienes | Fórmula |
|---------|--------|---------|
| Opuesto | hip y `θ` | `op = hip · sen θ` |
| Adyacente | hip y `θ` | `ady = hip · cos θ` |
| Opuesto | ady y `θ` | `op = ady · tan θ` |
| Adyacente | op y `θ` | `ady = op / tan θ` |
| Hipotenusa | op y `θ` | `hip = op / sen θ` |
| Hipotenusa | ady y `θ` | `hip = ady / cos θ` |
| El ángulo `θ` | dos lados | `θ = sen⁻¹(...)`, `cos⁻¹(...)` o `tan⁻¹(...)` |

### Identidad puente (si ya tienes sen y cos)

| Identidad | Fórmula |
|-----------|---------|
| Tangente | `tan θ = sen θ / cos θ` |
| Pitágoras trigonométrico | `sen²θ + cos²θ = 1` |

### Tabla de valores exactos (¡de memoria!)

| `θ` | `sen θ` | `cos θ` | `tan θ` | Decimal útil |
|-----|---------|---------|---------|--------------|
| 0° | `0` | `1` | `0` | 0 · 1 · 0 |
| 30° | `1/2` | `√3/2` | `1/√3` = `√3/3` | 0.5 · 0.866 · 0.577 |
| 45° | `√2/2` | `√2/2` | `1` | 0.707 · 0.707 · 1 |
| 60° | `√3/2` | `1/2` | `√3` | 0.866 · 0.5 · 1.732 |
| 90° | `1` | `0` | no existe | 1 · 0 · — |

> 💡 **Los tres que más ahorran tiempo:** `sen 30° = 0.5` · `cos 60° = 0.5` · `tan 45° = 1`.

**Truco de los senos (0° → 90°):** `√0/2`, `√1/2`, `√2/2`, `√3/2`, `√4/2`.
Los cosenos van **al revés**. La tangente es seno ÷ coseno.

### Ángulo de elevación vs. depresión

| Tipo | Dónde está el ángulo | Conversión práctica |
|------|----------------------|---------------------|
| Elevación | desde el suelo hacia arriba | `tan θ = altura / distancia` |
| Depresión | desde lo alto hacia abajo | el ángulo de depresión = el de elevación interno (alternos internos) |

---

# 🟩 BLOQUE 2 — Factorización

## 2.1 Tabla de casos (qué fórmula aplicar)

| Ves esto | Caso | Fórmula |
|----------|------|---------|
| Algo se repite en todos los términos | Factor común | `ax + ay = a(x + y)` |
| 4 términos | Agrupación | `ax+ay+bx+by = (a+b)(x+y)` |
| Resta de dos cuadrados | Diferencia de cuadrados | `a² − b² = (a+b)(a−b)` |
| Suma de dos cuadrados | **No factoriza** (reales) | deja `a² + b²` |
| Suma de cubos | Suma de cubos | `a³ + b³ = (a+b)(a² − ab + b²)` |
| Resta de cubos | Diferencia de cubos | `a³ − b³ = (a−b)(a² + ab + b²)` |
| Extremos cuadrados y medio = doble | TCP | `a² ± 2ab + b² = (a ± b)²` |
| `x² + bx + c` | Trinomio simple | `(x+p)(x+q)` con `p+q=b`, `p·q=c` |
| `ax² + bx + c` (`a ≠ 1`) | Método del ac | parte el medio y agrupa |

> **Orden de ataque:** 1) factor común → 2) cuenta términos → 3) aplica el caso → 4) ¿se puede seguir? (completamente).

## 2.2 Signos del trinomio `x² + bx + c`

| Signo de `c` | Signo de `b` | Conversión a factores |
|--------------|--------------|------------------------|
| `+` | `+` | ambos positivos: `(x+p)(x+q)` |
| `+` | `−` | ambos negativos: `(x−p)(x−q)` |
| `−` | `+` | el de mayor valor absoluto es `+` |
| `−` | `−` | el de mayor valor absoluto es `−` |

## 2.3 Cubos: regla de signos SOAP

**S**ame · **O**pposite · **A**lways **P**ositive

| Caso | 1er paréntesis | Término medio del 2º | Último del 2º |
|------|----------------|----------------------|---------------|
| `a³ + b³` | `(a + b)` | `−ab` (contrario) | `+ b²` siempre |
| `a³ − b³` | `(a − b)` | `+ab` (contrario) | `+ b²` siempre |

## 2.4 Cuadrados perfectos (conversión n → n²)

| n | n² | n | n² | n | n² |
|---|----|---|----|---|----|
| 1 | 1 | 8 | 64 | 15 | 225 |
| 2 | 4 | 9 | 81 | 16 | 256 |
| 3 | 9 | 10 | 100 | 17 | 289 |
| 4 | 16 | 11 | 121 | 18 | 324 |
| 5 | 25 | 12 | 144 | 19 | 361 |
| 6 | 36 | 13 | 169 | 20 | 400 |
| 7 | 49 | 14 | 196 | 25 | 625 |

Útiles para TCP y diferencia de cuadrados: `1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225`.

## 2.5 Cubos perfectos (conversión n → n³)

| n | n³ | Reconócelo en |
|---|----|----------------|
| 1 | 1 | `1`, `x³` |
| 2 | 8 | `8`, `8x³ = (2x)³` |
| 3 | 27 | `27`, `27x³ = (3x)³` |
| 4 | 64 | `64`, `64x³ = (4x)³` |
| 5 | 125 | `125`, `125x³ = (5x)³` |
| 6 | 216 | `216` |
| 7 | 343 | `343` |
| 8 | 512 | `512` |
| 9 | 729 | `729` |
| 10 | 1000 | `1000` |

## 2.6 Método del ac (pasos en una línea)

```
ax² + bx + c
   → calcula a·c
   → busca p, q con p·q = a·c  y  p+q = b
   → reescribe ax² + px + qx + c
   → agrupa y saca factor común
```

---

# 🟨 BLOQUE 3 — Desigualdades

## 3.1 Conversión entre notaciones

| Desigualdad | Intervalo | Conjunto | Gráfica |
|-------------|-----------|----------|---------|
| `x > a` | `(a, ∞)` | `{x ∈ ℝ \| x > a}` | ○ hueco, flecha a la **derecha** |
| `x ≥ a` | `[a, ∞)` | `{x ∈ ℝ \| x ≥ a}` | ● relleno, flecha a la **derecha** |
| `x < a` | `(−∞, a)` | `{x ∈ ℝ \| x < a}` | ○ hueco, flecha a la **izquierda** |
| `x ≤ a` | `(−∞, a]` | `{x ∈ ℝ \| x ≤ a}` | ● relleno, flecha a la **izquierda** |
| `a < x < b` | `(a, b)` | `{x ∈ ℝ \| a < x < b}` | ○ en `a` y `b`, segmento |
| `a ≤ x ≤ b` | `[a, b]` | `{x ∈ ℝ \| a ≤ x ≤ b}` | ● en `a` y `b`, segmento |
| `a < x ≤ b` | `(a, b]` | mixto | ○ en `a`, ● en `b` |
| `a ≤ x < b` | `[a, b)` | mixto | ● en `a`, ○ en `b` |
| `x < a` **o** `x > b` | `(−∞, a) ∪ (b, ∞)` | unión | dos rayos |
| `x ≤ a` **o** `x ≥ b` | `(−∞, a] ∪ [b, ∞)` | unión | dos rayos con relleno |
| todo ℝ | `(−∞, ∞)` = `ℝ` | todos | toda la recta |
| vacío | `∅` | ninguno | nada |

### Paréntesis: conversión rápida

| Símbolo | Incluye el extremo | Equivale a |
|---------|-------------------|------------|
| `(` `)` | **no** | `<` o `>` |
| `[` `]` | **sí** | `≤` o `≥` |
| `∞` / `−∞` | nunca se incluye | siempre `)` o `(` |

### Unión e intersección

| Símbolo | Significa | En la recta |
|---------|-----------|-------------|
| `∪` unión | “o”: se queda con **ambos** | pinta las dos zonas |
| `∩` intersección | “y”: se queda con el **traslape** | pinta solo lo común |

---

## 3.2 Regla de oro de las desigualdades lineales

| Operación | ¿Cambia el sentido? |
|-----------|---------------------|
| Sumar o restar (cualquier número) | no |
| Multiplicar o dividir por **positivo** | no |
| Multiplicar o dividir por **negativo** | **sí: invierte** `<` ↔ `>` y `≤` ↔ `≥` |
| Cambiar de lado un término | no (es sumar el opuesto) |

Ejemplo de conversión: `−x > 5` → multiplicar por `−1` → `x < −5`.

---

## 3.3 Valor absoluto — conversión a desigualdades

El valor absoluto `|X|` = distancia de `X` al 0. Siempre `|X| ≥ 0`.

| Ves | Se convierte en | Intervalo |
|-----|-----------------|-----------|
| `|X| < a`  (`a > 0`) | `−a < X < a` | `(−a, a)` |
| `|X| ≤ a` | `−a ≤ X ≤ a` | `[−a, a]` |
| `|X| > a` | `X < −a` **o** `X > a` | `(−∞, −a) ∪ (a, ∞)` |
| `|X| ≥ a` | `X ≤ −a` **o** `X ≥ a` | `(−∞, −a] ∪ [a, ∞)` |
| `|X| = a` | `X = −a` **o** `X = a` | dos puntos |
| `|X| < 0` | imposible | `∅` |
| `|X| ≤ 0` | solo `X = 0` | `{0}` |
| `|X| > 0` | `X ≠ 0` | `(−∞, 0) ∪ (0, ∞)` |

**Frase:** menor que → **entre**; mayor que → **afuera (unión)**.

Si el interior no es solo `x`, primero deja `|expresión|` y **después** despeja `x` en los tres (o dos) lados.

---

## 3.4 Polinómicas y racionales — receta

```
1. Pasa todo a un lado  →  f(x) > 0  (o <, ≥, ≤)
2. Factoriza  (bloque 2)
3. Marca ceros del numerador y del denominador
4. Divide la recta en intervalos
5. Prueba un número en cada intervalo (tabla de signos)
6. Elige los intervalos que cumplen
```

### Qué incluir / qué excluir

| Tipo de punto | Si la desigualdad es `>` o `<` | Si es `≥` o `≤` |
|---------------|--------------------------------|-----------------|
| Raíz del **numerador** (cero de `f`) | **excluir** ○ | **incluir** ● |
| Raíz del **denominador** (no existe) | **excluir siempre** ○ | **excluir siempre** ○ |

> 💡 El signo de `A/B` es el mismo que el de `A·B`. Trata la racional como producto, pero **nunca** incluyas el cero del denominador.

### Patrón de signos de un producto `(x−r₁)(x−r₂)…` (raíces simples)

Al cruzar una raíz de multiplicidad **impar**, el signo **cambia**.
Al cruzar una de multiplicidad **par**, el signo **se queda**.

---

# 🟧 BLOQUE 4 — Ecuación de la recta

## 4.1 Puntos: distancia y punto medio

Dados `A(x₁, y₁)` y `B(x₂, y₂)`:

| Qué | Fórmula | Lectura |
|-----|---------|---------|
| Distancia | `d = √[(x₂ − x₁)² + (y₂ − y₁)²]` | Pitágoras en el plano |
| Punto medio | `M = ( (x₁+x₂)/2 , (y₁+y₂)/2 )` | promedio de x, promedio de y |
| Pendiente | `m = (y₂ − y₁) / (x₂ − x₁)` | subida / avance |

Casos especiales de distancia:

| Situación | Conversión |
|-----------|------------|
| Misma `x` (vertical) | `d = \|y₂ − y₁\|` |
| Misma `y` (horizontal) | `d = \|x₂ − x₁\|` |

---

## 4.2 Conversión entre formas de la recta

| Forma | Ecuación | Qué se lee de golpe |
|-------|----------|---------------------|
| Pendiente-intersección | `y = mx + b` | `m` = pendiente, `b` = corta el eje **y** en `(0, b)` |
| Punto-pendiente | `y − y₁ = m(x − x₁)` | pasa por `(x₁, y₁)` con pendiente `m` |
| Estándar | `Ax + By = C` | A, B, C enteros (a veces `By` negativo) |
| Interceptos | `x/a + y/b = 1` | corta x en `(a, 0)` y y en `(0, b)` |
| Horizontal | `y = k` | `m = 0` |
| Vertical | `x = h` | `m` no existe (no es función) |

### Recetas de conversión

**De dos puntos → `y = mx + b`**
1. `m = (y₂ − y₁)/(x₂ − x₁)`
2. `y − y₁ = m(x − x₁)`
3. despeja `y`

**De `y = mx + b` → estándar `Ax + By = C`**
1. pasa `mx` al otro lado: `−mx + y = b`
2. si `m` es fracción, multiplica para enteros
3. (opcional) deja `A > 0`

**De interceptos `a` y `b` → pendiente**
- puntos `(a, 0)` y `(0, b)` → `m = (b − 0)/(0 − a) = −b/a`

### Cómo graficar `y = mx + b`

1. Marca `(0, b)`.
2. Escribe `m` como fracción `sube/avanza`.
3. Desde `(0, b)` aplica esa fracción (si `m` es negativa, **baja**).

| Pendiente | Significado gráfico |
|-----------|---------------------|
| `m > 0` | sube hacia la derecha |
| `m < 0` | baja hacia la derecha |
| `m = 0` | horizontal |
| `m` indefinida | vertical |

---

## 4.3 Paralelas y perpendiculares (conversión de pendientes)

| Relación | Conversión de `m` | Prueba |
|----------|-------------------|--------|
| Paralelas | `m₂ = m₁` (igual) | solo cambia `b` |
| Perpendiculares | `m₂ = −1/m₁` (recíproco negativo) | `m₁ · m₂ = −1` |
| Horizontal ⊥ vertical | `m = 0` ⊥ `x = h` | — |

**Tabla de recíprocos negativos (atajo de examen):**

| Si `m₁` es… | entonces `m₂` perpendicular es… |
|-------------|----------------------------------|
| `2` | `−1/2` |
| `−2` | `1/2` |
| `1/3` | `−3` |
| `−3/4` | `4/3` |
| `4` | `−1/4` |
| `1` | `−1` |
| `−1` | `1` |

---

## 4.4 Modelar una situación real → `y = mx + b`

| Dato del problema | Se convierte en |
|-------------------|-----------------|
| Valor inicial / arranque / cuando `x = 0` | `b` |
| “por cada…”, “cada semana”, “por km” | `m` (razón de cambio) |
| “se vacía / disminuye” | `m` **negativa** |
| Preguntan “¿cuánto cuando x = …?” | sustituye en `y = mx + b` |
| Preguntan “¿cuándo llega a y = …?” | despeja `x` |

---

# 🟪 BLOQUE 5 — Funciones

## 5.1 Evaluación: sustituir y simplificar

| Tipo | Aspecto | Cuidado al evaluar |
|------|---------|---------------------|
| Lineal `f(x) = mx + b` | sustituye | ninguno |
| Cuadrática `f(x) = x² + …` | `(−n)² = +n²` | el signo queda dentro del cuadrado |
| Valor absoluto `f(x) = \|…\|` | resultado ≥ 0 | primero opera adentro, luego quita el signo |
| Racional `f(x) = n/d` | `d ≠ 0` | si el denominador da 0 → **no existe** |
| Radical par `f(x) = √(…)` | interior ≥ 0 | si el interior es negativo → **no existe** (reales) |

---

## 5.2 Prueba de la recta vertical

| Resultado | Significa | Ejemplos |
|-----------|-----------|----------|
| Toda vertical toca **a lo más 1** punto | **sí** es función | `y = x²`, `y = \|x\|`, `y = mx+b` (no vertical) |
| Alguna vertical toca **2 o más** puntos | **no** es función | círculo, `x = y²`, `x = 3` |

| Ecuación | ¿Función? | Por qué |
|----------|-----------|---------|
| `y = …` (despejada, un solo valor) | sí | cada x da un y |
| `x = k` (vertical) | no | infinitos y para un x |
| `x = y²` / `x = y² − 1` | no | `±` |
| `x² + y² = r²` (círculo) | no | dos y por x interior |
| `y = \|x\|` | sí | una salida |
| `y = ±√x` escrito con los dos signos | no | dos salidas |

---

## 5.3 Dominio — conversión por tipo

| Tipo de función | Dominio | Cómo se escribe |
|-----------------|---------|-----------------|
| Lineal, cuadrática, valor absoluto, polinomio | todos los reales | `ℝ` o `(−∞, ∞)` |
| Racional `p(x)/q(x)` | todo **menos** donde `q(x) = 0` | `x ≠ a` o `ℝ − {a}` |
| Radical **par** `√g(x)` | `g(x) ≥ 0` | intervalo, p. ej. `[a, ∞)` |
| Radical impar `∛g(x)` | todos los reales | `ℝ` |
| Pares ordenados `{(x, y), …}` | los **primeros** de cada par | conjunto `{…}` |

**Rango** = valores de **salida** `y` posibles.

| Desde… | Dominio | Rango |
|--------|---------|-------|
| Pares ordenados | primeras componentes (sin repetir da igual) | segundas componentes **sin repetir** |
| Gráfica continua | x que recorre la curva (izq → der) | y que alcanza (abajo → arriba) |
| Extremo ● relleno | **incluye** ese valor | igual |
| Extremo ○ hueco | **no incluye** | igual |
| Parábola `y = x²` (abre arriba, vértice `(h, k)`) | `ℝ` | `[k, ∞)` |
| Parábola que abre abajo, vértice `(h, k)` | `ℝ` | `(−∞, k]` |
| `y = \|x\|` | `ℝ` | `[0, ∞)` |
| `y = √(x − a)` | `[a, ∞)` | `[0, ∞)` |

---

## 5.4 Función por trozos

```
f(x) = fórmula₁    si  x está en intervalo₁
       fórmula₂    si  x está en intervalo₂
       …
```

| Tarea | Qué hacer |
|-------|-----------|
| Evaluar `f(c)` | mira **en qué intervalo cae `c`** y usa **solo** esa fórmula |
| Si `c` está en un extremo | respeta `≤` / `<` (un extremo pertenece a un solo trozo) |
| Dominio | **unión** de los intervalos donde está definida |
| Rango | junta las salidas que produce cada trozo (ojo a huecos) |

---

# 🧠 Hoja exprés (una página mental)

Cópiala en una ficha o recítala en voz alta:

| # | Fórmula / conversión |
|---|----------------------|
| 1 | Complementarios `90°` · suplementarios `180°` · triángulo `180°` |
| 2 | Paralelas: correspondientes = · alternos = · mismo lado `180°` |
| 3 | `a² + b² = c²` · ternas 3-4-5, 5-12-13, 8-15-17 |
| 4 | SOH-CAH-TOA · `sen 30° = 1/2` · `cos 60° = 1/2` · `tan 45° = 1` |
| 5 | 45-45-90: `a, a, a√2` · 30-60-90: `a, a√3, 2a` |
| 6 | `a² − b² = (a+b)(a−b)` · `a² + b²` no factoriza |
| 7 | `a³ + b³ = (a+b)(a² − ab + b²)` · `a³ − b³ = (a−b)(a² + ab + b²)` |
| 8 | TCP: `a² ± 2ab + b² = (a ± b)²` |
| 9 | `x² + bx + c = (x+p)(x+q)` con `p+q=b`, `p·q=c` |
| 10 | `>` `(`  ·  `≥` `[`  ·  `∞` nunca cerrado |
| 11 | × o ÷ por negativo → **invierte** la desigualdad |
| 12 | `\|X\| < a` → entre · `\|X\| > a` → afuera (unión) |
| 13 | Cero del denominador: **nunca** se incluye |
| 14 | `d = √(Δx² + Δy²)` · `M = (promedio x, promedio y)` |
| 15 | `m = Δy/Δx` · `y = mx + b` · punto-pendiente `y − y₁ = m(x − x₁)` |
| 16 | Paralelas: misma `m` · perpendiculares: `m₂ = −1/m₁` |
| 17 | Racional: `x ≠` lo que anula el denom · radical par: interior `≥ 0` |
| 18 | Recta vertical: si toca 2 puntos → **no** es función |

---

## Cómo usarla en la jornada

1. **Antes de cada bloque** de la guía: lee solo las tablas de ese bloque (2–3 min).
2. **Al fallar un “Practico”:** vuelve a **esta hoja**, no al ejemplo largo; identifica qué fila de conversión te faltó.
3. **En el repaso de 30 min:** tápate la columna del medio y recita la conversión.

Kit web (práctica, fórmulas y recitar):
[`index.html`](../html/index.html)

Ficha de 2 páginas para pegar en el cuaderno:
PDF: [`IV Matemática 2026 - Hoja exprés.pdf`](../pdf/IV Matemática 2026 - Hoja exprés.pdf)
