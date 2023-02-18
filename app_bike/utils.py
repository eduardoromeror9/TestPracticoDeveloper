import requests

def obtener_datos():
    url = 'http://api.citybik.es/v2/networks/bikesantiago'
    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()
        return datos
    else:
        return None