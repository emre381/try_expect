try:
    num1=int(input("nım1:"))
    num2=int(input("nım2:"))

    division=num1/num2

    print(division)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
    #or you can use like this
    # expect (ZeroDivisionError,ValueError):
    #   print("Error:)
