#
# Problem - The problem at hand is we have an irrational number sqrt(2) and we need to multiply it and add it for maximum 10^100 times which is too large for normal calculations. And thus we need to find out a smaller way to do the same.
#
# Solution - First of all lets understand the problem.
#  if we try to visualise the problem the equation becomes sigma or summation of floor(i*sqrt(2)) for 1<=i<=10^100 lets write it as sigma(alpha*n) where alpha is sqrt(2) and n is the number of times
#
#  This equation is called beatty sequence. And we have a theorem that states that for 1<alpha<2 if we find a beta such that (alpha)^-1 + (beta)^-1 = 1 then sigma(alpha,n) + sigma(beta,n') = sum of m natural numbers
#
#
#  Let us visualise this first and then we will move on.
#  Let us suppose we have alpha as 5 and n as 2. (hypothetical question for visualisation purpose only)
#  this means that on a number line we are talking about two values i.e 5*1 = 5 and 5*2 = 10 and we need to find the sum of these values.
#
#  There are two ways to do this.
#
#  Way 1- the natural way sigma(alpha,n) = sigma(5,2) = 5*1 +5*2 = 15
#
#
#  Way 2- we can add all numbers to maximum limit of the value of summation. In this case the max limit will be alpha*n i.e sum of all numbers till 5*2=10 and subtracting the numbers which are not covered in the jumps
#           we made in way 1. Kind of like sum of all natural numbers till 10 - sigma(beta,(leftovers of way 1))
#
#  In the above example we will follow way 1 because in way 1 our sigma(alpha,n) makes way less jumps on number line than sigma(beta,(leftover of way 1 = 10-2 = 8))
#  but consider this , if our alpha is small , then on a number line it will make higher jumps as compared to its beta counterpart,so it will take fewer computatio cycles to compute beta
#
#  Now let us say our aplha becomes small and acc to the theorem 1<alpha<2 and n is very large indeed. To find sigma(alpha*n) we take following steps
#
#  Step 1
#  find the limit of alpha i.e the max value it can take i.e alpha*n. Let us say name it as m. So m = floor(alpha*n)
#
#  Step 2
#  find if the beta counter part exists using the formula (alpha)^-1 + (beta)^-1 = 1 which becomes (beta)^-1 = 1 - (1/alpha) which becomes beta = alpha/(apha-1)
#
#  step 3
#  we know if alpha jumps n times beta jumps the leftover ones in our theorem it is denoted by n'. So calculate n' using the formula n' = total - (jumps of alpha) which gives n' = m - n where m is the max value of alpha i.e our limit of the number line and n is the jumps of alpha
#
#  step 4
#  sigma(alpha,n) = sum of all natural number m - sigma(beta,n')  {According to theorem}.
#  here m = alpha*n and n' = m-n = (alpha*n) - n = n(alpha-1)
#  we know the sum of m natural numbers = (m(m+1))/2 and m = n+n' so this becomes
#  sum of m natural numbers = (n+n')(n+n'+1)/2
#
#
#  so our final equation becomes
#  sigma(alpha,n) = (n+n')(n+n'+1)/2 - sigma(beta,n') where n' = n(alpha-1)
#
# Coding explanation ->
# here the value of n  = from 1 to x where 1<=x<=10^100. x will be defined by user basically
# and the value of alpha = sqrt(2) (we will take upto 10^100 decimals only) = 1.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
# and the value of n' = n(alpha-1) = n*(sqrt(2)-1) = n(0.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727)
# and the value of beta  = alpha/(alpha-1) {from step 2}
# this becomes beta  = sqrt(2)/(sqrt(2)-1) which on simplification becomes beta = 2+sqrt(2) = 2+alpha , in this case
# So, sigma(beta,n') = sigma(2+alpha,n') = sigma(2,n')+sigma(alpha,n'). here sigma(2,n') = (2*1)+(2*2)+(2*3)+.....+(2*n') = 2[1+2+3+...+n'] = 2[n'(n'+1)/2] = n'(n'+1)
# and hence for this case where alpha = sqrt(2) sigma(beta,n') transforms into n'(n'+1)+sigma(alpha,n')
#
# so the final equation becomes
# sigma(alpha,n) = ((n+n')(n+n'+1)/2) - sigma(beta,n') = ((n+n')(n+n'+1)/2) - (n'(n'+1)+sigma(alpha,n')) = ((n+n')(n+n'+1)/2) - n'(n'+1) -sigma(alpha,n')
# which becomes sigma(alpha,n) = ((nn+nn'+n+n'n+n'n'+n')/2) - (n'n'+n') - sigma(alpha,n') = ([nn+n'n'+2nn'+n+n' - 2(n'n'+n')]/2)- sigma(alpha,n')
# which become sigma(alpha,n) = ([nn+n'n'-2n'n'+2nn'+n+n'-2n']/2)- sigma(alpha,n') = ([nn-n'n'+2nn'+n-n']/2)- sigma(alpha,n')
# which become sigma(alpha,n) = (2nn'/2) + ((nn+n)/2) + ((-n'n'-n')/2) - sigma(alpha,n') = nn' + (n(n+1)/2) - (n'(n'+1)/2) - sigma(alpha,n')
#
# final equation for this specific solution becomes sigma(alpha,n)=nn' + (n(n+1)/2) - (n'(n'+1)/2) - sigma(alpha,n')
# In the equation we see if we define a function to compute sigma(alpha,n) we will need to call it recursively for sigma(alpha,n')
#
# and finally we need a stopping condition for recursion which can be if n <1 i.e no jump is made or sigma(alpha,0) = floor(sqrt(2)*0) = 0 hence  return 0 and on last step where n = 1, sigma(alpha,1) = floor(sqrt(2)*1) = 1. Hence we return 1 when n = 1



sqrt2_minus_one = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727 # only decimal value of alpha-1 upto 10^100 decimal places

def n_dash(n):
    # We took sqrt(2)-1 as integer and later converted in decimal in this function
    # this is because if we had kept it in decimal form i.e 0.414.... then there was a chance that in some point of calculation a digit might be considered least significant and dropped
    # in our case during trial and error we found that this happens when the decimal multiplicatin reaches upto more than 16 places after decimal
    return (sqrt2_minus_one*n)//(10**100) # the floor (or int) value for n' = n(alpha-1)

#defining the sigma(alpha,n) function
def sigma(n):
    if n == 1:
        return 1 # because sigma(sqrt(2),1) = 1

    if n < 1:
        return 0 # because no jumps made or sigma(sqrt(2),0) = 0
    return n*n_dash(n) + n*(n+1)/2 - n_dash(n)*(n_dash(n)+1)/2 - sigma(n_dash(n)) # our derived final equation

def solution(n):
    n = long(n) # we get input as string so we convert it to int
    return str(int(sigma(n))) #calling our sigma(alpha,n) function and returning the answer
