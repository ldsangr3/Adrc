import time
import datetime
current_time = datetime.datetime.now()

        # Define las horas a las que se ejecutan las tareas
task1_hour = 17  # Ejecuta la tarea 1 a las 8:00
task2_hour = 10

# Ejecuta la tarea 2 a las 0:00 (medianoche)

current_time = datetime.datetime.now()

current_hour = current_time.hour
current_minute = current_time.minute


print(current_hour)
        # Verifica si es hora de ejecutar la tarea 1
if current_hour >= task1_hour:
    # Aquí va el código para ejecutar la tarea 1
    print("Ejecutar_ I")
    

# Verifica si es hora de ejecutar la tarea 2
elif current_hour >= task2_hour:
    # Aquí va el código para ejecutar la tarea 2
    print("Ejecutar_ II")
    