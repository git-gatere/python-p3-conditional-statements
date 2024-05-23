#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower () == "admin" and password == 12345 :
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        weather = "It's brisk out there!"
    elif (temperature >= 40 and temperature <= 65 ):
        weather = "It's a little chilly out there!"
    elif temperature > 85:
        weather = "It's too dang hot out there!"
    else :
        weather = "It's perfect out there!"
    return weather

def fizzbuzz(num):
    divisor_three = num % 3
    divisor_five = num % 5
    
    if divisor_three == 0 and divisor_five == 0:
        return "FizzBuzz"
    elif divisor_three == 0  and divisor_five != 0:
        return "Fizz"
    elif divisor_three != 0 and divisor_five == 0 :
        return "Buzz"
    else:
        return num
    

def calculator(operation, num1, num2):
    if operation == "+":
          return num1 + num2
    elif operation == "-":
          return num1 - num2
    elif operation == "*":
          return num1 * num2
    elif operation == "/":
          return num1 / num2
    else:
          return "Invalid operation!"
