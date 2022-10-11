N = int(input("кол-во чисел:"))
a = []
for i in range(N):
    a.append(int(input("число: ")))
print(a)

i = int(0)
i = int(input("1 - по возрастанию; 2 - по убыванию: "))

if i == 1:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
             a[j], a[j + 1] = a[j + 1], a[j]

if i == 2:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] < a[j + 1]:
              a[j], a[j + 1] = a[j + 1], a[j]

print(a)