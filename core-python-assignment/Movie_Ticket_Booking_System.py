def ava_seat(n,b):
    ava=[]
    for i in range(1,n+1):
        if i not in b:
            ava.append(i)
    return ava
def book_seat(n,s,b):
    if s<=n and s not in b:
        b.append(s)
def cancel_seat(n,s,b):
    if s<=n and s in b:
        b.remove(s)
size=int(input('total number of seats:'))
booked=list(map(int,input('already booked seats').split()))
book=int(input('booking seat:'))
cancel=int(input('cancelling seat:'))
book_seat(size,book,booked)
cancel_seat(size,cancel,booked)
print('Available seats:',ava_seat(size,booked))