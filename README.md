# 🏥 Simulación Hospitalaria con Paradigmas de Programación

Este proyecto simula el flujo de pacientes en un hospital, aplicando **tres paradigmas de programación distribuidos**:

## 💡 Descripción General

Se modela la atención de urgencias de forma realista usando:
- **Concurrencia (threading)** para el registro de pacientes simultáneos.
- **Control de recursos (semaphore)** para limitar el acceso a camas disponibles.
- **Paralelismo (multiprocessing)** para el diagnóstico intensivo de CPU.
- **Asincronía (asyncio)** para el seguimiento simulado de pacientes vía API.

---

## ⚙️ Tecnologías utilizadas

- Python 3.12+
- `threading`
- `asyncio`
- `multiprocessing`
- `random`, `time`, `os`

---

## 📌 Estructura del Código

| Etapa                | Técnica usada                        |
|----------------------|--------------------------------------|
| Registro             | `threading.Thread` + `Semaphore(3)` |
| Diagnóstico          | `multiprocessing.Pool`              |
| Seguimiento y alta   | `async def` + `await` (con `asyncio`) |

---

## 📊 Resultados

- 5 pacientes son procesados en paralelo y de forma asincrónica.
- Cada fase simula tiempos de espera, carga computacional y respuesta de red.
- Output visible en consola con emojis y mensajes descriptivos.

---

## 📁 Archivos Incluidos

- `main.py`: Código principal.
- `Practica 1 421040001.pdf`: Documento formal de entrega.
- `image.png`: Captura del sistema corriendo.
- `_Diagrama de flujo del Hospital.pdf`: Diagrama visual del flujo.

---

## ✅ Créditos y ética

> El desarrollo fue asistido con ChatGPT para diseño, depuración y documentación del sistema.  
> Todo fue utilizado como herramienta de apoyo para el aprendizaje, de manera ética y supervisada.

---

