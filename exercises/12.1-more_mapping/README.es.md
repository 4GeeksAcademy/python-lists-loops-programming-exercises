# `12.1` Más mapeo

La función `map()` de una lista, llama a una función por cada valor en la lista y, luego, entrega una nueva lista con los valores modificados.

```py
#incrementByOne
def values_list(number) {
  return number + 1
}

my_list = [1, 2, 3, 4]
result = map(values_list, my_list)  #returns [2, 3, 4, 5]
```

## 📝 Instrucciones:

1. Crear una función llamada `increment_by_one` que multiplicará cada número por 3.

2. Usa la función `map()` de la lista para ejecutar la función `increment_by_one` en cada valor en la lista.

3. Almacena la nueva lista en una nueva llamada `new_list` e imprime (`print()`) los nuevos valores.

## 💡 Pista:

+ La función cogerá un parámetro con el elemento original y lo transformará e insertará en una nueva lista.

+ Recuerda que tu función debe devolver cada nuevo elemento para almacenarlo en la nueva lista


