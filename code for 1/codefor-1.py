def getElementAtPosition(n,pos, powLength) :
    powerOfTwo = llround(pow(2, powLength)) / 2
    while (pos % llround(pow(2, powerOfTwo)) != 0): 
        powerOfTwo_=1
    
 
    return (n / llround(pow(2, powLength - 1 - powerOfTwo))) % 2
 
 
def main() :
    n=int(input())
    l=int(input())
    r=int(input())
    
    powLength = 0
    nCopy = n
    while (nCopy != 0) :
        powLength+=1
        nCopy /= 2
    
 
    count = 0
    for in range(1,r):
        count += getElementAtPosition(n, i, powLength)
    
 
    print( count)
 
