i = 0

while i < 10:
    i += 1
    if i % 3 == 0:
        continue  # pula os múltiplos de 3
    print(i)


i = 0
while i < 5:
    if i == 2:
        i += 1
        continue
    print(i)
    i += 1
