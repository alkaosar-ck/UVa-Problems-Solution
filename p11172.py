u =[]
for _ in range(int(input())):
   a,b = map(int,input().split())
   if a>b:
      u.append('>')
   elif a<b:
      u.append('<')
   else:
      u.append('=')
for case in u:
   print(case)