# `08.2` Divide and conquer

## 📝 Instrucciones:

1. Crea una función llamada `sort_odd_even` que espere una lista de números enteros.

2. Itera la lista y separa los números *pares* e *impares*.

3. Crea una lista vacía llamada `sorted_numbers` y empieza a insertar los números *impares*.

4. Si el número es par, colócalo en una lista llamada `even`.

5. Luego concatena la lista `even` en `sorted_numbers`. Recuerda que los números *impares* van primero y luego debes añadirle la lista `even` después.

## 💡 Pista:

+ Crea variables vacías cuando necesites almacenar información.

+ Lee sobre el método `extend()`: https://www.w3schools.com/python/ref_list_extend.asp

## 💻 Resultado esperado:

Debe quedar todo dentro de una sola lista, no debe haber listas anidadas.

```py
sort_odd_even([1, 2, 33, 10, 20, 4])

[1, 33, 2, 10, 20, 4] # <-- Si
[[1,33], [2,10,20,4]] # <-- No
```



