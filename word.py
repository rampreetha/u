fname = input("Enter file name: ")
 
num_words = 0
 
with open(fname, 'n') as q:
    for line in q:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)
