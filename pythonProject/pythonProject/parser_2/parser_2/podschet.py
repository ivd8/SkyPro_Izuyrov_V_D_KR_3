proba_list = [False, False, False, True, True, True, False, True, False, False, False,
          False, False, False, False, False, True, False, False, False, False, False,
          False, False, False, False, False, False, False, False, False, True, True, False,
          False, False, True, False, False, False, False, True, True, False, True, False,
          True, False, False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, True, False, False, True, False,
          True, False, False, False, False, True, True, False, True, True, False, False, False,
          False, True, True, False, True, False, False, False, False, False, False, False,
          False, False, False, False, False, False, False, False, True, False, False, False,
          False, False, False, False, False, False, True, False, False, False, False, False,
          False, False, False, False, True, False, False, False, False, False, False, False,
          False, False, True, False, False, False, False, False, False, False, False, False,
          True, False, False, False, False, False, False, False]

count_1 = 0
count_2 = 1
count_3 = 2
count_4 = 3
count_5 = 4

pod_6 = 0
pod_5 = 0
pod_4 = 0
pod_3 = 0
pod_2 = 0
pod_1 = 0

print(proba_list)
for i in proba_list:
    count_1 += 1
    count_2 += 1
    count_3 += 1
    count_4 += 1
    count_5 += 1

    if i == True and proba_list[count_1] == True and proba_list[count_2] == True and proba_list[count_3] == True and proba_list[count_4] == True:
        pod_5 += 1
        proba_list[count_1 - 1] = 'Цифра'
        proba_list[count_1] = 'Цифра'
        proba_list[count_2] = 'Цифра'
        proba_list[count_3] = 'Цифра'
        proba_list[count_4] = 'Цифра'
        continue

    elif i == True and proba_list[count_1] == True and proba_list[count_2] == True and proba_list[count_3] == True:
        pod_4 += 1
        proba_list[count_1 - 1] = 'Цифра'
        proba_list[count_1] = 'Цифра'
        proba_list[count_2] = 'Цифра'
        proba_list[count_3] = 'Цифра'
        continue

    elif i == True and proba_list[count_1] == True and proba_list[count_2] == True:
        pod_3 += 1
        proba_list[count_1 - 1] = 'Цифра'
        proba_list[count_1] = 'Цифра'
        proba_list[count_2] = 'Цифра'
        continue

    elif i == True and proba_list[count_1] == True:
        pod_2 += 1
        proba_list[count_1 - 1] = 'Цифра'
        proba_list[count_1] = 'Цифра'
        continue

    elif i == True:
        pod_1 += 1
        proba_list[count_1 - 1] = 'Цифра'
        continue
    else:
        continue

print(f'pod_6: {pod_6}')
print(f'pod_5: {pod_5}')
print(f'pod_4: {pod_4}')
print(f'pod_3: {pod_3}')
print(f'pod_2: {pod_2}')
print(f'pod_1: {pod_1}')
print(f'Всего: {len(proba_list)}')

