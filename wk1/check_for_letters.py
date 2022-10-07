letters = input("Please enter three letters separated by a space \n")
letters = letters.split()
words = open("words.txt", 'r')
fout = open("letters.txt", 'w')

for line in words:
    accept = 0
    word = line.strip()
    print(word)
    for letter in letters:
        if line.find(letter) != -1:
            accept += 1
    if accept == 3:
        fout.write(word + "\n")
    accept = 0
words.close()
fout.close()
