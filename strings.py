name = "alison"

length = len(name)

last = name[length-1]

print(length)
print(last)

#piglatin

first = name[0]
pigname = name[1:] + name[0] + "ay" #name[1:] is a slice of string starting at index 1
#pigname = name[1:5] + name[0] + "ay"
#name[:] is the whole string

print(pigname)

#all letters after l
print(name[1:6])

s = "Ginzberg, Moretti, Campbell"
print(s[0:8], s[10:17], s[19:27])

alison  = s[0:8]
#should add last names

print("type a word to see it in pig latin")
myword = raw_input()
pigword = myword[1:] + myword[0] + "ay"
print(pigword)

for char in pigword:
	print(char)

#[print char for char in pigword]








