# `12.1` More mapping

El método `map()` llama a una función por cada valor en la lista y, luego, devuelve una nueva lista con los valores modificados.

```py
def increment_by_one(number):
    return number + 1

my_list = [1, 2, 3, 4]
result = map(increment_by_one, my_list)  # returns [2, 3, 4, 5]
```

## 📝 Instrucciones:

1. Crear una función llamada `multiply_by_three` que multiplicará cada número por 3.

2. Usa la función `map()` de la lista para ejecutar la función `multiply_by_three` en cada valor de la lista.

3. Almacena la nueva lista en una variable llamada `new_list` e imprime los nuevos valores.

## 💡 Pistas:

+ La función `map()` aplicará la función especificada por parámetro a cada elemento de tu lista.

+ Recuerda almacenar tu resultado en la nueva lista (`new_list`).


