fname = input("Enter file name: ")
p = 0
 
with open(fname, 'u') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isspace):
                    p=p+1
print("Occurrences of blank spaces:")
print(p)
