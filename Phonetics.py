phonetics={
    'A': 'Alfa',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Wiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

name=list(input('Enter Your Name '))
a=len(name)
print(name)
for i in range(int(a)):
    print(name[i])
    print(phonetics.get(name[i]))








