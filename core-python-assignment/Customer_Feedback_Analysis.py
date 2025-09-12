def anal(rate):
    if not rate:
        return 0
    c=0
    for i in rate:
        if i>=4:
            c+=1
    return (c/len(rate))*100
rate=list(map(int,input('rating(1-5): ').split()))
print(f'Positive Feedback:{anal(rate)}%')
