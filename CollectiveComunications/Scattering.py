from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [5, 7, 8]
    print("<P:%d> %s" % (rank, data))
elif rank == 1:
    data = None
    print("<P:%d> %s" % (rank, data))
elif rank == 2:
    data = None
    print("<P:%d> %s" % (rank, data))
data = comm.scatter(data, root=0)
print("<P:%d> %s" % (rank, data))
