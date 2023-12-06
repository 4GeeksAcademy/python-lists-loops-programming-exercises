# `12.4` Map a list of dictionaries

El escenario más común para la función de mapeo es simplificar listas dadas, por ejemplo:

El actual algoritmo crea una lista con solo los nombres de personas (`name_list`) y los imprime en la consola.

## 📝 Instrucciones:

1. En este momento la función está imprimiendo solo los nombres. Por favor, actualiza la función de mapeo, de modo que cree una lista donde cada elemento contenga lo siguiente:

```py
'Hello, my name is <name> and I am <age> years old'
```

## 💡 Pistas:

- Tienes que obtener la edad de cada persona de acuerdo a su fecha de nacimiento (`birth_date`).

- Tómate tu tiempo para entender la función ya definida `calculate_age`.

- Busca en Google "cómo obtener la edad de alguien dada su fecha de nacimiento python".

- Dentro de tu función `format_greeting` debes devolver una concatenación.

## 💻 Resultado esperado:

La salida esperada debería ser similar a esta:

```py
[ 'Hello, my name is Joe and I am 32 years old',
  'Hello, my name is Bob and I am 42 years old',
  'Hello, my name is Erika and I am 28 years old',
  'Hello, my name is Dylan and I am 18 years old',
  'Hello, my name is Steve and I am 14 years old' ]
```
