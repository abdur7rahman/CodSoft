while True:
    print("\n Select operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter the Choice: "))

    if choice == 1:
        num_1 = float(input("Enter the 1st number : "))
        num_2 = float(input("Enter the 2nd number : "))
        add = num_1 + num_2
        print(f"Addition of {num_1} and {num_2} is {add}")

    elif choice == 2:
        num_1 = float(input("Enter the 1st number : "))
        num_2 = float(input("Enter the 2nd number : "))
        sub = num_1 - num_2
        print(f"Subtraction of {num_1} and {num_2} is {sub}")

    elif choice == 3:
        num_1 = float(input("Enter the 1st number : "))
        num_2 = float(input("Enter the 2nd number : "))
        mul = num_1 * num_2
        print(f"Multiplication of {num_1} and {num_2} is {mul}")

    elif choice == 4:
        num_1 = float(input("Enter the 1st number : "))
        num_2 = float(input("Enter the 2nd number : "))
        div = num_1 / num_2
        print(f"Division of {num_1} and {num_2} is {div}")
    
    else:
        print("Invalid choice!")

    next_calculation = input("let's do the operations again! [y/n]: ")
    if next_calculation == "n" :
       break