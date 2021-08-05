# `01.3` Imprimir el último

¡Nunca sabrás cuántos `items` tiene `my_stupid_list`, porque está siendo generada **aleatoriamente** durante la ejecución!

Sabes que la propiedad:
```py
len(name_list) # funcion
```
devuelve la length of (longitud de) `name_list`.

## 📝 Instrucciones:

1. Importa la función `random` al inicio del archivo.

2. Crea una variable llamada `the_last_one` y asígnale el último elemento de `my_stupid_list`.

3. Imprime `the_last_one` en la consola.

## 💡 Pista:

- Para usar la función random, debemos importarla. La forma más efectiva de hacerlo es `import random`, sin comillas, al principio del archivo. Para más información sobre la importación, consulta la documentación de Python: https://docs.python.org/3/reference/import.html?highlight=importing.

- Recuerda que, en Python, podemos acceder al primer elemento de la lista usando my_list_name[0], al segundo con my_list_name[1] y así. Para acceder a elementos empezando en el *fin* de la lista, podemos usar valores negativos, empezando desde my_list_name[-1] (no hay un [-0]). Para más, consulta esto: https://docs.python.org/3/tutorial/introduction.html.
