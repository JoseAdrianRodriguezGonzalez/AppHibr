from class_electron import electron
from class_electron import plot
from class_electron import hibrydization
import time

start=time.time()
e=electron()
e.radial(2,5,4)
print(f"Tiempo de calculo  radiial:{time.time()-start:.8f} s") #0.00099993
#p.plot_spherical_real(e.RealSpherical(1,0))
#p.plot_spherical_imaginary(e.ImaginarySpherical(2,-1))
#p.plot_wf_2d(e.normalized_wf(500,2,1,-1))
#p.plot_wf_3d(e.normalized_wf3D(3,2,0))
#p.plot_sp(e.Cartesian_definition())
#p.plot_sp2(e.Cartesian_definition())
#p.plot_sp3(e.Cartesian_definition())
#p.plot_sp2d(e.Cartesian_definition())
#p.plot_sp3d(e.Cartesian_definition())
#p.plot_sp3d2(e.Cartesian_definition())