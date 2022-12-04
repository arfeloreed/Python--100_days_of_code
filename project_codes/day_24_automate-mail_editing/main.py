with open("./Input/Names/invited_names.txt") as file:
    data_names = file.readlines()
list_names = [name.strip() for name in data_names]

for name in list_names:
    with open("./Input/Letters/starting_letter.txt") as file:
        letter = file.read()
        letter = letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", "w") as data:
            data.write(f"{letter}")
