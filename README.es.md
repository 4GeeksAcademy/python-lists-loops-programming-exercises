<!-- hide -->
<div align="center">

# Aprende listas y bucles de Python Interactivamente

[![Certificado por 4Geeks Academy](https://img.shields.io/badge/Certificado_por-4Geeks_Academy-2563eb)](https://4geeks.com/es/interactive-exercise/python-loops-lists-exercises-es)
[![Autocorregido con LearnPack](https://img.shields.io/badge/Autocorregido-LearnPack-2563eb)](https://learnpack.co)
[![Abrir en Codespaces](https://img.shields.io/badge/Abrir_en-Codespaces-fb5a1f)](https://codespaces.new/?repo=4GeeksAcademy/python-lists-loops-programming-exercises)

🇬🇧 [These instructions are also available in English](https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises/blob/HEAD/README.md)

</div>
<!-- endhide -->

Este tutorial reúne **45 ejercicios de Python autocorregidos** sobre listas, bucles, diccionarios y matrices, más una página de bienvenida, dentro de un único paquete LearnPack. Cada ejercicio incluye su `app.py`, su `test.py` y una solución de referencia en `solution.hide.py`, y todo el paquete se corrige con **131 comprobaciones de pytest**. Duración estimada: **10 horas**, dificultad **fácil**, Python 3. Las instrucciones están en español e inglés y 13 ejercicios traen vídeo explicativo.

<!-- hide -->
## 📋 Sobre este tutorial

- **Dificultad:** fácil (para principiantes, no hace falta saber nada de bucles)
- **Duración estimada:** 10 horas
- **Tecnologías:** Python 3, pytest, LearnPack
- **Ejercicios:** 45 ejercicios autocorregidos + 1 página de bienvenida
- **Corrección automática:** sí — 131 comprobaciones de pytest repartidas en 45 archivos `test.py`
- **Vídeo soluciones:** 13 ejercicios enlazan un vídeo de YouTube
- **Idiomas:** instrucciones en español e inglés (`README.es.md` y `README.md` dentro de cada ejercicio)
<!-- endhide -->

## 🎯 ¿Qué vas a aprender?

- **A acceder y modificar listas por índice**, sabiendo que la primera posición es la `0`: leer el tercer elemento con `mi_lista[2]`, sustituir un valor e imprimir una posición concreta.
- **Todas las formas de iterar en Python**: `for elemento in mi_lista`, `for i in range(inicio, fin, paso)` y `while`, incluida una cuenta atrás de `20` a `1` que termina con `LIFTOFF`.
- **Los patrones de acumulador escritos a mano**: totales, medias, máximos y mínimos construidos con un bucle `for` y una variable auxiliar en lugar de `sum()` o `max()`.
- **A transformar listas con `map()`** en 7 ejercicios: pasar de grados Celsius a Fahrenheit, mapear una lista con una función ya definida, imprimir el tipo de dato de cada elemento con `type()` y mapear una lista de diccionarios.
- **A descartar elementos con `filter()`** en 5 ejercicios: números mayores que `10`, nombres que empiezan por una letra concreta, tareas ya completadas dentro de una lista de diccionarios y un último ejercicio que combina `filter()` con `map()` para construir etiquetas `<li>` de HTML.
- **A manejar diccionarios**: leer y añadir claves, recorrer claves y valores, y contar cuántas veces se repite cada letra ignorando mayúsculas y espacios.
- **A construir y leer listas de dos dimensiones (matrices)**: generar una matriz de `1` de N×N y analizar la cuadrícula de un aparcamiento con bucles anidados.

## 👀 ¿Qué vas a construir?

Los 45 ejercicios son programas pequeños e independientes que van subiendo de dificultad. Algunos de los que vas a resolver:

- **`03` Flip list** — convertir `[45, 67, 87, 23, 5, 32, 60]` en `[60, 32, 5, 23, 87, 67, 45]` recorriendo la lista y añadiendo cada elemento a otra nueva.
- **`07` Do While** — imprimir con un `while` los números del `20` al `1`, añadiendo un signo de exclamación a los múltiplos de 5 y terminando con `LIFTOFF`.
- **`08.2` Divide and conquer** — una función `sort_odd_even()` que devuelve una sola lista plana con los impares primero y los pares después.
- **`09` Max integer** — una función `max_integer()` que recibe una lista y devuelve el número más grande usando un `for` y un `if`.
- **`12` Map a list** — convertir una lista de temperaturas en Celsius en `[28.4, 93.2, 132.8, 14.0]` dentro de un `map()`.
- **`13.4` Making HTML with filter and map** — combinar las dos funciones para obtener `['<li>Red</li>', '<li>Orange</li>', '<li>Pink</li>', '<li>Violet</li>']`.
- **`14.1` Letter counter** — contar cuántas veces aparece cada letra de un texto e imprimir un diccionario del estilo `{'h': 1, 'e': 1, 'l': 3, 'o': 2, ...}`.
- **`15.2` Parking lot** — una función `get_parking_lot()` que recibe una matriz y devuelve `total_slots`, `available_slots` y `occupied_slots`.
- **`16` Techno Beats** — el reto final: una función `lyrics_generator()` que convierte `[0, 0, 1, 1, 1, 0]` en una letra de `Boom` y `Drop the bass`, añadiendo `!!!Break the bass!!!` cada vez que encuentra tres `1` seguidos.

![Matriz del aparcamiento del ejercicio 15.2: una cuadricula de plazas de parking donde cada celda de la lista bidimensional representa una plaza ocupada, una plaza libre o un hueco que no es plaza](https://raw.githubusercontent.com/4GeeksAcademy/python-lists-loops-programming-exercises/master/.learn/assets/ex15.2.png)

## 🎓 ¿Qué necesitas saber antes de empezar?

- **Lo básico de Python**: variables, `print()`, `if/else` y cómo declarar una función. Si nunca has escrito Python, empieza por [Aprende Python Interactivamente (Principiante)](https://4geeks.com/es/interactive-exercise/python-beginner-exercises-es).
- **Nada que instalar** si abres el tutorial en GitHub Codespaces o Gitpod: el contenedor ya trae Python 3.10, LearnPack y pytest listos (el contenedor de Codespaces añade además Node.js 22).
- **Para trabajar en local**: Python 3, Node.js 14+ y npm, para poder instalar LearnPack y ejecutar `learnpack start`.
- **Cero experiencia con bucles**: el ejercicio `01` es un simple `print("Hello World")` y a partir de ahí la dificultad sube poco a poco.

## ✅ ¿Cómo funciona la corrección automática?

Cada uno de los 45 ejercicios tiene su archivo `test.py`, que se ejecuta con pytest (versión 6.2.5, junto a `pytest-testdox` para leer los resultados con claridad). Entre todos suman 131 comprobaciones con nombre y revisan tu trabajo de tres maneras distintas:

- **Salida por consola**: 40 ejercicios capturan lo que imprime tu programa y lo comparan con el texto esperado carácter a carácter, saltos de línea incluidos.
- **Comportamiento de la función**: 9 ejercicios exigen una función con un nombre exacto y 4 de ellos (`09`, `12.6`, `15.1` y `15.2`) la llaman con sus propios datos y comparan el valor **devuelto**, así que imprimir no basta.
- **Revisión del código fuente**: 39 ejercicios abren tu `app.py` y rastrean su texto (unos con una expresión regular, otros con una búsqueda simple) para asegurarse de que usaste la construcción que se está enseñando: `for`, `while`, `if`, `print`, `map`, `filter`, `type` o `import random`, según el caso.

Además, cada carpeta de ejercicio incluye un `solution.hide.py` con una solución de referencia que puedes comparar con la tuya una vez lo hayas resuelto por tu cuenta.

> 💡 Los tests son muy estrictos con el formato de la salida. Si tu lógica es correcta y aun así falla, compara tu resultado con el bloque «Resultado esperado» de las instrucciones, espacio por espacio.

## 💡 ¿Qué errores conviene evitar?

- **Imprimir cuando el test espera un `return`.** En `16` Techno Beats las últimas líneas de `app.py` ya hacen `print(lyrics_generator([0,0,1,1,0,0,0]))`, así que tu función tiene que devolver la cadena. Si imprimes dentro de la función, la salida se duplica y el test falla.
- **Olvidarte del parámetro de la función.** El test de `15.2` Parking lot llama a `get_parking_lot()` con sus propias matrices, no con la variable global `parking_state`. Una función que lea la lista global en vez de su argumento no pasa la segunda ni la tercera comprobación.
- **Contar mal las plazas del aparcamiento.** En `15.2` un `0` no es una plaza: solo el `1` (ocupada) y el `2` (libre) suman en `total_slots`. Para `[[1,1,1], [0,0,0], [1,1,2]]` la respuesta esperada es `{'total_slots': 6, 'available_slots': 1, 'occupied_slots': 5}`.
- **Sustituir `map()` o `filter()` por una comprensión de lista.** Los tests de los ejercicios 12.x buscan literalmente el texto `map` dentro de tu `app.py`, y los de 13.x buscan `filter`, así que una comprensión que imprima el resultado correcto no basta. Pasa lo mismo con `sum()` en `05` o `max()` en `09`: esos tests exigen que haya un bucle `for` en tu código.
- **Dejar `print()` de depuración por el camino.** En `05` Sum all items y en `13.4` el test compara la salida *completa* de la consola con la cadena esperada, así que cualquier línea de más rompe la comprobación.
- **Imprimir el objeto `map()` o `filter()` en lugar de la lista.** Envuélvelo en `list()`: se espera algo como `[23, 12, 35, 54, 21, 534, 23, 42]`, no `<filter object at 0x...>`.
- **Equivocarte de índice por uno.** Las listas empiezan en `0`, así que el «tercer elemento» es `mi_lista[2]` y `thursday`, en una lista con los días de la semana, está en `mi_lista[4]`. El test de `01.1` importa `my_list` desde tu archivo y comprueba que la posición 4 valga `None`, o sea que no renombres ni borres las variables que ya vienen en `app.py`.

## ❓ Preguntas frecuentes

### ¿Necesito instalar algo para empezar?

No. Al abrir el repositorio en GitHub Codespaces o en Gitpod se crea un contenedor que ya trae Python 3.10, LearnPack y pytest instalados, y los ejercicios arrancan solos. La instalación local es opcional y son dos comandos.

### ¿Hace falta saber Python antes de empezar?

Solo lo mínimo: variables, `print()`, `if/else` y cómo declarar una función. Las listas, los índices, los bucles, `map()`, `filter()`, los diccionarios y las matrices se explican desde cero en las propias instrucciones de cada ejercicio.

### ¿Cuánto se tarda en terminar los 45 ejercicios?

El paquete está estimado en 10 horas. Los primeros ejercicios se resuelven en un par de minutos, mientras que los últimos (`15.2` Parking lot y `16` Techno Beats) requieren bucles anidados y variables auxiliares, y pueden llevar bastante más tiempo.

### ¿Puedo resolver los ejercicios con comprensiones de lista en vez de `map()` y `filter()`?

No si quieres que los tests pasen. Los siete ejercicios de `map()` y los cinco de `filter()` revisan tu código fuente y buscan la función correspondiente dentro de `app.py`. Una vez aprobados, reescribir la solución con una comprensión es un ejercicio extra buenísimo.

### ¿Por qué falla mi ejercicio si la salida de la consola se ve bien?

Porque las comprobaciones comparan cadenas exactas. Un espacio final que falta, un decimal de más, comillas simples en lugar de dobles dentro de una lista impresa o una línea de depuración sobrante bastan para fallar. Copia el bloque «Resultado esperado» de las instrucciones y compáralo literalmente con tu salida.

### ¿El tutorial es gratis? ¿Puedo reutilizar el código?

Acceder a los ejercicios no cuesta nada y el código que escribas es tuyo: puedes guardarlo y reutilizarlo. El contenido del tutorial, en cambio, no es de código abierto: la [licencia](https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises/blob/HEAD/LICENSE.md) reserva todos los derechos de propiedad intelectual y no permite republicar, vender ni redistribuir el material.

<!-- hide -->
## 📚 Tutoriales relacionados

- [Aprende Python Interactivamente (Principiante)](https://4geeks.com/es/interactive-exercise/python-beginner-exercises-es) — el paso recomendado antes de este.
- [Aprende las funciones de Python Interactivamente](https://4geeks.com/es/interactive-exercise/python-function-exercises-es) — parámetros, valores de retorno y ámbito.
- [Aprende Programación Orientada a Objetos con Python](https://4geeks.com/es/interactive-exercise/aprende-programacion-orientada-a-objetos-con-python) — clases y objetos.
- [Domina Python Practicando (interactivo)](https://4geeks.com/es/interactive-exercise/master-python-exercises-es) — el siguiente reto cuando los bucles ya te salgan solos.

## 🚀 Cómo empezar

Lo más rápido es abrir el repositorio en un entorno en la nube ya preparado:

1. Haz clic en [Abrir en Codespaces](https://codespaces.new/?repo=4GeeksAcademy/python-lists-loops-programming-exercises) (recomendado) o en [Abrir en Gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises).

2. Espera a que el contenedor termine de construirse: instala Python 3.10, `pytest`, LearnPack y el plugin de Python de LearnPack (en Codespaces instala además Node.js 22).

3. Los ejercicios de LearnPack deberían abrirse automáticamente. Si no lo hacen, escribe esto en la terminal:

    ```bash
    $ learnpack start
    ```

También hay un vídeo de introducción a todo el tutorial: [Introducción a listas y bucles en Python](https://www.youtube.com/watch?v=xMg9d0KsYAk).

## 💻 Instalación local

1. Instala [LearnPack](https://learnpack.co) y su plugin de Python (necesitas Node.js 14+ y Python 3):

    ```bash
    $ npm i @learnpack/learnpack@5.0.348 -g && learnpack plugins:install @learnpack/python@1.0.6
    ```

2. Clona este repositorio y entra en la carpeta:

    ```bash
    $ git clone https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises.git
    $ cd python-lists-loops-programming-exercises
    ```

3. Instala las dependencias de los tests y arranca el tutorial desde la misma carpeta donde está `learn.json`:

    ```bash
    $ pip3 install pytest==6.2.5 pytest-testdox mock
    $ learnpack start
    ```

## 📝 Cómo están organizados los ejercicios

Cada ejercicio vive en su propia carpeta dentro de `exercises/` y contiene siempre los mismos archivos:

1. **`app.py`** — el archivo que editas; es el script de Python que se ejecuta.

2. **`README.md`** y **`README.es.md`** — las instrucciones en inglés y en español, a veces con un vídeo tutorial enlazado.

3. **`test.py`** — el script de corrección. No hace falta que lo abras, pero leerlo te dice exactamente qué se está comprobando.

4. **`solution.hide.py`** — la solución de referencia de ese ejercicio.

¿Has encontrado un error o una errata? [Repórtalo aquí](https://github.com/learnpack/learnpack/issues/new); estos ejercicios se construyen entre todos y cada aviso ayuda.

## 🤝 Colaboradores

Gracias a estas personas maravillosas ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

1. [Alejandro Sánchez (alesanchezr)](https://github.com/alesanchezr) — (programador) 💻, (idea) 🤔, (build-tests) ⚠️, (pull-request-review) 👀, (build-tutorial) ✅, (documentación) 📖

2. [Paolo (plucodev)](https://github.com/plucodev) — (bug reports) 🐛, (programador) 💻, (traducción) 🌎

Consulta la lista completa de [colaboradores](https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises/graphs/contributors). Este proyecto sigue la especificación [all-contributors](https://github.com/kentcdodds/all-contributors) y toda contribución es bienvenida.

Estos y muchos otros ejercicios los construyen los estudiantes del bootcamp de [4Geeks Academy](https://4geeks.com/es/blog/aprender-a-programar/aprender-a-programar-desde-cero). Conoce más sobre el [Bootcamp de Desarrollador Full Stack](https://4geeks.com/es/programas-de-carrera/desarrollo-full-stack) y el [Bootcamp de Data Science y Machine Learning](https://4geeks.com/es/programas-de-carrera/ciencia-de-datos-ml).
<!-- endhide -->
