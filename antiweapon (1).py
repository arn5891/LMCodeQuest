import math
b = []
for j in range(int(input())):
  a = {}
  for i in range(int(input())):
    ast = input().split(" ")
    aa = math.sqrt((int(ast[0])*int(ast[0]))+(int(ast[1])*int(ast[1])))
    a.update({str(ast[0])+" "+str(ast[1]):aa})
    a = sorted(a.items(), key=lambda x:x[1])
    a = dict(a)
  b.append(a)
  #break
for i in range(len(b)):
  for keys, value in b[i].items():
    print(keys)