a =[]
for i in range(int(input())):
  line = input().split(":")
  if float(line[0])>=float(line[1]):
    line = "SWERVE"
  elif (float(line[0])*5)>=float(line[1]):
    line = "BRAKE"
  else:
    line = "SAFE"
  a.append(line)
for i in range(len(a)):
  print(a[i])
