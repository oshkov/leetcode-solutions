'''
Задача с собеседования в INNOPROG

Пример:
На входе: АААВВСАА
На выходе: A3B2CA2
'''

def string_editor(string: str):
    amount = 1
    new_string = ''
    last_letter = None
    for letter in string:
        if new_string == '' or letter != last_letter:
            amount = 1
            new_string += letter
            last_letter = letter
        elif letter == last_letter:
            amount += 1
            if amount > 2:
                new_string = new_string[:-1] + str(amount)
            elif amount > 1:
                new_string += str(amount)
            else:
                new_string += letter

    return new_string


print(string_editor('AAABBCAA'))