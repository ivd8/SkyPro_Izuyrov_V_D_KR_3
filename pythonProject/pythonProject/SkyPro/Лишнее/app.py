from validators.validate_pin import validate_pin
from validators.validate_card import validate_card

print("Введите ваш номер карты")
card_number = input()
print("Введите ваш ПИН-код")
card_pin = input()

print(validate_pin(card_pin))
print(validate_card(card_number))
