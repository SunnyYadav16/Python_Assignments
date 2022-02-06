# Program to find the anagrams of words

# A function to find the anagrams of the input string
def Anagram(my_list):
    my_dict = {}

    for word in my_list:
        my_key = ''.join(sorted(word))

        if my_key in my_dict.keys():
            my_dict[my_key].append(word)
        else:
            my_dict[my_key] = []
            my_dict[my_key].append(word)

    result = []
    for key, value in my_dict.items():
        result.append(value)
    return result

if __name__ == "__main__":

    try:
        my_input_list = input().split(',')

        if len(my_input_list) == 1 and "" in my_input_list:
            print([""])
        else:
            final_output = Anagram(my_input_list)
            print(final_output)

    except KeyError:
        print("Error. Enter comma separated values like: eat,ate,tan,ban  etc...")