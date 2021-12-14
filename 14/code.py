from collections import Counter

data = [[str(value) for value in line] for line in open('input.dat').read().splitlines()]
polymer_template = data[0]
pair_insertion_rules = {}
number_of_pairs = {}
number_of_letters = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "Z": 0, "J": 0, "K": 0, "X": 0, "Y": 0, "W": 0}
for i in range (2,len(data)):
    pair_insertion_rules[str(data[i][0])+str(data[i][1])] = str(data[i][-1])
    number_of_pairs[str(data[i][0])+str(data[i][1])] = 0

polymer_old = polymer_template
for it in range (0,10):
    to_add = [pair_insertion_rules[str(polymer_old[i])+str(polymer_old[i+1])] for i in range (0,len(polymer_old)-1)]
    polymer_new = ""
    for i in range (0,len(polymer_old)):
        polymer_new += str(polymer_old[i])
        if i < len(polymer_old)-1:
            polymer_new += str(to_add[i])
    polymer_old = polymer_new

c = Counter(polymer_new)
print("Most common element - least common element:",c.most_common()[0][1]-c.most_common()[-1][1])

for i in range (0,len(polymer_template)):
    number_of_letters[str(polymer_template[i])] += 1
    if i < len(polymer_template)-1:
        number_of_pairs[str(polymer_template[i])+str(polymer_template[i+1])] += 1

for it in range (0,40):
    number_of_pairs_new = {pair: 0 for pair in number_of_pairs}
    for pair in number_of_pairs:
        new_letter = pair_insertion_rules[pair]
        number_of_pairs_new[pair[0]+new_letter] += 1*number_of_pairs[pair]
        number_of_pairs_new[new_letter+pair[1]] += 1*number_of_pairs[pair]
        number_of_letters[new_letter] += 1*number_of_pairs[pair]
    number_of_pairs = number_of_pairs_new

to_remove = []
for letter in number_of_letters:
    if number_of_letters[letter] == 0:
        to_remove.append(letter)
for letter in to_remove:
    del number_of_letters[letter]

c = Counter(number_of_letters)
print("Most common element - least common element:",c.most_common()[0][1]-c.most_common()[-1][1])