# `15.2` Parking lot

Podemos usar una lista bidimensional (matriz) para representar el estado actual de un estacionamiento:

![Parking lot](https://storage.googleapis.com/replit/images/1558366147943_71c41e2a3f01564b5bdba6618797af79.pn)

```py

parking_state = [
  [1,0,1,1,0,1],
  [2,0,1,1,0,1],
  [1,0,2,1,0,1],
  [1,0,1,1,0,1],
  [1,0,1,1,0,2],
  [1,0,1,1,0,1],
]
```

## 📝 Instrucciones:

1. Crea una función `get_parking_lot()` que devuelva un objeto con `total_slots` (cantidad total de estacionamientos), `available_slots` (estacionamientos disponibles) y `occupied_slots`(estacionamientos ocupados) así:


```py
state = {
     total_slots: 12,
     available_slots: 3,
     occupied_slots: 9
}
```

## 💡 Pista:

- Tienes que hacer un bucle anidado.

- Declara una variable para almacenar el valor.

- Compara los estados (`state`)
