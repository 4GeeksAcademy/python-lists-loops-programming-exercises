# `01.5` Loop from 1 to 17

Para iterar sobre un número específico de veces, podemos usar

```py

range(<start>,<end>)
```

En Python, `range(x,y)` devuelve una secuencia de números empezando en x e incrementando en 1 cada vez hasta alcanzar y, sin incluirlo.

Por ejemplo:

```py

for x in range(0,5):
  print(x)
```

Salida:

```py
0
1
2
3
4
```

Nota que el número final especificado en `range()`, 5 en este ejemplo, nunca se incluye; por lo tanto, 4 es el último número en la salida.

Podemos incorporar parámetros adicionales para especificar con más detalle (ahora sería un buen momento para buscar en Google o, al menos, revisar la sección de pistas ;) ).

## 📝Instrucciones:
1. Cuenta del 1 al 17 con un bucle e imprime cada número en la consola.

## 💡 Pista: 
- Así haces un bucle: [https://www.freecodecamp.org/espanol/news/bucle-for-en-python-ejemplo-de-for-i-en-range/](https://www.freecodecamp.org/espanol/news/bucle-for-en-python-ejemplo-de-for-i-en-range/)
## Resultado esperado:

```py
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
```