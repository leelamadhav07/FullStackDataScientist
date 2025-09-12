tot=[]
def fare(trip):
    base=50
    dist=10
    j=1
    for i in trip:
        a=50+(i*10)
        tot.append(a)
        print(f'Trip {j}:${a}')
        j+=1
    return sum(tot)
trip=list(map(int,input('enter trips: ').split()))
print(f'Total fare: ${fare(trip)}')s