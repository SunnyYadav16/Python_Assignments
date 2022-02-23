# Program to find the anagrams of words

# A function to find the anagrams of the input string
def find_anagram(my_list):
    my_dict = {}

    for word in my_list:
        # sorting the words from the list and using them as keys of the other same words
        my_key = ''.join(sorted(word))

        # checking if the key is already present in the dictionary, appending it if not present.
        if my_key in my_dict.keys():
            my_dict[my_key].append(word)
        else:
            my_dict[my_key] = []
            my_dict[my_key].append(word)

    result = []
    for value in my_dict.values():
        result.append(value)
    return result


if __name__ == "__main__":

    try:
        my_input_list = input().split(',')

        # Checking if input string is empty
        if len(my_input_list) == 1 and "" in my_input_list:
            print([""])
        else:
            final_output = find_anagram(my_input_list)
            print(final_output)

    except KeyError:
        print("Error. Enter comma separated values like: eat,ate,tan,ban  etc...")
