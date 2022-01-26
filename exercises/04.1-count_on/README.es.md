# `04.1` Count on

Como has visto en el ejercicio anterior tu lista puede ser un a mezcla de `tipos de datos` que vamos a dividir y conquistar.

¿Serías tan amable de añadir todos los elementos con *data-type* (tipo de dato) `dict` y `list` de la lista `my_list` en una nueva lista llamada `new_list`?

## 📝 Instrucciones:

1. Itera la lista dada (`my_list`).

2. Mete los tipos de datos `dict` y `list` encontrados en una nueva lista llamada `new_list`.

3. Imprime la variable `new_list`.

## 💡 Pista:

+ Recuerda que puedes saber el tipo de dato de una variable o valor con la función `type()`

+ Para más información sobre la función `type()`: https://www.w3schools.com/python/ref_func_type.asp

Así es como puedes imprimir TODOS los elementos:

```py
my_list = [42, true, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

for x in my_list:
    print(x)
```

## Resultado esperado:

```py
[[2, 1], {'name': 'juan'}]
```
