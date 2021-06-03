def print_final(object):
    assigned_letters_str = object.assigned_letters.__str__()
    assigned_letters_list = assigned_letters_str.split(',')
    final_output = ''
    for letter in assigned_letters_list:
        final_output += letter
    length = len(final_output)
    final_output = '\n' * 2 + '#' * (len(final_output) + 12) + f'\n#     {final_output}     #\n' + '#' * (
                len(final_output) + 12)
    final_output = '\n' * 6 + ' ' * (length // 2) + 'FINAL DIGITS' + final_output
    print(final_output)