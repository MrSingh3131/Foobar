from fractions import Fraction

def gcd(x, y):
  def gcd1(x, y):
    if y == 0:
      return x
    return gcd1(y, x%y)
  return gcd1(abs(x), abs(y))

def lcm(x, y):
  return int(x*y/gcd(x,y))

def change_matrix(m):
  sum_of_list=[]
  for i in range(len(m)):
    sum_of_list.append(sum(m[i]))
  for i in range(len(m)):
    for j in range(len(m[i])):
      if sum_of_list[i]==0:
        m[i][j]=Fraction(0,1)
      else:
        m[i][j]=Fraction(m[i][j],sum_of_list[i])
  return m

def gauss_elmination(m, values):
  mat = m
  for i in range(len(mat)):
    index = -1
    for j in range(i, len(mat)):
      if mat[j][i].numerator != 0:
          index = j
          break
    if index == -1:
      raise ValueError('Gauss elimination failed!')
    mat[i], mat[index] = mat[index], mat[j]
    values[i], values[index] = values[index], values[i]
    for j in range(i+1, len(mat)):
      if mat[j][i].numerator == 0:
        continue
      ratio = -mat[j][i]/mat[i][i]
      for k in range(i, len(mat)):
        mat[j][k] += ratio * mat[i][k]
      values[j] += ratio * values[i]
  res = [0 for i in range(len(mat))]
  for i in range(len(mat)):
    index = len(mat) -1 -i
    end = len(mat) - 1
    while end > index:
      values[index] -= mat[index][end] * res[end]
      end -= 1
    res[index] = values[index]/mat[index][index]
  return res

def transpose(mat):
  tmat = []
  for i in range(len(mat)):
    for j in range(len(mat)):
      if i == 0:
        tmat.append([])
      tmat[j].append(mat[i][j])
  return tmat

def inverse(mat):
  tmat = transpose(mat)
  mat_inv = []
  for i in range(len(tmat)):
    values = [Fraction(int(i==j), 1) for j in range(len(mat))]
    mat_inv.append(gauss_elmination(tmat, values))
  return mat_inv

def mat_mult(mat1, mat2):
  res = []
  for i in range(len(mat1)):
    res.append([])
    for j in range(len(mat2[0])):
      res[i].append(Fraction(0, 1))
      for k in range(len(mat1[0])):
        res[i][j] += mat1[i][k] * mat2[k][j]
  return res

def splitQR(mat, lengthR):
  lengthQ = len(mat) - lengthR
  Q = []
  R = []
  for i in range(lengthQ):
      Q.append([int(i==j)-mat[i][j] for j in range(lengthQ)])
      R.append(mat[i][lengthQ:])
  return [Q, R]

def solution(mat):
  empty = [ 0 for x in range(len(mat[0]))]
  count = 0
  for i in m:
    if i == empty:
      count+=1
  if count == len(mat):
    return [1,1]
  new_matrix=change_matrix(m)
  Q, R = splitQR(new_matrix,count)
  inv = inverse(Q)
  res = mat_mult(inv, R)
  row = res[0]
  l = 1
  for item in row:
      l = lcm(l, item.denominator)
  res = list(map(lambda x: int(x.numerator*l/x.denominator), row))
  res.append(l)
  return res
