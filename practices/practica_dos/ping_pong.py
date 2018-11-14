from mpi4py import MPI
import sys
import time


comm = MPI.COMM_WORLD
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()


#Programa que envia un mensaje de un proceso al otro y viceversa
state = True
while True:
	time.sleep( 1)
	if rank == 0:
		if state:
			#time.sleep( 1)
			comm.send("Ping", dest=1, tag=11)			
			state = False
		else:
			data = comm.recv(source=1, tag=11)
			print("<P:%d> %s" %(rank,data))
			state = True
	elif rank == 1:
		if not state:
			comm.send("    Pong", dest=0, tag=11)
			state = True
		else:
			data = comm.recv(source=0, tag=11)
			print("<P:%d> %s" %(rank,data))
			state = False
