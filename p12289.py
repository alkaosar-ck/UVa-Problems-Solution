# t = int(input())
# answers = []
# test_cases = []
# for _ in range(t):
#    test_cases.append(input().strip())
# list1 = ['three','four','five','seven','eight','nine']
# list2= ['one','two','six','ten']
# dict = {
#    'one':1,
#    'two':2,
#    'three':3,
#    'four':4,
#    'five':5,
#    'six':6,
#    'seven':7,
#    'eight':8,
#    'nine':9,
#    'ten':10,
# }
# for i in test_cases:
#    if len(i) == 3:
#       for x in list2:
#          if ( i[0] == x[0] or i[1] == x[1]) and i[-1] == x[-1]:
#             answers.append(x)
#    else:
#       for x in list1:
#          if (((i[0] == x[0] or i[1] == x[1])and i[-1] == x[-1]) and len(i) == len(x)):
#             answers.append(x)
# for case in answers:
#    if case in dict.keys():
#       print(dict[case])

t = int(input())
answers = []
test_cases = []
for _ in range(t):
    test_cases.append(input().strip())

words = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
}

for word in test_cases:
    for correct_word, value in words.items():

        if len(word) == len(correct_word):
            mismatch_count = sum(1 for a, b in zip(word, correct_word) if a != b)
            if mismatch_count <= 1:
                answers.append(value)
                break

for ans in answers:
    print(ans)
