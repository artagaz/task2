#1
inStr = input()

print("1:", inStr[2])

print("2:", inStr[-2])

print("3:", inStr[0:5])

print("4:", inStr[0:len(inStr)-2])

print("5:", inStr[::2])
print("6:", inStr[1::2])

print("7:", inStr[::-1])

print("8:", inStr[::-2])

print("9:", len(inStr))

#2
inStr = input()
l = len(inStr) + 1
print (inStr[0:l//2])
print (inStr[l//2:])

#3
inStr = input()
print(inStr[inStr.find("h")+1:inStr.find("h", inStr.find("h")+1, )][::-1])

4
inStr = input()
if inStr.find("f")!= -1:
    if inStr.rfind("f") != (-1 and inStr.find("f")):
        print(f"first index: {inStr.find("f")}, last index: {inStr.rfind("f")}")
    else:
        print("index of 'f': ", inStr.index("f"))

#5
prevWord = input()
newWord = input()
while prevWord[-1]==newWord[0]:
    prevWord = newWord
    newWord = input()
print(newWord)

#6
inStr = input()
for i in range(0, len(inStr)):
    print(inStr[i]*(i+1), end='')

#7
inStr = input()
a = inStr[1::].replace('V', '!V!').split('!')
current_pos = 0
k = 1 if len(inStr) == 1 or inStr[1] == 'V' else 0
for i in a:
    if i == '':
        continue
    elif i[0] == '<':
        current_pos -= len(i)
        print(current_pos * ' ' + inStr[0]  + i.replace('<', inStr[0]))
        k = 0
    elif i[0] == '>':
        print(current_pos * ' ' + inStr[0]  + i.replace('>', inStr[0]))
        current_pos += len(i)
        k = 0
    elif i[0] == 'V':
        if k :
            print(current_pos * ' ' + inStr[0])
        k = 1
if k :
    print(current_pos * ' ' + inStr[0])

#8
inStr = input()
if len(inStr) % 2 == 0:
    n = len(inStr) // 2
    for i in range(n):
        print(' ' * (n - i - 1) + inStr[n - i - 1] + ' ' * i +
              ' ' * i + inStr[n + i])
else:
    d = (len(inStr) + 1) // 2
    print(' ' * ((len(inStr) - 1) // 2) + inStr[d - 1] + ' ' * ((len(inStr) - 1) // 2))
    for i in range(1, d):
        print(' ' * (d - i - 1) + inStr[d - i - 1] + ' ' * i +
              ' ' * (i - 1) + inStr[d + i - 1])

#9
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

#10
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break

#11
a = [i for i in input().split()]
for i in range(1, len(a), 2):
    a[i-1], a[i] = a[i], a[i-1]
print(a)

#12
a = [i for i in input().split()]
b = []
for a in a:
    if a not in b:
        b.append(a)
print(b)

#13
numbers = [int(i) for i in input().split()]
words = [i for i in input().lower().split()]

print(words[numbers[0]-1].capitalize(), end=' ')
for i in range(1, len(numbers)):
    print(words[numbers[i]-1], end=' ')

#14
x = []
y = []
for i in range(8):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)
correct = True
for i in range(8):
    for j in range(i + 1, 8):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
if correct:
    print('NO')
else:
    print('YES')

#15
queue = []
for i in range(int(input())):
    task = input()
    if 'Кто последний?' in task:
        queue.append(task.split("-")[-1])
    elif 'Я только спросить!' in task:
        queue.insert(0, task.split("-")[-1])
    elif 'Следующий!' in task:
        if queue:
            print('Заходит ', queue.pop(0), '!', sep='')
        else:
            print('В очереди никого нет.')