# Python program to change the modification date to capture date
import os
from datetime import datetime, timezone
from win32_setctime import setctime
from win32com.propsys import propsys, pscon

# path of the directory 
path = os.getcwd()

# Getting the list of directories 
dir = os.listdir(path)

# Eliminamos de la lista de rutas los archivos eliminadorcarpetasvacias.py y modifiedatecreatedate.py
if "modifiedatecreatedate.py" in dir:
    dir.remove("modifiedatecreatedate.py")
if "eliminadorcarpetasvacias.py" in dir:
    dir.remove("eliminadorcarpetasvacias.py")

# Obtenemos los archivos de cada carpeta y lo vamos a guardar en un diccionario, donde cada carpeta será la key:
carpetayarchivos = {} # Creamos el diccionario vacío
for carpeta in dir:
    listarchivosdelacarpeta = os.listdir(carpeta)
    carpetayarchivos[carpeta] = listarchivosdelacarpeta #Guardamos la key carpeta y como valores, los archivos de cada carpeta

def dtfcfm(properties, claveprimaria, accion_dtfcfm = "Null"): 
    dt_dtfcfm = properties.GetValue(claveprimaria).GetValue() #Esta es la fecha de creación de los videos
    if accion_dtfcfm == "cambiar":
        TimeStampTransformado_dtfcfm = datetime.fromisoformat(str(dt_dtfcfm)).replace(tzinfo=timezone.utc).timestamp() #Tenemos en cuenta nuestra zona horaria con timezone.utc para que las fechas modificadas sean correctas
        return TimeStampTransformado_dtfcfm
    else:
        fc_dtfcfm = properties.GetValue(pscon.PKEY_DateCreated).GetValue() #lecura fecha creación
        fm_dtfcfm = properties.GetValue(pscon.PKEY_DateModified).GetValue()#lectura fecha modificación
        return dt_dtfcfm, fc_dtfcfm, fm_dtfcfm

    
def fecharchivos(accion): #Pasaremos un parámetro, o leer o cambiar
    for key, value in carpetayarchivos.items():
        for archivo in value:
            rutarelativadelarchivo = os.path.join(key, archivo)
            properties = propsys.SHGetPropertyStoreFromParsingName(os.path.join(path, rutarelativadelarchivo))
            if ".mp4" in archivo:
                if accion == "leer":
                    dt, fc, fm = dtfcfm(properties, pscon.PKEY_Media_DateEncoded)
                    print("{}:\tcapturedate:{}\tcreatedate:{}\tmodifdate:{}".format(archivo, str(dt), str(fc), str(fm)))
                if accion == "cambiar":
                    TimeStampTransformado = dtfcfm(properties, pscon.PKEY_Media_DateEncoded, accion)
                    os.utime(rutarelativadelarchivo, (TimeStampTransformado, TimeStampTransformado)) #(rutadelarchivo, (fechacceso, fechamodificion))
                    setctime(rutarelativadelarchivo, TimeStampTransformado)
            else:
                if accion == "leer":
                    dt, fc, fm = dtfcfm(properties, pscon.PKEY_ItemDate)
                    print("{}:\tcapturedate:{}\tcreatedate:{}\tmodifdate:{}".format(archivo, str(dt), str(fc), str(fm)))
                if accion == "cambiar":
                    TimeStampTransformado = dtfcfm(properties, pscon.PKEY_ItemDate, accion)
                    os.utime(rutarelativadelarchivo, (TimeStampTransformado+1200, TimeStampTransformado+1200)) #(rutadelarchivo, (fechacceso, fechamodificion))
                    setctime(rutarelativadelarchivo, TimeStampTransformado)

# Ahora vamos a proceder a leer las fechas de captura, modificación y creación de cada archivo:
#fecharchivos("leer") #Descomentar si queremos ver las fechas de todos los archivos de las subcarpetas
fecharchivos("cambiar") #Descomentar esta linea SI QUEREMOS CAMBIAR LAS FECHAS POR LAS DE CREACIÓN!!!!
