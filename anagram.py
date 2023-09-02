a = []
for i in range(int(input())):
  wrds = input()
  idk = wrds.split("|")
  anagram = False
  
  idk[0] = [*idk[0]]
  idk[1] = [*idk[1]]
  for b in range(len(idk[1])):
    for c in range(len(idk[0])):
      if idk[1][b]==idk[0][c]:
        idk[0].pop(c)
        break
  if len(idk[0])==0:
    wrds+=" = ANAGRAM"
    anagram = True
    
  if idk[0] == idk[1] or len(idk[0]) != len(idk[1]) or len(idk[0]) == len(idk[1]) and idk[0]!=idk[1]:
    wrds+=" = NOT AN ANAGRAM"
    a.append(wrds)
    continue
    
  

print("\n")
for i in range(len(a)):
  print(a[i])
