from itertools import permutations
def get_time(nodes,matrix):
  #the bulkhead door is the end
  end=len(matrix)-1
  time =0
  #adding time from start to first bunny and from last bunny to bulkhead door
  time += matrix[0][nodes[0]]
  time += matrix[nodes[-1]][end]
  # adding time between each bunny to calculate exact total time.
  for i in range(len(nodes)-1):
    time += matrix[nodes[i]][nodes[i+1]]
  return time



def solution(times, time_limit):
  #Bellman Ford to find shortest paths between each node, also it can deal with negative weights.

  #bellman ford can also detect negative cycles. Our advantage is if a negative cycle occurs we know the negative increases.
  # so the bulkhead door can remain open for as long as we want hence all rabbits can be save.
  def BellmanFord():
    for src in range(V):
      new_matrix[src][src] = 0
      for _ in range(V - 1):
        for u in range(V):
          for v in range(V):
            #if we find a smaller time than given in matrix we need to replace it
            if new_matrix[src][u] != INF and new_matrix[src][u] + times[u][v] < new_matrix[src][v]:
              new_matrix[src][v] = new_matrix[src][u] + times[u][v]
      #checking if negative weight cycle exist
      for u in range(V):
        for v in range(V):
          if new_matrix[src][u] != INF and new_matrix[src][u] + times[u][v] < new_matrix[src][v]:
            #return false if negative weight cycle found
            return False
    return True


  V = len(times) #no. of vertices
  INF = float("Inf") #initializing an infinity variable
  new_matrix = [[INF for _ in range(V)] for _ in range(V)] #initialising each weight to infinity

  #if there is only starting and ending row. This means no bunny needs to be saved and hence we can return empty string.
  if len(times)<=2:
      return []

  #calling the bellman ford
  result = BellmanFord()
  #we have a new_matrix matrix popualted with minimum new_matrix

  # Total bunnies we have
  total_bunnies = len(times)-2
  # bunny_row is the corresponding row of each bunny
  bunny_row = [x+1 for x in range(total_bunnies)]
  if not result:
    #if nagative cycle exist. All bunnies are saved
    ans=[i for i in range(total_bunnies)]
    return ans

  # if no negative cycle exists. we will take permutation of each possible bunny pair. We will use permutation because the
  # graph is bi-directional which means the idstance of bunny x to bunny y is not the same as bunny y to bunny x.


  # i stands for number of bunny pairs in a permutation. we start with maximum and go on to minimum
  for i in range(total_bunnies,0,-1):
    #j is the each pair found after permuation. we give total bunnies and number of bunnies in a pair as the parameters
    for j in permutations(bunny_row,i):
      #converting tupple to a list
      j=list(j)

      #calculating time of current bunny pair traversal
      this_time = get_time(j,new_matrix)
      # if we find a time which suits our time limit given we will straight away stop the loop and return the ans as we have started with considering
      # maximum number of bunny in the pairs.
      if this_time <= time_limit:
        # reducing the bunny row number by one to get bunny number
        for i in range(len(j)):
          j[i]-=1
        # sorting bunny number and return the answer
        j.sort()
        return j
  # if no bunny pair is found it means we can not save any bunny
  return []
