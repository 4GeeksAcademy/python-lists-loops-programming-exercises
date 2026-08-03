<!-- hide -->
<div align="center">

# Learn Python Loops and lists Interactively

[![Certified by 4Geeks Academy](https://img.shields.io/badge/Certified_by-4Geeks_Academy-2563eb)](https://4geeks.com/en/interactive-exercise/python-loops-lists-exercises)
[![Auto-graded with LearnPack](https://img.shields.io/badge/Auto--graded-LearnPack-2563eb)](https://learnpack.co)
[![Open in Codespaces](https://img.shields.io/badge/Open_in-Codespaces-fb5a1f)](https://codespaces.new/?repo=4GeeksAcademy/python-lists-loops-programming-exercises)

🇪🇸 [Estas instrucciones también están disponibles en español](https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises/blob/HEAD/README.es.md)

</div>
<!-- endhide -->

This tutorial contains **45 auto-graded Python exercises** about lists, loops, dictionaries and matrices, plus a welcome page, all inside one LearnPack package. Every exercise folder ships an `app.py`, a `test.py` and a reference `solution.hide.py`, and the whole package is graded by **131 individual pytest checks**. Estimated duration: **10 hours**, difficulty **easy**, Python 3. Instructions are available in English and Spanish, and 13 exercises include a video walkthrough.

<!-- hide -->
## 📋 About this tutorial

- **Difficulty:** easy (beginner, no previous loop experience needed)
- **Estimated duration:** 10 hours
- **Technologies:** Python 3, pytest, LearnPack
- **Exercises:** 45 auto-graded exercises + 1 welcome page
- **Automatic grading:** yes — 131 pytest checks across 45 `test.py` files
- **Video solutions:** 13 exercises embed a YouTube walkthrough
- **Languages:** instructions in English and Spanish (`README.md` and `README.es.md` inside every exercise)
<!-- endhide -->

## 🎯 What will you learn?

- **Access and mutate lists by index**, where the first position is `0`: read the 3rd item with `my_list[2]`, replace a value, and print a specific position.
- **All the ways of looping in Python**: `for item in my_list`, `for i in range(start, stop, step)` and `while`, including a countdown from `20` to `1` that ends with `LIFTOFF`.
- **Accumulator patterns written by hand**: totals, averages, maximums and minimums built with a `for` loop and an auxiliary variable instead of `sum()` or `max()`.
- **Transform lists with `map()`** across 7 exercises: converting Celsius to Fahrenheit, mapping a list with an already-defined function, printing the data type of every item with `type()`, and mapping a list of dictionaries.
- **Remove elements with `filter()`** across 5 exercises: numbers greater than `10`, names that start with a given letter, completed tasks inside a list of dictionaries, and a final one that combines `filter()` with `map()` to build `<li>` HTML tags.
- **Work with dictionaries**: read and add keys, loop over keys and values, and count letter frequencies ignoring case and spaces.
- **Build and read 2-dimensional lists (matrices)**: generate an N×N matrix of `1`s and analyse a parking-lot grid with a nested loop.

## 👀 What will you build?

The 45 exercises are small, self-contained programs that grow in difficulty. Some of the ones you will solve:

- **`03` Flip list** — turn `[45, 67, 87, 23, 5, 32, 60]` into `[60, 32, 5, 23, 87, 67, 45]` by looping the list and appending each item into a new one.
- **`07` Do While** — print every number from `20` down to `1` with a `while` loop, adding an exclamation mark to multiples of 5, and finish with `LIFTOFF`.
- **`08.2` Divide and conquer** — a `sort_odd_even()` function that returns one single flat list with the odd numbers first and the even ones after.
- **`09` Max integer** — a `max_integer()` function that receives a list and returns the biggest number using a `for` loop and an `if`.
- **`12` Map a list** — convert a list of Celsius temperatures into `[28.4, 93.2, 132.8, 14.0]` inside a `map()` call.
- **`13.4` Making HTML with filter and map** — combine both functions to output `['<li>Red</li>', '<li>Orange</li>', '<li>Pink</li>', '<li>Violet</li>']`.
- **`14.1` Letter counter** — count how many times each letter appears in a text and print a dictionary such as `{'h': 1, 'e': 1, 'l': 3, 'o': 2, ...}`.
- **`15.2` Parking lot** — a `get_parking_lot()` function that receives a matrix and returns `total_slots`, `available_slots` and `occupied_slots`.
- **`16` Techno Beats** — the final challenge: a `lyrics_generator()` function that turns `[0, 0, 1, 1, 1, 0]` into `Boom` and `Drop the bass` beats, adding `!!!Break the bass!!!` every time it finds three `1`s in a row.

![Parking lot matrix used in exercise 15.2, a grid of parking spaces where each cell of the two-dimensional list represents an occupied slot, an available slot or no slot at all](https://raw.githubusercontent.com/4GeeksAcademy/python-lists-loops-programming-exercises/master/.learn/assets/ex15.2.png)

## 🎓 What do you need before starting?

- **Python basics**: variables, `print()`, `if/else` and how to declare a function. If you have never written Python, start with [Learn Python Interactively (beginner)](https://4geeks.com/en/interactive-exercise/python-beginner-exercises) first.
- **No installation** if you open the tutorial in GitHub Codespaces or Gitpod: the container already installs Python 3.10, LearnPack and pytest for you (the Codespaces dev container also adds Node.js 22).
- **For a local setup**: Python 3, Node.js 14+ and npm, so you can install LearnPack and run `learnpack start`.
- **Zero previous knowledge of loops**: exercise `01` is a plain `print("Hello World")` and the difficulty ramps up from there.

## ✅ How does the automatic grading work?

Each of the 45 exercises has a `test.py` file executed with pytest (version 6.2.5, with `pytest-testdox` for readable output). Together they contain 131 named checks, and they grade your work in three different ways:

- **Console output**: 40 exercises capture what your program prints and compare it against the expected text, character by character, including line breaks.
- **Function behaviour**: 9 exercises require a function with an exact name, and 4 of them (`09`, `12.6`, `15.1` and `15.2`) call that function with their own inputs and compare the **returned** value, so printing instead of returning is not enough.
- **Source code inspection**: 39 exercises open your `app.py` and scan its text (some with a regular expression, some with a plain search) to make sure you actually used the construct being taught — `for`, `while`, `if`, `print`, `map`, `filter`, `type` or `import random`, depending on the exercise.

Every exercise folder also contains `solution.hide.py` with a reference solution, so you can compare approaches once you have solved it yourself.

> 💡 The tests are deliberately strict about output formatting. If your logic is right but a test still fails, compare your output with the "Expected result" block in the exercise instructions, space by space.

## 💡 What mistakes should you avoid?

- **Printing when the test expects a `return`.** In `16` Techno Beats the last lines of `app.py` already call `print(lyrics_generator([0,0,1,1,0,0,0]))`, so your function must return the string. If you print inside the function, the output is duplicated and the test fails.
- **Ignoring the function parameter.** The `15.2` Parking lot test calls `get_parking_lot()` with its own matrices, not with the global `parking_state` variable. A function that reads the global list instead of its argument fails the second and third checks.
- **Miscounting the parking-lot values.** In `15.2` a `0` is not a parking slot: only `1` (occupied) and `2` (available) count towards `total_slots`. For `[[1,1,1], [0,0,0], [1,1,2]]` the expected answer is `{'total_slots': 6, 'available_slots': 1, 'occupied_slots': 5}`.
- **Replacing `map()` or `filter()` with a list comprehension.** The 12.x tests literally search for the text `map` inside your `app.py`, and the 13.x tests search for `filter`, so a comprehension that prints the right result is not enough. The same happens with `sum()` in `05` or `max()` in `09`: those tests require a `for` loop in your code.
- **Leaving debugging `print()` calls behind.** In `05` Sum all items and `13.4` the test compares the *entire* console output with the expected string, so any extra line breaks the assertion.
- **Printing the `map()` or `filter()` object instead of the list.** Wrap the result in `list()`; the expected output looks like `[23, 12, 35, 54, 21, 534, 23, 42]`, not `<filter object at 0x...>`.
- **Off-by-one indexes.** Lists start at `0`, so the "3rd item" is `my_list[2]` and `thursday` in a week list lives at `my_list[4]`. Exercise `01.1` imports `my_list` from your file and asserts that position 4 is `None`, so do not rename or delete the variables that come predefined in `app.py`.

## ❓ Frequently asked questions

### Do I need to install anything to start?

No. Opening the repository in GitHub Codespaces or Gitpod builds a container with Python 3.10, LearnPack and pytest already installed, and the exercises start on their own. Installing locally is optional and takes two commands.

### Do I need to know Python before starting these exercises?

You need the very basics: variables, `print()`, `if/else` and function declarations. Lists, indexes, loops, `map()`, `filter()`, dictionaries and matrices are all explained from scratch inside the exercise instructions.

### How long does it take to complete the 45 exercises?

The package is estimated at 10 hours of work. The first exercises take a couple of minutes each, while the final ones (`15.2` Parking lot and `16` Techno Beats) require nested loops and auxiliary counters and can take considerably longer.

### Can I solve the exercises with list comprehensions instead of `map()` and `filter()`?

Not if you want the tests to pass. The seven `map()` exercises and the five `filter()` exercises inspect your source code and look for the corresponding function inside `app.py`. Once you have passed them, rewriting the solution as a comprehension is an excellent extra practice.

### Why does my exercise fail if the console output looks correct?

Because the assertions compare exact strings. A missing trailing space, a different number of decimals, single quotes instead of double quotes inside a printed list, or an extra debugging line are enough to fail. Copy the "Expected result" block from the instructions and compare it literally with your output.

### Is this tutorial free, and can I reuse the code?

Access to the exercises costs nothing and the solutions you write are yours to keep and reuse. The tutorial content itself is not open source: the [LICENSE](https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises/blob/HEAD/LICENSE.md) reserves all intellectual property rights and does not allow republishing, selling or redistributing the material.

<!-- hide -->
## 📚 Related tutorials

- [Learn Python Interactively (beginner)](https://4geeks.com/en/interactive-exercise/python-beginner-exercises) — the recommended step before this one.
- [Learn Python Functions Interactively](https://4geeks.com/en/interactive-exercise/python-function-exercises) — parameters, return values and scope.
- [Learn Object Oriented Programming with Python](https://4geeks.com/en/interactive-exercise/object-oriented-programing-with-python) — classes and objects.
- [Master Python by practice (interactive)](https://4geeks.com/en/interactive-exercise/master-python-exercises) — a bigger challenge once loops feel natural.

## 🚀 How to start

The fastest way is to open the repository in a ready-made cloud environment:

1. Click [Open in Codespaces](https://codespaces.new/?repo=4GeeksAcademy/python-lists-loops-programming-exercises) (recommended) or [Open in Gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises).

2. Wait for the container to finish building. It installs Python 3.10, `pytest`, LearnPack and the LearnPack Python plugin (in Codespaces it also installs Node.js 22).

3. The LearnPack exercises should open automatically. If they do not, run this in the terminal:

    ```bash
    $ learnpack start
    ```

There is also an intro video for the whole tutorial: [Python lists and loops introduction](https://www.youtube.com/watch?v=xMg9d0KsYAk).

## 💻 Local installation

1. Install [LearnPack](https://learnpack.co) and its Python plugin (you need Node.js 14+ and Python 3):

    ```bash
    $ npm i @learnpack/learnpack@5.0.348 -g && learnpack plugins:install @learnpack/python@1.0.6
    ```

2. Clone this repository and enter the folder:

    ```bash
    $ git clone https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises.git
    $ cd python-lists-loops-programming-exercises
    ```

3. Install the testing dependencies and start the tutorial from the same folder that contains `learn.json`:

    ```bash
    $ pip3 install pytest==6.2.5 pytest-testdox mock
    $ learnpack start
    ```

## 📝 How the exercises are organized

Every exercise lives in its own folder inside `exercises/` and contains the same set of files:

1. **`app.py`** — the file you edit; it is the Python script that gets executed.

2. **`README.md`** and **`README.es.md`** — the instructions in English and Spanish, sometimes with a linked video tutorial.

3. **`test.py`** — the grading script. You do not need to open it, but reading it tells you exactly what is being checked.

4. **`solution.hide.py`** — the reference solution for that exercise.

Found a bug or a typo? [Report it here](https://github.com/learnpack/learnpack/issues/new); these exercises are built collaboratively and every report helps.

## 🤝 Contributors

Thanks to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

1. [Alejandro Sánchez (alesanchezr)](https://github.com/alesanchezr) — (coder) 💻, (idea) 🤔, (build-tests) ⚠️, (pull-request-review) 👀, (build-tutorial) ✅, (documentation) 📖

2. [Paolo (plucodev)](https://github.com/plucodev) — (bug reports) 🐛, (coder) 💻, (translation) 🌎

See the full list of [contributors](https://github.com/4GeeksAcademy/python-lists-loops-programming-exercises/graphs/contributors). This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification; contributions of any kind are welcome.

This and many other exercises are built by students as part of the [4Geeks Academy](https://4geeks.com/en/coding-bootcamp) coding bootcamp. Learn more about the [Full Stack Developer career program](https://4geeks.com/en/career-programs/full-stack) and the [Data Science and Machine Learning career program](https://4geeks.com/en/career-programs/data-science-ml).
<!-- endhide -->
