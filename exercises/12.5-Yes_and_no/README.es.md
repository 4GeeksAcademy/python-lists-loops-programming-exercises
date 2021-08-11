# `12.5` Sí y no

# 📝 Instrucciones
1. Por favor, usa la funcionalidad de mapeo de lista para iterar la lista de buleanos y crear una nueva lista
   que contentdrá el texto 'wiki' por cada 1 y 'woko' por cada 0 que tenga la lista original.
2. Imprime la nueva lista en la consola.

```py
Ejemplo de salida:

[ 'woko',   'wiki',   'woko',   'woko',   'wiki',   'wiki',   'wiki',   'woko',   'woko',   'wiki',   'woko',   'wiki',   'wiki',   'woko',   'woko',   'woko',   'woko',   'woko',   'woko',   'woko',   'woko',   'wiki',   'woko',   'woko',   'woko',   'woko',   'wiki' ]
```

## 💡 Pista:

- Necesitas mapear la lista entera.

- Dentro de tu función `map()`necesitas usar un condicional para verificar si el valor actual es `1` o `0`.

- Si el valor es `1` asignas el texto `wiki`.

- Si el valor es `0` asignas el texto `woko`.