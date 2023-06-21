from pin import check_pin
print("Введите ваш ПИН-код")
user_input = input()
x = check_pin(user_input)
if x == True:
    print("Такой ПИН-код подходит")
else:
    print("Такой ПИН-код НЕ подходит")