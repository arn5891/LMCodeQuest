a =[]
for i in range(int(input())):
  line = input().split(" ")
  b = int(line[0])+int(line[1])
  c = int(line[0])*int(line[1])
  a.append([b,c])
for i in range(len(a)):
  print(str(a[i][0])+" "+str(a[i][1]))
