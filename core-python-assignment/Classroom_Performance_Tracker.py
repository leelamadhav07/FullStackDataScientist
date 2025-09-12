def cal_avg(mark):
    return round(sum(mark)/len(mark),2)
students={}
N=int(input('no. of students:'))
for i in range(N):
    name=input('name:')
    mark=list(map(int,input(f'marks of {name} with space:').split()))
    students[name]=mark
avg_m={}
for name,mark in students.items():
    avg_m[name]=cal_avg(mark)
top=max(avg_m,key=avg_m.get)
print("Average Marks of each student:",avg_m)
print(f'Top perfomer:{top}')