t = int(input())
u = []
for _ in range(t):
   a,b,c = map(int,input().split())
   u.append([a,b,c])
result = []
for case in u:
   if case[0]<=20 and case[1]<=20 and case[2]<=20:
      result.append('good')
   else:
      result.append('bad')
for i in range(len(result)):
   print(f'Case {i+1}: {result[i]}')