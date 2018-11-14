from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = 1
    print("<P:%d> [DATA] %s" % (rank, data))
elif rank == 1:
    data = 7
    print("<P:%d> [DATA] %s" % (rank, data))
elif rank == 2:
    data = 8
    print("<P:%d> [DATA] %s" % (rank, data))

data = comm.reduce(data, root=0, op=MPI.PROD)
print("<P:%d> %s" % (rank, data))
