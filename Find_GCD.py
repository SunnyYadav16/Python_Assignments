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
    '9': 'nine'
}


# Function to convert words to digit
def word_to_digit(inputs):
    converted_digit = int(''.join(word_to_digit_dict[ele] for ele in inputs.split()))
    return converted_digit

# Function to convert digits to words
def digit_to_word(result_value_digit):
    result_value_words = ''
    for value in str(result_value_digit):
        result_value_words += digit_to_word_dict.get(value)
    return result_value_words


if __name__ == "__main__":

    try:
        first_input, second_input = input("Enter your first value: "), input("Enter your second value: ")
        a_factor, b_factor = [], []
        i = 1

        a_number = word_to_digit(first_input)
        b_number = word_to_digit(second_input)

        while i <= a_number and i <= b_number:
            if a_number % i == 0:
                a_factor.append(i)
            if b_number % i == 0:
                b_factor.append(i)
            i += 1

        # Creating a new list to find the intersection values that occurs in both lists
        answer_list = [value for value in a_factor if value in b_factor]
        result_value = answer_list[-1]

        final_result = digit_to_word(result_value)
        print(f"The calculated GCD of the numbers is: {final_result}")


    except KeyError:
        print()
        print("Error. Please insert numeric value in all words inputs like this: three six, one two, etc..")
