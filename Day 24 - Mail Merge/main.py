with open("Input/Letters/starting_letter.txt") as letter:
    letter_text = letter.read()

with open("Input/Names/invited_names.txt") as name:
    names = name.read().splitlines()

for each_name in names:
    text = letter_text.replace("[name]", each_name)
    with open(f"Output/ReadyToSend/letter_for_{each_name}.txt", "w") as output:
        output.write(text)