from kafka import KafkaProducer
import json
import time
import random
 
# Configurar el productor Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Asegúrate de que esto sea correcto
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
 
# Duración mínima de ejecución en segundos (ajustable)
tiempo_ejecucion = 60  # 1 minuto (ajustable)
inicio = time.time()
 
while time.time() - inicio < tiempo_ejecucion:
    equipaje = {
        "id": str(random.randint(10000, 99999)),
        "estado": random.choice(["en tránsito", "en bodega", "entregado"]),
        "ubicación": random.choice(["Zona A", "Zona B", "Zona C", "Terminal 1", "Terminal 2"])
    }
    producer.send('equipaje_tracking', equipaje)
    print(f"[x] Mensaje enviado: {equipaje}")
    time.sleep(random.uniform(0.5, 2))  # Espera aleatoria entre envíos
 
print("[x] Producción de mensajes finalizada.")