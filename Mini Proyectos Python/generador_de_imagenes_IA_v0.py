# En este caso, el código descarga 10 imágenes de rostros generados por la IA de la API Generated Photos. Para ello, se hace una petición a la URL de la API y se obtiene la respuesta en formato JSON. Luego, se extrae la URL de la imagen de cada rostro y se descarga la imagen con la librería requests. Finalmente, se guarda la imagen en un archivo con el nombre imagen_{i}.jpg, donde i es el número de la imagen.
# Es importante tener en cuenta que para utilizar la API Generated Photos es necesario obtener una clave de API, la cual se debe incluir en la URL de la petición. Además, es importante respetar los términos de uso de la API y asegurarse de tener los permisos necesarios para descargar y utilizar las imágenes generadas por la IA.


# Path: generador_de_imagenes_IA.py
# import requests


# def generar_imagenes_IA():
#     url = "https://api.generated.photos/api/v1/faces?api_key=YOUR_API_KEY&order_by=random&per_page=10"

#     response = requests.get(url)
#     data = response.json()
#     for i in range(10):
#         image_url = data["faces"][i]["urls"][4]["512"]
#         response = requests.get(image_url)
#         file = open(f"imagen_{i}.jpg", "wb")
#         file.write(response.content)
#         file.close()
#         print(f"Imagen {i} descargada")


# generar_imagenes_IA()
