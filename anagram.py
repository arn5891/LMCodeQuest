a = []
for i in range(int(input())):
  wrds = input()
  idk = wrds.split("|")
    
  if idk[0] == idk[1] or len(idk[0]) != len(idk[1]):
    wrds+=" = NOT AN ANAGRAM"
    a.append(wrds)
    continue
    
  idk[0] = [*idk[0]]
  idk[1] = [*idk[1]]
  for b in range(len(idk[1])):
    for c in range(len(idk[0])):
      if idk[1][b]==idk[0][c]:
        idk[0].pop(c)
        break
  if len(idk[0])==0:
    wrds+=" = ANAGRAM"
  else:
    wrds+=" = NOT AN ANAGRAM"
  a.append(wrds)
    
  
for j in range(len(a)):
  print(a[j])
