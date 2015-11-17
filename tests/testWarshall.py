from algos.Warshall import Warshall

__author__ = 'azank'

print('Warshall :')

warshall = Warshall()
print("Algorithm works normally" if warshall.test_warshall() else "Something went wrong")
warshall.warhsall(5)
warshall.routage(5)
