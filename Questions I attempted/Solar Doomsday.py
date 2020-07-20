def solution(area):
   # Your code here
   ans=[]
   i=1
   def closest_square(n):
       a=int((n/2)+1)
       length = len(str(n))
       if (length == 1):
           i=1
       elif(length == 2):
           i = 3
       elif(length == 3):
           i = 9
       elif(length == 4):
           i = 31
       elif(length == 5):
           i = 99
       elif( length == 6):
           i = 316
       else:
           i = 999
       # for j in range (i,a+1):
       #     k = j*j
       #     if k == n:
       #         return k
       #     if k >n:
       #         return (j-1)*(j-1)

       while (i<=a):
         mid = int((i+a)/2)
         small = mid*mid
         big = (mid+1)*(mid+1)
         if (small <= n and big > n):
           break
         else:
           if(small > n):
             a = mid
           else:
             i = mid
       return small


   while(area>0):
       n = closest_square(area)
       ans.append(n)
       area = area - n
   return ans
