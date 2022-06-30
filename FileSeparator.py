import re


def separate_file(file_content):
    curr = 0
    file_length = len(file_content)
    while curr < file_length:
        curr_char = file_content[curr]

        # Case where character is a space
        if curr_char == " ":
            curr = process_space(curr)
        # Case where we don't know if the "." symbol is a number or special symbol
        elif curr_char == ".":
            curr = num_or_ss(file_content, file_length, curr)
        # Case where character is a number
        elif (bool(re.fullmatch("[0-9]", curr_char))) and True:
            curr = process_num(file_content, file_length, curr, curr_char)
        # Case where character is a word
        elif (bool(re.fullmatch("[a-zA-Z]", curr_char))) and True:
            curr = process_word(file_content, file_length, curr, curr_char)
        # Case where character is a special character
        else:
            curr = process_ss(curr, curr_char)


# The space is skipped by just incrementing curr by 1
def process_space(curr):
    return curr + 1


# The "." goes with a number if it has a number directly after it. If not, the "." is a special symbol.
def num_or_ss(file_content, file_length, curr):
    if curr + 1 < file_length:
        if (bool(re.fullmatch("[0-9]", file_content[curr+1]))) and True:
            return process_num(file_content, file_length, curr, ".")
        else:
            return process_ss(curr, ".")
    else:
        return process_ss(curr, ".")


# The number is processed by concatenating numbers and possibly a single decimal point together.
def process_num(file_content, file_length, curr, curr_char):
    this_num = ""
    while curr < file_length:
        curr_char = file_content[curr]
        if (bool(re.fullmatch("[0-9]", curr_char))):
            this_num += str(curr_char)
            curr += 1
        elif curr_char == ".":
            this_num += str(curr_char)
            curr += 1
            break
        else:
            break
    while(curr < file_length):
        curr_char = file_content[curr]
        if (bool(re.fullmatch("[0-9]", curr_char))):
            this_num += str(curr_char)
            curr += 1
        else:
            break
    print(this_num + " -- number")
    return curr


# The word is processed by concatenating any characters (if any) following the first.
def process_word(file_content, file_length, curr, curr_char):
    this_word = curr_char
    curr += 1
    while curr < file_length:
        curr_char = file_content[curr]
        if (bool(re.fullmatch("[a-zA-Z]", curr_char))) and True:
            this_word += curr_char
            curr += 1
        else:
            break
    print(this_word + " -- word")
    return curr


# We simply print the special symbol and increment curr by 1.
def process_ss(curr, curr_char):
    print(curr_char + " -- ss")
    return curr + 1
