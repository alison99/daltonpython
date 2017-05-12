print("type a word to see in pig latin")

word = raw_input()

pigword = word[1:]+word[0]+"ay"

print("the word in pig latin is " + pigword)
