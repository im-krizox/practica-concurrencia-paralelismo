import random
import time
import asyncio
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
from asyncio import Semaphore
import multiprocessing

# Función para cargar y preprocesar la imagen
def cargar_y_preprocesar_imagen(imagen_paciente):
    img = image.load_img(imagen_paciente, target_size=(224, 224))  # Cargar la imagen
    img_array = image.img_to_array(img)  # Convertir la imagen a array
    img_array = tf.expand_dims(img_array, axis=0)  # Expande dimensiones
    img_array = preprocess_input(img_array)  # Preprocesar la imagen para el modelo
    return img_array

# Función para hacer predicción con el modelo preentrenado
def diagnostico_ia(imagen_paciente):
    img_array = cargar_y_preprocesar_imagen(imagen_paciente)  # Preprocesar la imagen
    preds = model.predict(img_array)  # Realizar la predicción
    decoded_preds = decode_predictions(preds, top=3)[0]  # Decodificar las predicciones
    print(f"Diagnóstico automático: {decoded_preds}")
    return decoded_preds

# Función de diagnóstico asincrónico
async def diagnostico(paciente_id, semaforo):
    async with semaforo:
        print(f"Paciente {paciente_id}: Diagnóstico automatizado iniciado.")
        # imagen_paciente = f"paciente_{paciente_id}_radiografia.jpg" # Si tuvieramos varias imágenes por paciente
        imagen_paciente = f"image.jpg" # Ejemplo de imagen
        predicciones = diagnostico_ia(imagen_paciente)  # Llamar al modelo de IA
        
        # Simulamos el tiempo de diagnóstico con IA
        await asyncio.sleep(random.uniform(2, 5))  
        
        print(f"Paciente {paciente_id}: Diagnóstico completado. Predicción: {predicciones[0][1]} con probabilidad de {predicciones[0][2]:.2f}")

# Modificación de la función de asignación de recursos para cumplir con el orden de primero cama y después doctor
def asignacion_recursos(paciente_id):
    cama = f"Cama {random.randint(1, 10)}"
    print(f"Paciente {paciente_id}: Cama asignada: {cama}.")
    doctor = f"Doctor {random.randint(1, 5)}"
    print(f"Paciente {paciente_id}: Doctor asignado: {doctor}.")
    time.sleep(random.uniform(1, 2))  # Simulando asignación
    print(f"Paciente {paciente_id}: Asignación de recursos completada.")

# Función de seguimiento y alta para ser procesada en multiprocessing
def seguimiento_y_alta(paciente_id):
    print(f"Paciente {paciente_id}: Seguimiento y alta iniciado.")
    time.sleep(random.uniform(1, 3))  # Simulando alta
    print(f"Paciente {paciente_id}: Alta completada.")

# Función de registro para los pacientes
def registro(paciente_id):
    print(f"Paciente {paciente_id}: Registro realizado.")

# Función principal de proceso de paciente
async def proceso_paciente(paciente_id, semaforo):
    # Etapas en orden
    registro(paciente_id)
    await diagnostico(paciente_id, semaforo)
    
    asignacion_recursos(paciente_id)
    
    # La etapa de seguimiento y alta se realiza en paralelo usando multiprocessing
    p = multiprocessing.Process(target=seguimiento_y_alta, args=(paciente_id,))
    p.start()
    p.join()  # Espera a que el proceso termine antes de continuar

# Función para simular el hospital
def simular_hospital(pacientes):
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
    # Cargar el modelo preentrenado VGG16
    model = VGG16(weights='imagenet')

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
