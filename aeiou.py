a =[]
vwls = ["a","e","i","o","u"]
for i in range(int(input())):
  line = list(input())
  ct = 0
  for j in range(len(line)):
    for k in range(len(vwls)):
      if line[j] == vwls[k]:
        ct+=1
  a.append(ct)
for i in range(len(a)):
  print(str(a[i]))
