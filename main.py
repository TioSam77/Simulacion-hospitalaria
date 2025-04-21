import threading
import multiprocessing
import asyncio
import time
import os
import random

# Control de camas disponibles: solo 3 pacientes a la vez
camas_disponibles = threading.Semaphore(3)

# Seguimiento asíncrono (alta del paciente y envío de expediente)
async def seguimiento_paciente(id_paciente):
    print(f"📡 Enviando expediente del paciente {id_paciente} a la nube...")
    await asyncio.sleep(random.uniform(1, 3))  # Simula latencia de red
    print(f"☁️ Expediente del paciente {id_paciente} enviado correctamente.")

# Registro concurrente con uso de camas (controlado con semáforo)
def registrar_paciente(id_paciente):
    print(f"📝 Paciente {id_paciente} esperando cama...")
    with camas_disponibles:  # Espera si no hay camas disponibles
        print(f"🛏️ Paciente {id_paciente} asignado a una cama.")
        time.sleep(1)  # Simula el tiempo de registro
        print(f"✅ Paciente {id_paciente} registrado y cama liberada.")
    return id_paciente

# Diagnóstico paralelo (simula carga pesada tipo IA)
def diagnosticar_paciente(id_paciente):
    print(f"🧪 Diagnóstico iniciado para paciente {id_paciente} (PID {os.getpid()})")
    resultado = sum(i*i for i in range(10_000_000))  # Cálculo intensivo
    time.sleep(1)
    print(f"🔍 Diagnóstico completado para paciente {id_paciente}")
    return resultado

def main():
    pacientes = [1, 2, 3, 4, 5]
    hilos = []

    # Fase 1: Registro concurrente
    for id_paciente in pacientes:
        hilo = threading.Thread(target=registrar_paciente, args=(id_paciente,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("🏥 Todos los pacientes han sido registrados.\n")

    # Fase 2: Diagnóstico paralelo
    with multiprocessing.Pool(processes=3) as pool:
        pool.map(diagnosticar_paciente, pacientes)

    # Fase 3: Seguimiento y alta (asincronía)
    print("\n🔄 Enviando expedientes a la nube...\n")
    async def procesar_seguimiento():
        tareas = [seguimiento_paciente(p) for p in pacientes]
        await asyncio.gather(*tareas)

    asyncio.run(procesar_seguimiento())

    print("\n🧾 Todos los diagnósticos han sido realizados.")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
