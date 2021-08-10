# `10.1` Y uno, y dos, y tres

Los diccionarios (o `dict` en Python) son una forma de almacenar elementos como lo harías en una lista de Python. Pero, en lugar de acceder a los elementos por su índice, asignas una **clave fija** a cada uno y accedes al elemento usando su `key`.

Ahora te enfrentas a un par "clave-valor", el cual es, en ocasiones, una estructura de datos más apropiada 
para muchos problemas, en lugar de una simple lista.


## 📝 Instrucciones

1. Dado un objeto `contact`, por favor itera todas sus propiedades y valores` e imprímelos en la consola.

2. Tendrás que iterar sus propiedades para poder imprimirlos.

```py
Ejemplo de salida:
fullname : John Doe
phone : 123-123-2134
email : test@nowhere.com
```

## 💡 Pista:

- contact.keys()  `['fullname', 'phone', 'email']`

- contact.values()  `['Jane Doe', '321-321-4321', 'test@test.com']`

- contact.items()  `[('fullname', 'Jane Doe'), ('phone', '321-321-4321'), `
                    `('email', 'test@test.com')]`
