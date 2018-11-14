from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [8, 9, 7, 1]
    print("<P:%d> %s" % (rank, data))
else:
    data = None
    print("<P:%d> %s" % (rank, data))

data = comm.bcast(data, root=0)
print("<P:%d> %s" % (rank, data))
