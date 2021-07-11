i = 1
while i <= 5:
    print('*' * i, i)
    i = i + 1
print('Done')

secret_number = 7
count = 0
guess_limit = 3
while count < guess_limit:
    number = int(input('Enter a number:'))
    count += 1
    if number == secret_number:
        print('You won!!!')
