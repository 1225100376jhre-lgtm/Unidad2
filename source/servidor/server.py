"""
Mi primer servidor web Flask y Python
Autor: Jairo Rosas Enriquez
Fecha: 30 de Septiembre

"""

from flask import Flask
app = Flask(__name__)

inventario = [
	{"hostname": "Core-SW01", "ip": "10.0.0.1", "status": "up"},
	{"hostname": "Dist-SW02", "ip": "10.0.0.2", "status": "down"},
	{"hostname": "Access-SW03", "ip": "10.0.0.3", "status": "up"},
	{"hostname": "Edge-R01", "ip": "172.16.1.1", "status": "down"}
]



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/<nombre>')
def saludo(nombre):
	return f"<h1>Hola {nombre}</h1>"

@app.route('/dispositivo/<device>')
def buscar_dispositivo(device):
    for e in inventario:
        if e["hostname"].lower() == device.lower():
            return f"<h1>{e['hostname']}</h1><p>IP: {e['ip']}</p><p>Estatus: {e['status']}</p>"
            
    return "<h1>No encontrado</h1>", 404



if __name__ == "__main__":
	app.run(debug=True, port=5013)