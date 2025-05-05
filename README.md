# Simulación Hospitalaria con Concurrencia y Paralelismo

## Descripción
Este proyecto implementa una simulación avanzada de un sistema hospitalario utilizando técnicas de programación concurrente y paralela en Python. El sistema modela el flujo de pacientes a través de diferentes etapas del proceso hospitalario, demostrando la aplicación práctica de conceptos de concurrencia y paralelismo en un escenario del mundo real.

## Características Principales

- **Procesamiento Concurrente**: Implementación de múltiples pacientes siendo procesados simultáneamente
- **Control de Recursos**: Uso de semáforos para gestionar el acceso a recursos limitados
- **Simulación Realista**: Modelado de diferentes etapas del proceso hospitalario:
  - Registro de pacientes
  - Diagnóstico automatizado
  - Asignación de recursos
  - Seguimiento y alta

## Tecnologías Utilizadas

- Python 3.x
- Modelo preentrenado para el procesamiento de imágenes (VGG16). 
- Módulos principales:
  - `asyncio` para programación asíncrona
  - `multiprocessing` para procesamiento paralelo
  - `threading` para concurrencia
  - `random` para simulación de tiempos variables

## Estructura del Proyecto

- `simulacion-hospitalaria.py`: Código de la simulación sin el uso de un modelo preentrenado.
- `simulacion-hospitalaria-ia.py`: Código de la simulación que incluye el modelo `VGG16` para el procesamiento de imágenes en el diagnostico automatizado.
- `requirements.txt`: Archivo con las dependencias necesarias.
- `Reporte.pdf`: Reporte de la práctica en formato PDF.

El sistema está organizado en las siguientes etapas principales:

1. **Registro**: Proceso inicial de ingreso del paciente
2. **Diagnóstico**: Evaluación automatizada con control de concurrencia
3. **Asignación de Recursos**: Gestión de camas y personal médico
4. **Seguimiento y Alta**: Proceso final de monitoreo y liberación

## Requisitos del Sistema

- Python 3.6 o superior
- Sistema operativo compatible con tensorflow, asyncio, threading y multiprocessing

## Instalación

1. Clonar el repositorio:
```bash
git clone git@github.com:im-krizox/practica-concurrencia-paralelismo.git
```

2. Navegar al directorio del proyecto:
```bash
cd practica-concurrencia-paralelismo/
```

3. Instalar las dependencias del proyecto:
```bash
pip install tensorflow Pillow
```

4. Ejecutar los scripts:
```bash
python3 simulacion-hospitalaria.py
```

```bash
python3 simulacion-hospitalaria-ia.py
```

## Uso

El sistema simula automáticamente el procesamiento de pacientes a través de las diferentes etapas del hospital. Además de que también se incluye otra simulación que emplea el uso de modelo preentrenado para dar un diagnostico automatizado de acuerdo a una imagen.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
