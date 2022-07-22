f = open("sampleSentences.txt", "r")
lines = f.readlines()

from collections import Counter

# set up counter to keep letter counts
counts = Counter()

for line in lines:
    
    # split on space
    words = line.split()

    # check each word
    for word in words:
        if word[0].isalpha():  # make sure it starts with a letter
            counts.update([word[0].lower()])

f = open("ps4-6_out.txt", "w")
for letter,count in counts.most_common():
    f.write(letter + ":" + str(count) + "\n")
f.close()
