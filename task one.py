number_input = input("Please, enter your number: ")
sum_of_digits = 0
for digit in str(number_input):
    sum_of_digits += int(digit)
print(sum_of_digits)
