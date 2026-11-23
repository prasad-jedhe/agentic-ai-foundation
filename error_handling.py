

try:
    a = int (input("Enter a number: "))
    b = int (input("Enter b number: "))
    c = int (input("Enter c number: "))
    c = (a+b+c)/3
    print(f"Output for a/b: {c}")

except ValueError as e:
        print(f"Please enter valid number",e)
except ZeroDivisionError as e:
        print(f"Please enter valid number denominator cannot be 0",e)
except Exception as e:
        print(e)
finally:
    print("Program done")

