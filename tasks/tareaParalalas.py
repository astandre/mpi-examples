from mpi4py import MPI
import sys
import time
from random import randint


comm = MPI.COMM_WORLD
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

if rank == 0:
	cadena = "UTPL"
	print("Enviando a <2> %s" % cadena)
	comm.send(cadena, dest=2, tag=11)
elif rank == 1:
	n1 = randint(0, 10)
	print ("Numero generado %d" % n1)
	n2 = randint(0, 10)
	print ("Numero generado %d" % n2)
	suma = n1 + n2
	print("Enviando a <2> %d "% suma )
	comm.send(suma, dest=2, tag=11)
elif rank == 2:
	cadena = comm.recv(source=0, tag=11)
	print("Recibido de <0> %s"% cadena)
	suma = comm.recv(source=1, tag=11)
	print("Recibido de <1> %d"% suma)
	print("Data: %s %d en el procesador %s" %(cadena,suma,name))
