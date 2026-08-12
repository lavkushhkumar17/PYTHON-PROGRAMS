import math
def scientific_calculator():
    while True:
        print("\n===== SCIENTIFIC CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Sine (sin)")
        print("8. Cosine (cos)")
        print("9. Tangent (tan)")
        print("10. Log Base 10")
        print("11. Natural Log (ln)")
        print("12. Factorial")
        print("13. Pi")
        print("14. Euler's Number (e)")
        print("15. Exit")

        choice = input("\nEnter your choice (1-15): ")

        if choice == "15":
            print("Thank you for using the Scientific Calculator!")
            break

        try:
            if choice in ["1", "2", "3", "4", "5"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    print("Result =", a + b)
                elif choice == "2":
                    print("Result =", a - b)
                elif choice == "3":
                    print("Result =", a * b)
                elif choice == "4":
                    if b != 0:
                        print("Result =", a / b)
                    else:
                        print("Error: Division by zero!")
                elif choice == "5":
                    print("Result =", math.pow(a, b))

            elif choice == "6":
                num = float(input("Enter number: "))
                print("Result =", math.sqrt(num))

            elif choice == "7":
                angle = float(input("Enter angle in degrees: "))
                print("Result =", math.sin(math.radians(angle)))

            elif choice == "8":
                angle = float(input("Enter angle in degrees: "))
                print("Result =", math.cos(math.radians(angle)))

            elif choice == "9":
                angle = float(input("Enter angle in degrees: "))
                print("Result =", math.tan(math.radians(angle)))

            elif choice == "10":
                num = float(input("Enter number: "))
                print("Result =", math.log10(num))

            elif choice == "11":
                num = float(input("Enter number: "))
                print("Result =", math.log(num))

            elif choice == "12":
                num = int(input("Enter a positive integer: "))
                print("Result =", math.factorial(num))

            elif choice == "13":
                print("Pi =", math.pi)

            elif choice == "14":
                print("Euler's Number =", math.e)

            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input! Please enter numbers only.")
        except Exception as e:
            print("Error:", e)

scientific_calculator()
