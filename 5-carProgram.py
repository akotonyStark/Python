command = ""
started = False

while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print('Car has already started!')
        else:
            print('Car has started')
            started = True
    elif command == 'stop':
        if not started:
            print('car has already been stopped!')
        else:
            started = False
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
