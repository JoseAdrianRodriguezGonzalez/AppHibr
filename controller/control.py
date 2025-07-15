from model import (
    calcular_radial,calcular_spherical_real,
    calcular_spherical_imag,calcular_wf_2d,calcular_wf_3d,
    mostrar_cartesian
    )
from utils import validar_entradas,mostrar_error
from lib.class_electron import plot

def mostrar_radial(n,l,m):
    """
    Recibe los numeros cuanticos, los valida
    y obtiene los datos en base a los numeros por medio de la funcion calcular_radial
    y grafica los datos
    """
    try:
        p=plot()
        n,l,m=validar_entradas(n,l,m)
        #Esta seccion se corregira con la libreria bien implementada, ya que esto hace doble calculo
        #innecsario
        datos=calcular_radial(n,l)
        p.plot_radial_(2,n,l)
    except Exception as ex:
        mostrar_error("Error de calculo",str(ex))
def mostrar_real_esfericos(n,l,m):
    """
    Recibe los numeros cuanticos,los valida y obtiene los datos en base
    a los numeros por medio de la 
    funcion calcular_spherical_real y grafica los datos
    """
    try:
        p=plot()
        n,l,m=validar_entradas(n,l,m)
        datos=calcular_spherical_real(l,m)
        p.plot_spherical_real(datos)
    except Exception as ex:
        mostrar_error("Error de calculo",str(ex))
def mostrar_imag_esfericos(n,l,m):
    """
    Recibe los numeros cuanticos,los valida y obtiene los datos en base a los
    numeros por medio de la funcion calcular_spherical_imag y grafica los datos
    """
    try:
        p=plot()
        n,l,m=validar_entradas(n,l,m)
        datos=calcular_spherical_imag(l,m)
        p.plot_spherical_imaginary(datos)
    except Exception as ex:
        mostrar_error("Error de calculo",str(ex))
def mostrar_wf_2d(n,l,m):
    """
    Recibe los numeros cuanticos,los valida y obtiene los datos en base a los
    numeros por medio de la funcion calcular_wf_2d y grafica los datos
    """
    try:
        p=plot()
        n,l,m=validar_entradas(n,l,m)
        datos=calcular_wf_2d(n,l,m)
        p.plot_wf_2d(datos)
    except Exception as ex:
        mostrar_error("Error de calculo",str(ex))
def mostrar_wf_3d(n,l,m):
    """
    Recibe los numeros cuanticos,los valida y obtiene los datos en base a los
    numeros por medio de la funcion calcular_wf_3d y grafica los datos
    """
    try:
        p=plot()
        n,l,m=validar_entradas(n,l,m)
        datos=calcular_wf_3d(n,l,m)
        p.plot_wf_3d(datos)
    except Exception as ex:
        mostrar_error("Error de calculo",str(ex))
def hibridaciones(func):
    """
    Recibe una funcion como argumento y se le pasa a la funcion de mostrar_cartesian
    """
    try:
        mostrar_cartesian(func)
    except Exception as ex:
        mostrar_error("Error de calculo",str(ex))