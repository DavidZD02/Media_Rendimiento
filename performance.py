import time
import cy_planeta
import py_planeta

planeta = py_planeta.Planet()
planeta2 = cy_planeta.Planet()

init_time = time.time()

py_planeta.step_time(planeta, 1000, 3000)
fin_time = time.time()

total_time_python = fin_time - init_time
print("Tiempo total de python: ",total_time_python)

init_time = time.time()
cy_planeta.step_time(planeta2, 1000, 3000)
fin_time = time.time()

total_time_cython = fin_time - init_time
print("Tiempo total de Cython: ", total_time_cython)

print(f"Cython es {total_time_python/total_time_cython} veces más rapido que Python")
