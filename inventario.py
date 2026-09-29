inventario = [
	{"hostname": "Core-SW01", "ip": "10.0.0.1", "status": "up"},
	{"hostname": "Dist-SW02", "ip": "10.0.0.2", "status": "down"},
	{"hostname": "Access-SW03", "ip": "10.0.0.3", "status": "up"},
	{"hostname": "Edge-R01", "ip": "172.16.1.1", "status": "down"}
]
print("Hostname")
# Imprimir todos los hostname 
for h in inventario:
	print(h["hostname"])
print()

print("IPS")
# Imprimir todas las IPS 
for i in inventario:
	print(i["ip"])
print()

print("Dispo en down")
# Imprimir todos los que estan en down
for d in inventario:
    if d["status"] == "down":
        print(d["hostname"])