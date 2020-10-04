# Justin Calma
# CECS 378 - 09
# MW 8 AM - 10:15 AM
# Lab 1 Part 1

# Definition of brute force Caesar Cipher decrypter
def caesarDecrypt(text, key):

    # Create a string that will store the decrypted text
    decrypted = ""

    # For each char in the text
    for c in text:

        # If the current char is lowercase
        if c.islower():

            # Find the index of the current char by subtracting the Unicode of 'a' from
            # the unicode of the current char
            cIndex = ord(c) - ord('a')

            # Find the index of the current char by subracting the current shift amount from cIndex
            # Then mod 26 --> 26 because the possible range is the number of characters in the alphabet
            # Add the unicode of 'a' to get the result
            cOriginalPosition = (cIndex - key) % 26 + ord('a')

            # Find the original position of the char before it was shifted
            # chr() finds the character represented by a number
            cOriginal = chr(cOriginalPosition)

            # Add the found char to the string containing the decrypted phrase
            decrypted += cOriginal

        # If the current char is uppercase
        elif c.isupper():

            # Find the index of the current char by subtracting the Unicode of 'A' from
            # the unicode of the current char
            cIndex = ord(c) - ord('A')

            # Find the index of the current char by subracting the current shift amount from cIndex
            # Then mod 26 --> 26 because the possible range is the number of characters in the alphabet
            # Add the unicode of 'A' to get the result
            cOriginalPosition = (cIndex - key) % 26 + ord('A')

            # Find the original position of the char before it was shifted
            # chr() finds the character represented by a number
            cOriginal = chr(cOriginalPosition)

            # Add the found char to the string containing the decrypted phrase
            decrypted += cOriginal

        # Else the current char is a non-alphabetic char --> Puncatation marks
        else:

            # Add the current char to the string storing the decrypted phrase
            decrypted += c

    # Return the decrypted string
    return decrypted

# Definition of the function to find the frequencies in the text
def findTheFrequencies(text):

    # Create a dictionary to save the values and keys
    frequencies = {}

    # For each character in the passed in text
    for i in text:

        # If the current char is already in the dictionary ...
        if i in frequencies:

            # Go to the current char and increment the value
            frequencies[i] += 1

        # If the current char is not in the dictionary ...
        else:

            # Add it to the dictionary and give it a value of 1
            frequencies[i] = 1

    # Return the frequencies dictionary
    return frequencies

# Definition of the main function
def main():

    # Output the menu to the user
    print("-----------------------------------------Part 1-----------------------------------------\n"
          "\n1: fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc\n" 
          
          "\n2: oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv" \
          "\n aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy\n"
          
          "\n3: ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa" \
          "\n twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae\n" \
          
          "\n4: iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq" \
          "\n ihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs" \
          "\n hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt" \
          "\n isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun" \
          "\n siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq" \
          "\n uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz\n")

    # Initialize string variables with the encrypted text corresponding to each part
    text1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"

    text2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"

    text3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa" \
            " twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"

    text4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq" \
            " ihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs" \
            " hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt" \
            " isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun" \
            " siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq" \
            " uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"

    print("A: Caesar Cipher -- Works for text options 1 and 2\n" \
          "B: Find the frequencies of the chars in the string and then use monoalphabetic cipher\n")

    # Keep running the program until the user wants to quit
    while (True):

        print("----------------------------------------------------------------------------------------\n")

        # Save the input of the user
        userInput = input("Enter the letter and number that corresponds to the option you want:\n")

        # If the user has chosen to perform Caesar cipher on problem 1
        if (userInput == "A1" or userInput == "1A"):

            # Print the message before it was decrypted
            print("The encrypted text before decryption is:\n", text1, "\n")

            # Loop until 26 iterations has been performed
            for i in range(0, 26):

                # Perform decryption using Caesar Cipher. Takes in text1 and the current shifted key
                plain_text = caesarDecrypt(text1, i)

                # Output the results to the user
                print("For key {}, decrypted text: {}".format(i, plain_text))

            print("\n")

        # If the user has chosen to perform Caesar cipher on problem 2
        elif (userInput == "A2" or userInput == "2A"):

            # Print the message before it was decrypted
            print("The encrypted text before decryption is:\n", text2, "\n")

            # Loop until 26 iterations has been performed
            for i in range(0, 26):

                # Perform decryption using Caesar Cipher. Takes in text2 and the current shifted key
                plain_text = caesarDecrypt(text2, i)

                # Output the results to the user
                print("For key {}, decrypted text: {}".format(i, plain_text))

            print("\n")

        # If the user has chosen to perform Caesar cipher on problem 3
        elif (userInput == "A3" or userInput == "3A"):

            # Print the message before it was decrypted
            print("The encrypted text before decryption is:\n", text3, "\n")

            # Loop until 26 iterations has been performed
            for i in range(0, 26):

                # Perform decryption using Caesar Cipher. Takes in text3 and the current shifted key
                plain_text = caesarDecrypt(text3, i)

                # Output the results to the user
                print("For key {}, decrypted text: {}".format(i, plain_text))

            print("\n")

        # If the user has chosen to perform Caesar cipher on problem 4
        elif (userInput == "A4" or userInput == "4A"):

            # Print the message before it was decrypted
            print("The encrypted text before decryption is:\n", text4, "\n")

            # Loop until 26 iterations has been performed
            for i in range(0, 26):

                # Perform decryption using Caesar Cipher. Takes in text4 and the current shifted key
                plain_text = caesarDecrypt(text4, i)

                # Output the results to the user
                print("For key {}, decrypted text: {}".format(i, plain_text))

            print("\n")

        # If the user has chosen to method 2 on problem 1
        elif (userInput == "B1" or userInput == "1B"):

            # Find the amount of occurences of each char in the text and save them into a dict
            frequenciesDict = findTheFrequencies(text1)

            # Sort the frequencies dictionary in ascending order
            frequenciesDict = sorted(frequenciesDict.items(), key = lambda x: x[1])

            # Output the frequencies dictionary to the user
            print("Count of all characters in text1 is:\n " + str(frequenciesDict) + "\n")

            # Print the message before it was decrypted
            print("The encrypted text before decryption is:\n", text1, "\n")

            # Hack the monoalphabetic cipher and brute force by swapping each char in the text one by one.
            # Paper and penicl, guess and check method
            # Using the "Relative frequency in the English language" (Monogram Frequencies) and how often a given char occurs
            # swap the most occured char in the string with the most common letter in the english language,
            # do this until the higher occured chars have been swapped into the text.
            # Now find patterns within the text like "oo" , "ss" , "is" , "ing" , "tion" , "ee" , etc.
            # Keep doing this process until all patterns have been found.
            # Now go through the text and find partially encrypted words and guess which word it is.
            # Find chars that are in between two words --> they are most likely "A" or "I"
            # Keep doing this process until the string has been decrypted.
            decrypt1 = text1.replace("n", "E")
            decrypt1 = decrypt1.replace("j", "A")
            decrypt1 = decrypt1.replace("b", "S")
            decrypt1 = decrypt1.replace("w", "N")
            decrypt1 = decrypt1.replace("c", "T")
            decrypt1 = decrypt1.replace("v", "M")
            decrypt1 = decrypt1.replace("f", "W")
            decrypt1 = decrypt1.replace("q", "H")
            decrypt1 = decrypt1.replace("r", "I")
            decrypt1 = decrypt1.replace("u", "L")
            decrypt1 = decrypt1.replace("x", "O")
            decrypt1 = decrypt1.replace("d", "U")
            decrypt1 = decrypt1.replace("k", "B")
            decrypt1 = decrypt1.replace("h", "Y")
            decrypt1 = decrypt1.replace("a", "R")
            decrypt1 = decrypt1.replace("m", "D")

            # Output the decrypted text to the user
            print("The decrypted text of text1 is:\n", decrypt1, "\n")

        # If the user has chosen to method 2 on problem 2
        elif (userInput == "B2" or userInput == "2B"):

            # Find the amount of occurences of each char in the text and save them into a dict
            frequenciesDict = findTheFrequencies(text2)

            # Sort the frequencies dictionary in ascending order
            frequenciesDict = sorted(frequenciesDict.items(), key = lambda x: x[1])

            # Output the frequencies dictionary to the user
            print("Count of all characters in text2 is :\n " + str(frequenciesDict) + "\n")

            # Print the message before it was decrypted
            print("The encrypted text before decryption is:\n", text2, "\n")

            # Hack the monoalphabetic cipher and brute force by swapping each char in the text one by one.
            # Paper and penicl, guess and check method
            # Using the "Relative frequency in the English language" (Monogram Frequencies) and how often a given char occurs
            # swap the most occured char in the string with the most common letter in the english language,
            # do this until the higher occured chars have been swapped into the text.
            # Now find patterns within the text like "oo" , "ss" , "is" , "ing" , "tion" , "ee" , etc.
            # Keep doing this process until all patterns have been found.
            # Now go through the text and find partially encrypted words and guess which word it is.
            # Find chars that are in between two words --> they are most likely "A" or "I"
            # Keep doing this process until the string has been decrypted.
            decrypt2 = text2.replace("o", "T")
            decrypt2 = decrypt2.replace("z", "E")
            decrypt2 = decrypt2.replace("c", "H")
            decrypt2 = decrypt2.replace("m", "R")
            decrypt2 = decrypt2.replace("v", "A")
            decrypt2 = decrypt2.replace("n", "S")
            decrypt2 = decrypt2.replace("a", "F")
            decrypt2 = decrypt2.replace("j", "O")
            decrypt2 = decrypt2.replace("r", "W")
            decrypt2 = decrypt2.replace("m", "R")
            decrypt2 = decrypt2.replace("d", "I")
            decrypt2 = decrypt2.replace("b", "G")
            decrypt2 = decrypt2.replace("i", "N")
            decrypt2 = decrypt2.replace("t", "Y")
            decrypt2 = decrypt2.replace("e", "J")
            decrypt2 = decrypt2.replace("g", "L")
            decrypt2 = decrypt2.replace("p", "W")
            decrypt2 = decrypt2.replace("y", "D")
            decrypt2 = decrypt2.replace("h", "M")
            decrypt2 = decrypt2.replace("x", "C")
            decrypt2 = decrypt2.replace("f", "K")
            decrypt2 = decrypt2.replace("q", "V")

            # Output the decrypted text to the user
            print("The decrypted text of text2 is:\n", decrypt2, "\n")

        # If the user has chosen to method 2 on problem 3
        elif (userInput == "B3" or userInput == "3B"):

            # Find the amount of occurences of each char in the text and save them into a dict
            frequenciesDict = findTheFrequencies(text3)

            # Sort the frequencies dictionary in ascending order
            frequenciesDict = sorted(frequenciesDict.items(), key = lambda x: x[1])

            # Output the frequencies dictionary to the user
            print("Count of all characters in text3 is :\n " + str(frequenciesDict) + "\n")

            # Print the message before it was decrypted
            print("The encrypted text before decryption is:\n", text3, "\n")

            # Hack the monoalphabetic cipher and brute force by swapping each char in the text one by one.
            # Paper and penicl, guess and check method
            # Using the "Relative frequency in the English language" (Monogram Frequencies) and how often a given char occurs
            # swap the most occured char in the string with the most common letter in the english language,
            # do this until the higher occured chars have been swapped into the text.
            # Now find patterns within the text like "oo" , "ss" , "is" , "ing" , "tion" , "ee" , etc.
            # Keep doing this process until all patterns have been found.
            # Now go through the text and find partially encrypted words and guess which word it is.
            # Find chars that are in between two words --> they are most likely "A" or "I"
            # Keep doing this process until the string has been decrypted.
            decrypt3 = text3.replace("l", "E")
            decrypt3 = decrypt3.replace("a", "I")
            decrypt3 = decrypt3.replace("t", "T")
            decrypt3 = decrypt3.replace("o", "F")
            decrypt3 = decrypt3.replace("q", "S")
            decrypt3 = decrypt3.replace("j", "O")
            decrypt3 = decrypt3.replace("w", "W")
            decrypt3 = decrypt3.replace("s", "A")
            decrypt3 = decrypt3.replace("k", "H")
            decrypt3 = decrypt3.replace("f", "L")
            decrypt3 = decrypt3.replace("r", "D")
            decrypt3 = decrypt3.replace("c", "G")
            decrypt3 = decrypt3.replace("e", "C")
            decrypt3 = decrypt3.replace("u", "U")
            decrypt3 = decrypt3.replace("h", "B")
            decrypt3 = decrypt3.replace("i", "N")
            decrypt3 = decrypt3.replace("g", "M")
            decrypt3 = decrypt3.replace("p", "R")

            # Output the decrypted text to the user
            print("The decrypted text of text2 is:\n", decrypt3, "\n")

        # If the user has chosen to method 2 on problem 4
        elif (userInput == "B4" or userInput == "4B"):

            # Find the amount of occurences of each char in the text and save them into a dict
            frequenciesDict = findTheFrequencies(text4)

            # Sort the frequencies dictionary in ascending order
            frequenciesDict = sorted(frequenciesDict.items(), key = lambda x: x[1])

            # Output the frequencies dictionary to the user
            print("Count of all characters in text4 is :\n " + str(frequenciesDict) + "\n")

            # Print the message before it was decrypted
            print("The encrypted text before decryption is:\n", text4, "\n")

            # Hack the monoalphabetic cipher and brute force by swapping each char in the text one by one.
            # Paper and penicl, guess and check method
            # Using the "Relative frequency in the English language" (Monogram Frequencies) and how often a given char occurs
            # swap the most occured char in the string with the most common letter in the english language,
            # do this until the higher occured chars have been swapped into the text.
            # Now find patterns within the text like "oo" , "ss" , "is" , "ing" , "tion" , "ee" , etc.
            # Keep doing this process until all patterns have been found.
            # Now go through the text and find partially encrypted words and guess which word it is.
            # Find chars that are in between two words --> they are most likely "A" or "I"
            # Keep doing this process until the string has been decrypted.
            decrypt4 = text4.replace("q", "E")
            decrypt4 = decrypt4.replace("s", "T")
            decrypt4 = decrypt4.replace("y", "O")
            decrypt4 = decrypt4.replace("e", "A")
            decrypt4 = decrypt4.replace("i", "S")
            decrypt4 = decrypt4.replace("h", "H")
            decrypt4 = decrypt4.replace("n", "I")
            decrypt4 = decrypt4.replace("a", "N")
            decrypt4 = decrypt4.replace("x", "G")
            decrypt4 = decrypt4.replace("j", "L")
            decrypt4 = decrypt4.replace("o", "Y")
            decrypt4 = decrypt4.replace("l", "F")
            decrypt4 = decrypt4.replace("u", "R")
            decrypt4 = decrypt4.replace("m", "M")
            decrypt4 = decrypt4.replace("t", "B")
            decrypt4 = decrypt4.replace("z", "W")
            decrypt4 = decrypt4.replace("d", "D")
            decrypt4 = decrypt4.replace("b", "C")
            decrypt4 = decrypt4.replace("k", "V")
            decrypt4 = decrypt4.replace("r", "U")
            decrypt4 = decrypt4.replace("f", "P")
            decrypt4 = decrypt4.replace("v", "K")
            decrypt4 = decrypt4.replace("w", "X")

            # Output the decrypted text to the user
            print("The decrypted text of text2 is:\n", decrypt4, "\n")

        # The user has decided to stop the program
        else:
            print("THE PROGRAM WILL NOW TERMINATE")
            quit()

# Call the main function to start the program
main()