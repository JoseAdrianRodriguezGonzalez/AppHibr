from model.electron_model import (
    calcular_radial,calcular_spherical_real,
    calcular_spherical_imag,calcular_wf_2d,calcular_wf_3d,
    mostrar_cartesian
    )
from utils.validator import validar_entradas
from utils.message import mostrar_error
from lib.class_electron import plot

def mostrar_radial(n,l,m):
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
    try:
        p=plot()
        n,l,m=validar_entradas(n,l,m)
        datos=calcular_spherical_real(l,m)
        p.plot_spherical_real(datos)
    except Exception as ex:
        mostrar_error("Error de calculo",str(ex))
def mostrar_imag_esfericos(n,l,m):
    try:
        p=plot()
        n,l,m=validar_entradas(n,l,m)
        datos=calcular_spherical_imag(l,m)
        p.plot_spherical_imaginary(datos)
    except Exception as ex:
        mostrar_error("Error de calculo",str(ex))
def mostrar_wf_2d(n,l,m):
    try:
        p=plot()
        n,l,m=validar_entradas(n,l,m)
        datos=calcular_wf_2d(n,l,m)
        p.plot_wf_2d(datos)
    except Exception as ex:
        mostrar_error("Error de calculo",str(ex))
def mostrar_wf_3d(n,l,m):
    try:
        p=plot()
        n,l,m=validar_entradas(n,l,m)
        datos=calcular_wf_3d(n,l,m)
        p.plot_wf_3d(datos)
    except Exception as ex:
        mostrar_error("Error de calculo",str(ex))
def hibridaciones(func):
    try:
        mostrar_cartesian(func)
    except Exception as ex:
        mostrar_error("Error de calculo",str(ex))