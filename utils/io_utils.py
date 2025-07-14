import os
import pickle 
def guardar_datos(nombre_archivo, datos):
    """
    Recibe un string nombre_archivo y los datos, en un formato de iterable.
    crea un carpeta y escribe los datos en formato pckl
    """
    os.makedirs(os.path.dirname(nombre_archivo),exist_ok=True)
    with open(nombre_archivo, "wb") as f:
        pickle.dump(datos, f)
def cargar_datos(nombre_archivo):
    """
    Dado a un archivo, carga los datos dentro de un archivo pckl y los devuelve 
    en el formato que previamente fue guardado
    si no encontro el archivo, retorna nada
    """
    try:
        with open(nombre_archivo, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None
