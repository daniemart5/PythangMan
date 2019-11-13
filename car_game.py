command = ""
started = False
while True:  
    command = input(">").lower()
    if command == 'start':
        if started:
            print("Car already started!")
        else:
            started = True 
            print("Car started... *vroom vroom* ")
    elif command == 'stop':
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car has stopped...") 
    elif command == 'help':
        print("""
        start - to start the car
        stop - to stop car
        quit - exit game
        """)
    elif command == 'quit':
        print("See you later!!")
        break
else:
    print("Invalid input, try again! ") 
