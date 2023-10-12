lines = int(input("How many lines will there be?"))

poem = []

i = 0

# lets the user input as many lines as he declared

while i < lines:
    line_of_poem = input("")
    poem.append(line_of_poem.lower())
    i += 1

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

number_of_vowels = 0
number_of_consonants = 0

# counts the vowels and consonants in the poem (used isalpha)

for line in poem:
    for letter in line:
        if letter in vowels:
            number_of_vowels += 1
        elif letter.isalpha():
            number_of_consonants += 1
            
            
# shows the statistics

print("Number of vowels: ", number_of_vowels)
print("Number of consonants: ", number_of_consonants)