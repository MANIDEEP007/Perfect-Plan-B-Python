def tower(n,src,dest,aux):
    if n==1:
        print("Move disk 1 from",src,"To",dest)
    else:
        tower(n-1,src,aux,dest)
        print("Move disk",n,"From",src,"To",dest)
        tower(n-1,aux,dest,src)
n = 4 #Number of Disks
tower(n,'A','B','C')
