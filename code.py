def hanoi( source, dest, extra, n ):
    if n==1:
        print "move disk from %s to %s" % ( source, dest )
        return
    hanoi( source, extra, dest, n-1)
    print "move disk from %s to %s" % ( source, dest )
    hanoi( extra, dest, source, n-1)
    
def main():
    n = input( "Number of disks : " )
    hanoi( "A", "B", "C", n )
        
main()
