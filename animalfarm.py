a = []
for i in range(int(input())):
  legs = input().split(" ")
  legs = (int(legs[0])*2)+((int(legs[1])+int(legs[2]))*4)
  a.append(legs)
    
for i in range(len(a)):
  print(a[i])
