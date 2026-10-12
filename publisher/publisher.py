import paho.mqtt.client as mqtt
import time, random, json

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883, 60)
client.loop_start()

lojas = [f"loja_{i:02d}" for i in range(1, 15)]
cidades = ["santo_andre"] * 4 + ["sao_bernardo"] * 4 + ["sao_caetano"] * 3 + ["diadema"] * 3
cidade_da_loja = dict(zip(lojas, cidades))
seq = {loja: 0 for loja in lojas}
inicio = time.time()

while True:
    for loja in lojas:
        temp = round(random.uniform(3.0, 7.0), 2)
        if loja == "loja_07" and time.time() > inicio + 120:
            temp = round(random.uniform(11.5, 12.5), 2)  # anomalia
        seq[loja] += 1
        payload = json.dumps({"loja": loja, "temp": temp, "seq": seq[loja], "ts": time.time()})
        topico = f"friocerto/v1/abc/{cidade_da_loja[loja]}/{loja}/camara_01/sensor_{loja[-2:]}/telemetry"
        client.publish(topico, payload, qos=0)
    print("publicado", time.strftime("%H:%M:%S"))
    time.sleep(2)