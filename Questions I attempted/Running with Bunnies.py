# finding single shortest path -
def purane_vala(times,times_limit):
      times_limit+=1
      time_list = []
      for i in range(len(times)-1):
        mini = 1000
        for j in range(len(times[i])):
          if i!=j:
            if mini>times[i][j]:
              mini = times[i][j]
        time_list.append(mini)
      time_list.append(0)

      visited=[]
      start = 0
      end = len(times)-1
      empty = [-1000 for i in range(len(times))]

      while(True):
        current = times[start]

        for i in visited:
          if i!= end:
            current[i]=-1000

        visited.append(start)
        maximum = -1000
        yesrow=[]
        for jana in range(len(times)):
          if current[jana]!=-1000 and jana!=start:
            if times_limit-current[jana]-time_list[jana] >0 :
              yesrow.append(times_limit-current[jana])
              if maximum<times_limit-current[jana]:
                maximum = times_limit-current[jana]
            else:
              yesrow.append(-1000)
          else:
            yesrow.append(-1000)
        if yesrow==empty:
          break

        start = yesrow.index(maximum)
        times_limit-=current[start]
      visited.sort()
      visited.pop(0)
      try:
          j = visited.index(end)
          visited = visited[:j]
          for i in range(len(visited)):
            visited[i]-=1
          return visited
      except:
          return visited


def solution(times, time_limit):
    # import copy
    def BellmanForddd():
        for src in range(V):
            distances[src][src] = 0
            for _ in range(V - 1):
                for u in range(V):
                    for v in range(V):
                        if distances[src][u] != INF and distances[src][u] + times[u][v] < distances[src][v]:
                            # Record this lower distance
                            distances[src][v] = distances[src][u] + times[u][v]
                            # self.shortestPath[src][v] = v if src == u else u

            # Check for negative-weight cycles.  The above step
            for u in range(V):
                for v in range(V):
                    if distances[src][u] != INF and distances[src][u] + times[u][v] < distances[src][v]:
                        return False
        return True
    V = len(times)
    INF = float("Inf")
    distances = [[INF for _ in range(V)] for _ in range(V)]
    if len(times)<=2:
        return []
    new_matrix=BellmanForddd()
    if new_matrix:
        return purane_vala(distances, time_limit)
    else:
        lenn=len(times)-2
        ans=[i for i in range(lenn)]
        return ans

time=[[0, 2, 2, 2, -1],
             [9, 0, 2, 2, -1],
             [9, 3, 0, 2, -1],
             [9, 3, 2, 0, -1],
             [9, 3, 2, 2, 0]]
time_limit=1
print(solution(time, time_limit))
