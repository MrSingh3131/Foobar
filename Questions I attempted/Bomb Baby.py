def solution(x, y):
    # Your code here
    x=int(x)
    y=int(y)
    if(y>x):
      temp = x
      x=y
      y=temp
    count = 0
    while(x!=y and y>0):
        if (y ==1):
            count += x-1
            break
        else:
            count += x//y
            temp = y
            y = x%y
            x=temp
    if(y==1):
      return str(count)
    return "impossible"
