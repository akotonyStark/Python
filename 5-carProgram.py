command = ""

while True:
    command = input('>').lower()
    if command == 'start':
        print('Car has started')
    elif command == 'stop':
        print('car has stopped')
    elif command == 'help':
        print("""
              start - to start the car
              stop -  to stop the car
              quit - to quit
              """)
    elif command == 'quit':
        break
    else:
        print("I don't understand that")
