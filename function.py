def print_multiples(n):
    i=1
    output=""
    while i <= 6:
      output += str(n*i) + "\t"
      i += 1
    print(output)

#function called print_multiples
#while loop looks similar
#printing happens here IN the function

#print_multiples(3)

def print_square():
    return [n**2 for n in range(10)]

#for n in range(10): print n

print print_square()

