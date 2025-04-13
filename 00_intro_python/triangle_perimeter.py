def perimeter():
    side1:float = float(input("What is the length of side 1?"))
    side2:float = float(input("What is the length of side 2?"))
    side3:float = float(input("What is the length of side 3?"))
    result = side1 + side2 + side3
    print(f"The perimeter of the triangle is " + str(result))

if __name__ == "__main__":
    perimeter()