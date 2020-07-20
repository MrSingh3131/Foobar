# This question was real head scratching and required a lot of research to be done by the same. The research included the understanding of orbit-stablizer theorem.
# This theorem further included two concepts one of Burnside lemma and one of stablizer.
# Moreover I took a little inspiration to code this from the internet itself.
#
# So first of all lets look into what exactly the problem is.
# The problem at hand is we need to shift all rows and columns for each permutation of state to find out unique matrices and sum them up. As you can already feel it requires a lot of permutation and calculations.
# SO we can conclude to solve it, brute force can't exactly be the way and hence we shift to mathematical theorems and concepts. Here, this problem lies under Combinatorics according to me.
#
# Now first let us see what Burnside's lemma or Orbit counting theorem states.
# It states that for a given matrix the total number of distinct states = sigma(m^gcd(i,N)/N) where i ranges from 0 to N and N is the number of cells in matrix and M is the total number of states.
#
# Now, in this case, we need to solve for different combinations of same matrix obtained from shifting rows and columns. For this problem, in my research, I found that it
# will be better to split matrices up by partitioning via rows and columns. For eg. if we have 10 rows then one partition will be of all 10 together other will be (1,9) i.e 2 partitions or (1,1,8) i.e three partitions etc.
# and hence we will be partioning rows and columns for the matrix and for each combination of such partitions we will be solving the equation.
#
#
# Once the partition is done there comes the role of stablizer. Stablizer basically gives out the unique combinations of matrix, i.e., for which combination how many distinct matrices we can have.
# The formula of stablizer is fairly simple for one matrix input i.e., Stablizer or Stab = n!/n
# but when we give the partition as list it differs a bit as follows
# In case of lets say 10. The stablizer = factorial(10)/10
#
# In case of lets say (1,9). The stablizer = factorial(10) / (1*9)
#
# in case of lets say (1,1,8). the stablizer = factorial(10)/(1*1*8*factorial(2)).    Here we did a 2 factorial because 2 digits were same.
#
#
#
# once the stablizer is calculated now comes the role of Orbit stablizer theorem.
# This theorem states that
# |G(x)| = |O(x)|*|Stab(x)|
# here, G is the total number of distinct combinations. In our case,G is the answer.
# Stab is the stablizer
# and O is the orbit counting theorem or burnside lemma
#
#
# we have already discussed the formula for stablizer.
# Moving on to Orbit counting theorem, the formula is sigma(m^gcd(i,N)/N)
# Here, N is the number of cells in matrix which means rows * columns. But, in our case, we have the same matrix with all permutations of shifted rows and columns.
# So, permutation all the rows becomes total of factorial(rows) and all columns become factorial(columns).
# Hence, N = factorial(rows)*factorial(columns)
#
# The m in the formula here is the number of states which is provided by s in our code.
# and gcd of (i,n) is basically the total gcd of the array of partitioned rows and partitioned columns.
#
# so the final formula becomes,
# required count = (|Stab(x)|*(s^sum of gcd of array of each partition))/(factorial(rows)*factorial(columns))
# which gives count  = (Stablizer of partition of row * stablizer of partion of column * (s^sum of gcd of array of each partition))/(factorial(rows)*factorial(columns))
#
# The links used by me to understand the concepts were
# Link 1 = http://www.math.lsa.umich.edu/~kesmith/OrbitStabilizerTheorem-ANSWERS.pdf
# Link 2 = https://www.geeksforgeeks.org/orbit-counting-theorem-or-burnsides-lemma/
#
# Having a basic concept in mind lets move on to the code.
#
# Importing the necessary files
from math import factorial
from collections import Counter
from fractions import gcd

def cycle_count(c, n): # this is basically our stablizer  or cycle count formula
    stab=factorial(n) # factorial of n
    for a, b in Counter(c).items(): # counter counts and makes dictionary of each element and hence (1,1,8) becomes {1:2,8:1}
        stab//=(a**b)*factorial(b) # when we divide, it becomes fatorial(n)/(1^2)(factorial(2)). which is actually factorial(n)/(1*1*factorial(2))
        # and in second iteration it becomes factorial(n)/(1*1*factorial(2)*8*factorial(1)) which is exactly the calculation we need as discussed above.
    return stab

def cycle_partitions(n, i=1): # this is the code to generate all the possible partions of a row or column.
    A = []
    A.append([n])
    for i in range(i, n//2 + 1):
        for p in cycle_partitions(n-i, i):
            p.append(i)
            A.append(p)
    return A

#our main driver code
def solution(w, h, s):
    ans=0
    for row_part in cycle_partitions(w): # creating partition array of the rows
        for col_part in cycle_partitions(h): # creating partition array of the columns
            final_stablizer=cycle_count(row_part, w)*cycle_count(col_part, h) #for the combination of each element of row partiton and column partiton we find out the stablizer or cycle count and multiply them
            a=[]
            for i in row_part:
                for j in col_part:
                    a.append(sum([gcd(i,j)])) #array of gcd of each partition
            summ=sum(a) #total of the array of gcd obtained above
            ans+=final_stablizer*(s**summ) #this is out final formula obtained from orbit-stablizer theorem except the division part
    return str(ans//(factorial(w)*factorial(h))) # the final division is done here and hence the answer required is obtained.
