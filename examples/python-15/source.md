# Python para principiantes (15 años)

Curso corto para escribir tus primeros programas. Sin librerías raras: solo lo que trae Python.

## 1. Variables y tipos (25 pts)

Una variable guarda un valor con un nombre.

```python
nombre = "Ana"
edad = 15
altura = 1.62
activo = True
```

- `str` = texto (comillas)
- `int` = entero
- `float` = decimal
- `bool` = True o False

`type(x)` dice el tipo. `print(x)` lo muestra.

## 2. Condicionales y bucles (25 pts)

```python
if edad >= 18:
    print("adulto")
else:
    print("menor")
```

`for n in range(5):` recorre 0, 1, 2, 3, 4.  
`while` se repite mientras la condición sea verdadera. Cuidado con los bucles infinitos.

## 3. Listas (20 pts)

```python
notas = [80, 90, 70]
notas.append(95)
print(len(notas))   # 4
print(notas[0])     # 80  (el primero)
print(notas[-1])    # 95  (el último)
```

Los índices empiezan en **0**.

## 4. Funciones (20 pts)

```python
def area_rect(base, altura):
    return base * altura

print(area_rect(3, 4))  # 12
```

`return` entrega el resultado. Sin `return`, la función devuelve `None`.

## 5. Errores comunes (10 pts)

- Olvidar `:` al final de `if` / `for` / `def`
- Mezclar `=` (asignar) con `==` (comparar)
- Pedir `lista[4]` cuando solo hay 4 elementos (el último es `[3]`)
- Dividir entre 0
