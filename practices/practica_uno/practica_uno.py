from mpi4py import MPI
import sys

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()
# Hola mundo en paralelo
print("Hola, soy el proceso %d de %d en el equipo %s.\n" % (rank, size, name))