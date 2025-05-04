import random
import time
import asyncio
import multiprocessing
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

# Función de asignación de recursos para cumplir con el orden de asignar primero la cama y después el doctor
def asignacion_recursos(paciente_id):
    # Primero asignar cama
    cama = f"Cama {random.randint(1, 10)}"
    print(f"Paciente {paciente_id}: Cama asignada: {cama}.")
    
    # Luego asignar doctor
    doctor = f"Doctor {random.randint(1, 5)}"
    print(f"Paciente {paciente_id}: Doctor asignado: {doctor}.")
    
    time.sleep(random.uniform(1, 2))  # Simulando asignación
    print(f"Paciente {paciente_id}: Asignación de recursos completada.")

# Función de seguimiento y alta para ser procesada en multiprocessing
def seguimiento_y_alta(paciente_id):
    print(f"Paciente {paciente_id}: Seguimiento y alta iniciado.")
    time.sleep(random.uniform(1, 3))  # Simulando alta
    print(f"Paciente {paciente_id}: Alta completada.")

async def proceso_paciente(paciente_id, semaforo):
    # Etapas en orden
    registro(paciente_id)
    await diagnostico(paciente_id, semaforo)
    
    asignacion_recursos(paciente_id)
    
    # La etapa de seguimiento y alta se realiza en paralelo usando multiprocessing
    p = multiprocessing.Process(target=seguimiento_y_alta, args=(paciente_id,))
    p.start()
    p.join()  # Espera a que el proceso termine antes de continuar

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
    # Pedir al usuario que ingrese el número de pacientes
    num_pacientes = int(input("Ingrese el número de pacientes a simular: "))
    
    # Simulando la llegada de pacientes al hospital
    pacientes = list(range(1, num_pacientes + 1))
    
    # Medir el tiempo de ejecución
    start_time = time.time()
    
    simular_hospital(pacientes)
    
    # Imprimir el tiempo total de la simulación
    end_time = time.time()
    print(f"La simulación duró {end_time - start_time:.2f} segundos.")