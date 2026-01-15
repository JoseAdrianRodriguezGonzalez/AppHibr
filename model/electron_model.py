from lib.class_electron import electron
from utils import cargar_datos,guardar_datos
def calcular_radial(n,l):
    """
    Le pasa los numeros cuanticos n,l.
    Se intenta cargar los datos, si no existe, entonces se calculan con la funcion
    del radial por medio del objeto electron() en formato pkl
    y con el numero n,l asociado. Estos datos se guardan en la carpeta data
    """
    e=electron()
    radial_file = f"data/radial_{n}_{l}.pkl"
    radial_data = cargar_datos(radial_file)
    if radial_data is None:
        radial_data = e.RealSpherical(n, l)
        guardar_datos(radial_file, radial_data)
    return radial_data
def calcular_spherical_real(l,m):
    """
    Le pasa los numeros cuanticos l,m.
    Se intenta cargar los datos, si no existe, entonces se calculan con la funcion
    de la parte real esferica por medio del objeto electron() en formato pkl
    y con el numero l,m asociado. Estos datos se guardan en la carpeta data
    """
    archivo = f"data/spherical_real_{l}_{m}.pkl"
    e=electron()
    datos = cargar_datos(archivo)
    if datos is None:
        datos = e.RealSpherical(l, m)
        guardar_datos(archivo, datos)
    return datos
def calcular_spherical_imag(l,m):
    """
    Le pasa los numeros cuanticos l,m.
    Se intenta cargar los datos, si no existe, entonces se calculan con la funcion
    de la parte imaginaria esferica por medio del objeto electron() en formato pkl
    y con el numero l,m asociado. Estos datos se guardan en la carpeta data
    """
    archivo = f"data/spherical_imaginary_{l}_{m}.pkl"
    datos = cargar_datos(archivo)
    e=electron()
    if datos is None:
        datos = e.ImaginarySpherical(l, m)
        guardar_datos(archivo, datos)
    return datos
def calcular_wf_2d(n,l,m):
    """
    Le pasa los numeros cuanticos n,l,m.
    Se intenta cargar los datos, si no existe, entonces se calculan con la funcion
    de la funcion psi de onda en 2d por medio del objeto electron() en formato npy
    y con el numero l,m asociado. Estos datos se guardan en la carpeta data
    """
    e=electron()
    wf_2d_file = f"data/wf_2d_{n}_{l}_{m}.npy"
    wf_2d = cargar_datos(wf_2d_file)
    if wf_2d is None:
        wf_2d = e.normalized_wf(500, n, l, m)
        guardar_datos(wf_2d_file, wf_2d)
    return wf_2d
def calcular_wf_3d(n,l,m):
    """
    Le pasa los numeros cuanticos n,l,m.
    Se intenta cargar los datos, si no existe, entonces se calculan con la funcion
    de la funcion psi de onda en 3d por medio del objeto electron() en formato npy
    y con el numero l,m asociado. Estos datos se guardan en la carpeta data
    """
    e=electron()
    wf_3d_file = f"data/wf_3d_{n}_{l}_{m}.npy"
    wf_3d = cargar_datos(wf_3d_file)
    if wf_3d is None:
        wf_3d = e.normalized_wf3D(n, l, m)
        guardar_datos(wf_3d_file, wf_3d)
    return wf_3d

def mostrar_cartesian(func):
    """
    Le pasa como parametro una funcion, busca si existe los datos,buscamos el archivo  y
    si no existen, se genera una region x,y,z; se guarda en un formato pkl 
    y se le pasa a la funcion
    """
    archivo = "data/cartesian.pkl"
    e=electron()
    datos = cargar_datos(archivo)
    if datos is None:
        datos = e.Cartesian_definition()
        guardar_datos(archivo, datos)
    func(datos)
