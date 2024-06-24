# Verify that Given number is prime number are not..?

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("Enter a number: "))

# Check if the number is prime are not.
if is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is not a Prime Number.")
