def add_item(menu,n):
    menu.append(n)
def remove_item(menu,n):
    if n in menu:
        menu.remove(n)
def check_item(menu,n):
    if n in menu:
        print(f'Availability:{n} is available')
    else:
        print(f'Availability:{n} is not available')
menu=list(map(str,input('enter intial menu').split()))
add=input('add_item=')
rem=input('remove_item=')
check=input('check_item=')
add_item(menu,add)
remove_item(menu,rem)
print(f'Updated menu:{menu}')
check_item(menu,check)