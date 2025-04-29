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
- Módulos principales:
  - `asyncio` para programación asíncrona
  - `multiprocessing` para procesamiento paralelo
  - `threading` para concurrencia
  - `random` para simulación de tiempos variables

## Estructura del Proyecto

El sistema está organizado en las siguientes etapas principales:

1. **Registro**: Proceso inicial de ingreso del paciente
2. **Diagnóstico**: Evaluación automatizada con control de concurrencia
3. **Asignación de Recursos**: Gestión de camas y personal médico
4. **Seguimiento y Alta**: Proceso final de monitoreo y liberación

## Requisitos del Sistema

- Python 3.6 o superior
- Sistema operativo compatible con asyncio y multiprocessing

## Instalación

1. Clonar el repositorio:
```bash
git clone git@github.com:im-krizox/practica-concurrencia-paralelismo.git
```

2. Navegar al directorio del proyecto:
```bash
cd practica-concurrencia-paralelismo/
```

3. Ejecutar el script:
```bash
python simulacion-hospitalaria.py
```

## Uso

El sistema simula automáticamente el procesamiento de pacientes a través de las diferentes etapas del hospital. Por defecto, se simulan 5 pacientes, pero este número puede ser modificado en el código según las necesidades.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
