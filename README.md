# ChangeFileDatesfromGoogleCloud
AVISO: Estos scripts solo funcionan en Windows.

Lo que se pretende con este proyecto es, una vez descargados los videos y fotos de Google Fotos (fotos en cualquier formato y videos MP4), cambiar la fecha de creación de cada archivo por la de captura o creación del medio, para que al subirlos a otro servicio de nube las fotos y videos queden ordenados por fecha correcta

1. Una vez descomprimido el .zip de la copia de Google Fotos (en el repostorio he dejado "takeout-XXXXXXXXXXX.zip" listo como archivo de pruebas) buscamos y eliminamos todos los archivos "json" en el buscador de windows
![image](https://github.com/torbol/ChangeFileDatesfromGoogleCloud/assets/99366541/9e43541f-fa01-4ff5-a42f-1f84da667602)

2. Ejecutamos el script "eliminadorcarpetasvacias.py" con doble click (debe estar en la carpeta donde están todas las subcarpetas con las fotos, como en las carpetas de ejemplo) y se eliminarán las carpetas vacías, en la carpeta de ejemplo, "Carpeta 1" y "Carpeta 2"
![image](https://github.com/torbol/ChangeFileDatesfromGoogleCloud/assets/99366541/6aaa8800-1b69-4eb7-84d8-60a5eeb7d172)


3. Por último, lanzamos el script "modifiedatecreatedate.py" para cambiar las fechas de acceso, modificación y creación del archivo y poner la que viene en los metadatos como "Fecha de captura" o "Creación de medio" si es MP4

Fechas sin modificar:
![image](https://github.com/torbol/ChangeFileDatesfromGoogleCloud/assets/99366541/3f18abc7-b3fc-46e2-bd73-ab8156f1400e)
![image](https://github.com/torbol/ChangeFileDatesfromGoogleCloud/assets/99366541/0f86f0b9-a295-4dc2-8369-688f09bc40f6)



Fechas tras haber lanzado el script:
![image](https://github.com/torbol/ChangeFileDatesfromGoogleCloud/assets/99366541/9e351063-2682-45b6-a070-c6dd38b9f04b)
