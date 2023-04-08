#1. If input is divisible by 4, the function will show the string "fizz"
#2. If input is divisible by 7, he function will show the string "buzz"
#3. If input is divisible by both 4 and 8, the function output will show "fizzbuzz"
#4. The same inut will show for all other numbers

def fizz_buzz(input):
    if input % 4 == 0:
        if input % 7 == 0:
            return "FizzBuzz"
        elif input % 7 != 0:
            return "Fizz"
    elif input % 7 == 0:
        return "Buzz"
    else:
        return input

print(fizz_buzz(4))
