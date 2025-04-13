def temp():
    fahrenheit = float(input("Enter temepratue in Fahrenheit:"))
    celsius = float(fahrenheit - 32) * 5.0 / 9.0
    print(f"Temperature {fahrenheit}F = {celsius}C")

if __name__ == "__main__":
    temp()