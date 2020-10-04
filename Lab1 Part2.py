# Justin Calma
# CECS 378 - 09
# MW 8 AM - 10:15 AM
# Lab 1 Part 2

# Declared the acceptable characters that are a part of the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz,.;-’ "

# Declared the keys used for options 1 - 4
key1 = "bdmkfqlyngiwsopvuzetcrahjx,.;-’ "
key2 = "etbzhlfnkidamgcsvxpowujqry,.;-’ "
key3 = "mhsdrblinajyozvqfgxtpcuewk,.;-’ "
key4 = "keyabcdfghijlmnopqrstuvwxz,.;-’ "

# Definition of the simple - substitution encrypter
def encrypt(msg, key):

    # Create a string variable that will store the encrypted phrase
    cipher = ""

    # For each character in the passed in text ...
    for i in msg:

        # ... Substitute the current char with the char in the key
        # at the same index
        cipher += key[alphabet.index(i.lower())]

    # Return the encryted phrase
    return cipher

# Definition of the simple - substitution decrypter
def decrypt(cipher, key):

    # Create a string variable that will store the decrypted phrase
    text = ""

    # For each character in the passed in encrypted text ...
    for i in cipher:

        # ... Substitute the current char with the char in the alphabet at
        # the same index
        text += alphabet[key.index(i.lower())]

    # Return the decrypted phrase
    return text

# Definition of the main function
def main():

    # Output the menu to the user
    print("-----------------------------------------Part 2-----------------------------------------\n"  \
          
          "\n1: He who fights with monsters should look to it that he himself does" \
          "\n not become a monster. And if you gaze long into an abyss, the abyss" \
          "\n also gazes into you.\n"
          
          "\n2: There is a theory which states that if ever anybody discovers" \
          "\n exactly what the Universe is for and why it is here, it will" \
          "\n instantly disappear and be replaced by something even more bizarre" \
          "\n and inexplicable. There is another theory which states that this" \
          "\n has already happened.\n"
          
          "\n3: Whenever I find myself growing grim about the mouth; whenever it is" \
          "\n a damp, drizzly November in my soul; whenever I find myself" \
          "\n involuntarily pausing before coffin warehouses, and bringing up the" \
          "\n rear of every funeral I meet; and especially whenever my hypos get" \
          "\n such an upper hand of me, that it requires a strong moral principle" \
          "\n to prevent me from deliberately stepping into the street, and" \
          "\n methodically knocking people’s hats off - then, I account it high" \
          "\n time to get to sea as soon as I can.\n" \
          
          "\n4: Enter your own message. \n")

    # Initialize 3 variables to represent the 3 texts to encrypt and decrypt
    text1 = "He who fights with monsters should look to it that he himself does not become a monster. And if you gaze long into an abyss, the abyss also gazes into you."

    text2 = "There is a theory which states that if ever anybody discovers" \
          " exactly what the Universe is for and why it is here, it will" \
          " instantly disappear and be replaced by something even more bizarre" \
          " and inexplicable. There is another theory which states that this" \
          " has already happened."


    text3 = "Whenever I find myself growing grim about the mouth; whenever it is" \
          " a damp, drizzly November in my soul; whenever I find myself" \
          " involuntarily pausing before coffin warehouses, and bringing up the" \
          " rear of every funeral I meet; and especially whenever my hypos get" \
          " such an upper hand of me, that it requires a strong moral principle" \
          " to prevent me from deliberately stepping into the street, and" \
          " methodically knocking people’s hats off - then, I account it high" \
          " time to get to sea as soon as I can."

    # Keep running the program until the user wants to quit
    while (True):

        print("----------------------------------------------------------------------------------------\n")

        # Save the input of the user
        userInput = input("Enter the number of which message you want to encrypt and decrypt or enter any value to quit: \n")

        # The user has selected to work on the first option
        if (userInput == '1'):

            # Call the encrypt function to encrypt text. Takes in text1 and key1
            encryptValue = encrypt(text1, key1)

            # Call the decrypt function to decrypt the encrypted text. Takes in the encrypted text from the encrypt function
            # and the key that we used to encrypt the text
            decryptValue = decrypt(encryptValue, key1)

            # Output the results to the user
            print("The encrypted text for problem 1 is:\n", encryptValue)
            print("The decrypted text for problem 1 is:\n", decryptValue)
            print("The key used for problem 1 is:\n", key1, "\n")

        # The user has selected to work on the second option
        elif (userInput == '2'):

            # Call the encrypt function to encrypt text. Takes in text2 and key2
            encryptValue = encrypt(text2, key2)

            # Call the decrypt function to decrypt the encrypted text. Takes in the encrypted text from the encrypt function
            # and the key that we used to encrypt the text
            decryptValue = decrypt(encryptValue, key2)

            # Output the results to the user
            print("The encrypted text for problem 2 is:\n", encryptValue)
            print("The decrypted text for problem 2 is:\n", decryptValue)
            print("The key used for problem 2 is:\n", key2, "\n")

        # The user has selected to work on the third option
        elif (userInput == '3'):

            # Call the encrypt function to encrypt text. Takes in text3 and key3
            encryptValue = encrypt(text3, key3)

            # Call the decrypt function to decrypt the encrypted text. Takes in the encrypted text from the encrypt function
            # and the key that we used to encrypt the text
            decryptValue = decrypt(encryptValue, key3)

            # Output the results to the user
            print("The encrypted text for problem 3 is:\n", encryptValue)
            print("The decrypted text for problem 3 is:\n", decryptValue)
            print("The key used for problem 3 is:\n", key3, "\n")

        # The user has selected to work on the fourth option
        elif (userInput == '4'):

            # Output to the user and save their input into a variable
            text4 = input("Enter the text you want to encrypt and decrypt (Program does not take in a large passage): \n")

            # Call the encrypt function to encrypt the user input. Takes in the user input and the modified alphabet key
            encryptValue = encrypt(text4, key4)

            # Call the decrypt function to decrypt the encrypted text. Takes in the encrypted text from the encrypt function
            # and the key that we used to encrypt the text
            decryptValue = decrypt(encryptValue, key4)

            # Output the results to the user
            print("The encrypted text for your input is is:\n", encryptValue)
            print("The decrypted text for your input is:\n", decryptValue)
            print("The key used for your input is:\n", key4, "\n")

        # The user has decided to stop the program
        else:
            print("THE PROGRAM WILL NOW TERMINATE")
            quit()

# Call the main function to start the program
main()