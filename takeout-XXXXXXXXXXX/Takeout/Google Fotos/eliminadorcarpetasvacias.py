# Python program to check whether 
# the directory empty or not 


import os 

# path of the directory 
path = os.getcwd()
print("La ruta es: " + path)

# Getting the list of directories 
dir = os.listdir(path)

# Checking if the list is empty or not
for carpeta in dir:
    if carpeta == "eliminadorcarpetasvacias.py":
        pass
    elif os.listdir(carpeta) == []:
        os.rmdir(carpeta)
        print(carpeta + " - Empty directory deleted")
