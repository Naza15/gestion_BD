from kafka import KafkaConsumer
import json
 
consumer = KafkaConsumer(
    'equipaje_tracking',
    bootstrap_servers='localhost:9092', 
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)
 
for mensaje in consumer:
    print(f"[x] Equipaje actualizado: {mensaje.value}")
