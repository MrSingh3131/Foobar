src = 0
des = 1
visited =[0 for i in range (64)]
count=0
ans=[src,"null"]
def possible_values(num):
  x = int(num/8)
  y = num-(x*8)
  x_moves = [1,-1,-1,1,2,-2,-2,2]
  y_moves = [2,-2,2,-2,1,-1,1,-1]
  for i in range(8):
    new_x = x+x_moves[i]
    new_y = y+y_moves[i]
    if new_x>=0 and new_x<8 and new_y>=0 and new_y<8:
      n=(new_x)*8+new_y
      if (n==des):
        return 1
      if visited[n] != 1:
        visited[n] = 1
        ans.append(n)
  return 0

while(True):
  if ans[0] == 'null':
    ans.pop(0)
    ans.append('null')
    count +=1
  else:
    num = ans[0]
    ans.pop(0)
    final = possible_values(num)
    if final == 1:
      count+=1
      print(count)
      break
