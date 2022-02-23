# Program to calculate GCD or HCF of 2 numbers

# A dictionary containing words as keys and numbers as their values
word_to_digit_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# A dictionary containing numbers as keys and words as their values
digit_to_word_dict = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}


# Function to convert words to digit
def word_to_digit(inputs):
    # converted_digit = int(''.join(word_to_digit_dict[ele] for ele in inputs.split()))
    start, end = 0, 0
    converted_digit = ''
    while end < len(inputs):
        if word_to_digit_dict.get(inputs[start:end+1]):
            converted_digit += word_to_digit_dict.get(inputs[start:end+1])

            start = end + 1
        end += 1
    return converted_digit


# Function to convert digits to words
def digit_to_word(result_value_digit):
    result_value_words = ''
    i = 0
    while i < len(str(result_value_digit)):
        result_value_words += digit_to_word_dict.get(str(result_value_digit)[i])
        i += 1
    return result_value_words


# Function for calculating the gcd of two numbers and returning the value
def calculate_gcd(a_num, b_num):
    i = 1
    while i <= a_num and i <= b_num:
        if a_num % i == 0 and b_num % i == 0:
            common_factor.append(i)
        i += 1

    if len(common_factor) == 0:
        return -1

    # Taking the last value of the list as it is the biggest factor
    result_value = common_factor[-1]

    return result_value


if __name__ == "__main__":

    try:
        first_input, second_input = input("Enter your first value: "), input("Enter your second value: ")
        common_factor = []

        # Converting input words to digit
        a_number = int(word_to_digit(first_input))
        b_number = int(word_to_digit(second_input))

        # Calculating GCD of the number
        gcd_answer = calculate_gcd(a_number, b_number)

        if gcd_answer != -1:
            # Converting the digits to words
            final_result = digit_to_word(gcd_answer)
            print(f"\nThe calculated GCD of the numbers is: {final_result}")
        else:
            print("\nGCD not found for the two numbers")

    except KeyError:
        print()
        print("Error. Please insert numeric value in all words inputs like this: three six, one, two, etc..")
