PLACEHOLDER = '[name]'

with open('./Input/Letters/starting_letter.txt') as text: 
    starting_letter = text.read()

with open('./Input/Names/invited_names.txt') as names:
    names_arr = names.read().split('\n')

for name in names_arr:
    cur_letter = starting_letter.replace(PLACEHOLDER, name)
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as new_letter:
        new_letter.write(cur_letter)
