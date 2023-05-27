#mapquest-prueba2-valentina-javier.py
# importar librerias 
#(urllib.parse) proporciona funciones para manipular URLs y sus componentes, para descomponerlas o construirlas.
import urllib.parse
import requests

#URL api
main_api = "https://www.mapquestapi.com/directions/v2/route?"
#Key proporcinada desde Mapquest Key

key = "fXI23yakIqIHqGDQgy2Cnk28VSuLiI1z" 
#implementacion codigo ciudad de origen y destino 
while True:
    orig = input("Ciudad de Origen: ")
    if orig == "quit" or orig == "q":

            break
    dest = input("Ciudad de Destino: ")
    if dest == "quit" or dest == "q":
            break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

    json_data = requests.get(url).json()
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("*********************************************")
        print("Dirección de Origen  " + (orig) + " Destino " + (dest))
        print("Tiempo Total de Viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilometros: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

        print("*********************************************")