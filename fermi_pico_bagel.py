import random

num = int(input('Enter the number of digits you want to play with: '))
while True :
    original_number = ''

    for i in range(num):
        original_number = original_number + str(random.randint(1,9))
        
    if (len(set(original_number)) == num):
        break

while True :
    guess_number = input("\nEnter your guess : ")
    output = []

    if len(original_number) != len(guess_number):
        print("Invalid Number !!")
        continue
    
    if len(set(guess_number)) != len(guess_number):
        print("Duplicate number")
        continue
    
    if guess_number == original_number :
        print("Fermi "*len(original_number))
        print("\nYou win !!\n")
        break

    for i in range(len(original_number)):
        if guess_number[i] == original_number[i]:
            output.append('Fermi')
        elif guess_number[i] in original_number :
            output.append('Pico')
        
    output_string = ''
    for i in output:
        output_string += i + ' '
        
    if len(output) == 0 :
        print("Bagel")
    else :
        print(output_string)