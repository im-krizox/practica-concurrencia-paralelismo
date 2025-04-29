import random
import time
import asyncio
import multiprocessing
import threading
from asyncio import Semaphore

# Definir las etapas del proceso
def registro(paciente_id):
    print(f"Paciente {paciente_id}: Registro iniciado.")
    time.sleep(random.uniform(1, 3))  # Simulando tiempo de registro
    print(f"Paciente {paciente_id}: Registro completado.")

async def diagnostico(paciente_id, semaforo):
    async with semaforo:
        print(f"Paciente {paciente_id}: Diagnóstico automatizado iniciado.")
        await asyncio.sleep(random.uniform(2, 5))  # Simulando diagnóstico IA
        print(f"Paciente {paciente_id}: Diagnóstico completado.")

def asignacion_recursos(paciente_id):
    print(f"Paciente {paciente_id}: Asignación de recursos (camas, doctores) iniciada.")
    time.sleep(random.uniform(1, 2))  # Simulando asignación
    print(f"Paciente {paciente_id}: Asignación de recursos completada.")

def seguimiento_y_alta(paciente_id):
    print(f"Paciente {paciente_id}: Seguimiento y alta iniciado.")
    time.sleep(random.uniform(1, 3))  # Simulando alta
    print(f"Paciente {paciente_id}: Alta completada.")

async def proceso_paciente(paciente_id, semaforo):
    # Etapas en orden
    registro(paciente_id)
    await diagnostico(paciente_id, semaforo)
    asignacion_recursos(paciente_id)
    seguimiento_y_alta(paciente_id)

def simular_hospital(pacientes):
    # Semáforo para limitar las solicitudes concurrentes de diagnóstico
    semaforo = Semaphore(2)  # Solo 2 diagnósticos concurrentes a la vez

    loop = asyncio.get_event_loop()

    # Crear las tareas para los pacientes
    tareas = []
    for paciente_id in pacientes:
        tarea = asyncio.ensure_future(proceso_paciente(paciente_id, semaforo))
        tareas.append(tarea)

    loop.run_until_complete(asyncio.gather(*tareas))
    print("Todos los pacientes han sido procesados.")

# Función principal para ejecutar la simulación
if __name__ == "__main__":
    # Simulando la llegada de 5 pacientes al hospital
    pacientes = [1, 2, 3, 4, 5]
    simular_hospital(pacientes)