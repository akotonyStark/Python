is_hot = False
is_cold = False
if is_hot:
    print('The weather is hot')
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day")
print('Enjoy your day')

price_of_house = 1000000
has_good_credits = True
has_high_income = True
has_criminal_record = True

if has_high_income and has_good_credits and not has_criminal_record:
    print('Down Payment = $', 0.1 * price_of_house)
elif has_high_income or has_good_credits:
    print(f'Down Payment =  ${0.2 * price_of_house}')
else:
    print(f'Down Payment =  ${0.2 * price_of_house}')
