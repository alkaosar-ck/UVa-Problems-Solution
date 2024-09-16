t = int(input())
current = 0
for _ in range(t):
   s = input()
   if s.startswith('donate'):
      current += int(s.split()[1])
   elif s == 'report':
      print(current)
      