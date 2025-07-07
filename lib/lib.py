from quplots import electron,plots
import time 
start=time.time()
e=electron(5,4,0,2)
e.compute_radial()
print(f"Tiempo de calculo  radiial:{time.time()-start:.8f} s") #0.00099969