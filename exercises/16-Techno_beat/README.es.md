# `16` Latidos de tecno

Estás trabajando con un DJ que necesita un programa que pueda crear latidos para sus canciones.

## 📝 Instrucciones:

1. Crea una función `lyrics_generator` que reciba una lista. La lista que se le pase a la función será algo como esto:
```py
    [0,0,1,1,0,0,0]
```

2. Para cada `Cero` añadirás al string `Boom`.

3. Para cada `Uno` añadirás al string `Drop the base`.

## Restricciones:

Si encuentras un uno (`1)` tres veces seguidas, debes añadir al string también `!!!Break the base!!!`


## Resultado esperado:

```py
Valor devuelto por la función:

Unstring compuesto por `Boom` o `Drop` the base o `!!!Break the base!!!`

Salida esperada:

Boom Boom Drop the base Drop the base Boom Boom Boom
Boom Boom Drop the base Drop the base Drop the base !!!Break the base!!! Boom Boom Boom
Boom Boom Boom
Drop the base Boom Drop the base
Drop the base Drop the base Drop the base !!!Break the base!!!
```


## 💡 Pista:

- Recuerda usar variables auxiliares.

- Declara una variable para almacenar.

- Declara una variable para contar y sumar.
