from itertools import combinations
def solution(num_buns, num_required):
    # Your code here
    # Earlier i never commented my code but from this challenge i will be
    # commenting my code and telling my approach too

    #this is a permutaion and combination problem. In permutation we get all possible outcomes
    # but in combinations we get only unique ones irrespective of position . In this one we will be using combinatoins

    # combinations accept the list of items to iterate and total length
    # in our case the list of items will be a list of total keys to be distributed

    # total numbers of keys needed will be

  copy_of_key = num_buns-num_required+1 #it means we find out how many bunnies will have same key
  ans=[]
  for x in range(num_buns):
    ans.append([])
  for i,j in enumerate(combinations(range(num_buns),copy_of_key):
    for k in j:
      ans[k].append(i)

  return ans
