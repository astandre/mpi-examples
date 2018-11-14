from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    print("<P:%d>" % rank)
    time.sleep(5)
    comm.send("Ping", dest=1, tag=11)
else:
    print("Waiting for <P:%d>" % (rank - 1))
    data = comm.recv(source=0, tag=11)
    print("<P:%d> %s" % (rank, data))
