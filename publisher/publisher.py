import paho.mqtt.client as mqtt
import time, random, json

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883, 60)
client.loop_start()

lojas = [f"loja_{i:02d}" for i in range(1, 15)]
inicio = time.time()

while True:
    for loja in lojas:
        temp = round(random.uniform(3.0, 7.0), 2)
        if loja == "loja_07" and time.time() > inicio + 120:
            temp = round(random.uniform(11.5, 12.5), 2)  # anomalia
        payload = json.dumps({"loja": loja, "temp": temp, "ts": time.time()})
        client.publish(f"friocerto/abc/{loja}/temperatura", payload, qos=1)
    print("publicado", time.strftime("%H:%M:%S"))
    time.sleep(2)