# function to check if a number is prime
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


# open file for writing
with open("results.txt", "w") as file:
    # loop through numbers 0 to 250
    for i in range(0, 250):
        # check if number is prime
        if is_prime(i):
            # write prime number to file
            file.write(str(i) + "\n")
