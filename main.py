#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# starting_letter = ''
with open('./Input/Letters/starting_letter.txt') as text: 
    starting_letter = text.read()

# names_arr = []
with open('./Input/Names/invited_names.txt') as names:
    names_arr = names.read().split('\n')

# cur_letter = ''
for name in names_arr:
    cur_letter = starting_letter.replace('[name]', name)
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as new_letter:
        new_letter.write(cur_letter)
