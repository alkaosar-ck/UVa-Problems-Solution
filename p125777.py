inputs = []
while True:
   x = input()
   if x =='*':
      break
   else:
      inputs.append(x)
for i in range(len(inputs)):
   if inputs[i] == 'Hajj':
      print(f'Case {i+1}: Hajj-e-Akbar')
   else:
      print(f'Case {i+1}: Hajj-e-Asghar')
