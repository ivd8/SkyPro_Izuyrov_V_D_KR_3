result = ['f', '4']

result_list = result
print(result_list)
result_file = {}
with open('history2.txt', 'r') as file:
    for data in file:
        print(data)
        result_file.append(data)
    if result_list[0] in result_file and int(result_list[1]) > result_file[result_list]:
        result_file[result_list] = result_list[1]
print(result_file)