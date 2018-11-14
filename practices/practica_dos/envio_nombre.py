from mpi4py import MPI
import sys
import time


comm = MPI.COMM_WORLD
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
#name = MPI.Get_processor_name()


#Programa que envia un nombre de un proceso a otro, un caracter a la vez
if rank == 0:
	name = "Mark Zucaritas."
	for i in range(0,len(name)):
		data = name[i]
		#print("<S:%d> -> %s" %(rank,data))
		comm.send(data, dest=1, tag=11)
elif rank == 1:
	final_name = ""
	while True:
		data = comm.recv(source=0, tag=11)
		if data is ".":
			break
		print("<R:%d> <- %s" %(rank,data))
		final_name +=data
	print("Name: "+final_name)
