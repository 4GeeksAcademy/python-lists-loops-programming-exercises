# `15.2` Parking lot

Podemos usar una lista bidimensional (matriz) para representar el estado actual de un estacionamiento:

![Parking lot](../../.learn/assets/ex15.2.png)
  

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

## 💡 Pistas:

- Declara las claves para almacenar los valores.
  
- Tienes que hacer un bucle anidado.

- Compara los estados (`state`)
