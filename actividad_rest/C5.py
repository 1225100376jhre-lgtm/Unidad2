import requests

print("Jairo Haziel Rosas Enriquez")

def obtener_clima(latitud, longitud):
    url = "https://api.open-meteo.com/v1/forecast"

    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,wind_speed_10m"
    }

    r = requests.get(
        url,
        params=parametros,
        timeout=10
    )

    r.raise_for_status()

    return r.json()["current"]


ciudades = [
    ("Queretaro", 20.59, -100.39),
    ("Ciudad de Mexico", 19.43, -99.13),
    ("Guadalajara", 20.67, -103.35)
]

print()
print("Ciudad              Temperatura     Viento")
print("-" * 50)

for nombre, latitud, longitud in ciudades:
    try:
        clima = obtener_clima(latitud, longitud)

        print(
            f"{nombre:<20} "
            f"{clima['temperature_2m']:<15} "
            f"{clima['wind_speed_10m']}"
        )

    except requests.exceptions.RequestException as e:
        print(nombre, "- Error:", e)