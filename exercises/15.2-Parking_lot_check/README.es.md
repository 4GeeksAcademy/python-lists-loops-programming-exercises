# `15.2` El Parking

Podemos usar una lista bidimensional (matriz) para representar el estado actual de un parking:
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

# 📝 Instrucciones
1. Crea una función get_parking_lot() que devuelva un objeto con total_slots, 
available_slots y occupied_slots como sigue:
const state = {
     totalSlots: 12,
     availableSlots: 3,
     occupiedSlots: 9
}

## 💡 Sugerencias
- Tienes que hacer un bucle anidado
- Declara una variable para almacenar el valor
- Compara los estados
