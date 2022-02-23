# Program to find the number of correct parenthesis generation according to the user input

def generate_parenthesis(my_res_list, my_string, open_parenthesis, close_parenthesis, n):

    if open_parenthesis == n and close_parenthesis == n:
        my_res_list.append(my_string)
        return

    # Checking condition for if the value of open_parenthesis is less than the number of parenthesis allowed
    if open_parenthesis < n:
        generate_parenthesis(my_res_list, my_string + "(", open_parenthesis + 1, close_parenthesis, n)

    # Checking condition for if the value of close_parenthesis is less than the open_parenthesis generated
    if close_parenthesis < open_parenthesis:
        generate_parenthesis(my_res_list, my_string + ")", open_parenthesis, close_parenthesis + 1, n)

    return my_res_list


if __name__ == "__main__":

    try:
        my_result_list = []
        number_of_parenthesis = int(input('Enter the number of parenthesis to be generated: '))

        result = generate_parenthesis(my_result_list, '', 0, 0, number_of_parenthesis)
        print(result)

    except ValueError:
        print("\nError! Enter numerical value in the input.")
