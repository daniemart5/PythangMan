try: 
    age = int(input('Age: '))
    income = 20000 
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age must be higher than 0")
except ValueError:
    print('Invalid value')