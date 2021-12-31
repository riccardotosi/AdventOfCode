"""Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....                                  0
                                                    --------->       1   2
  5:      6:      7:      8:      9:                                   3
 aaaa    aaaa    aaaa    aaaa    aaaa                                4   5
b    .  b    .  .    c  b    c  b    c                                 6
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

- The wire/segment connections are mixed up separately for each four-digit display
- All of the digits within a display use the same connections

You might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on:
- the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on,
- with just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.

Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

We have ten unique signal patterns, a | delimiter, and finally the four digit output value.

Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are).
The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections.
- Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on.
- Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

You should be able to work out which combination of signal wires corresponds to each of the ten digits.
Then, you can decode the four digit output value.
Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.
"""

"""Part 1: Because the digits 1, 4, 7, and 8 each use a unique number of segments,
you should be able to tell which combinations of signals correspond to those digits.
Counting only digits in the output values (the part after | on each line), in the above example,
there are 26 instances of digits that use a unique number of segments (highlighted above)."""

def returnNumber(positions):
    if set([2, 5]) == set(positions):
        return 1
    elif set([1, 2, 3, 5]) == set(positions):
        return 4
    elif set([0, 2, 5]) == set(positions):
        return 7
    elif set([0, 1, 2, 3, 4, 5, 6]) == set(positions):
        return 8
    elif set([0,1,2,4,5,6]) == set(positions):
        return 0
    elif set([0,2,3,4,6]) == set(positions):
        return 2
    elif set([0,2,3,5,6]) == set(positions):
        return 3
    elif set([0,1,3,5,6]) == set(positions):
        return 5
    elif set([0,1,3,4,5,6]) == set(positions):
        return 6
    elif set([0,1,2,3,5,6]) == set(positions):
        return 9

def buildLetterToPositionMap(pattern):
    letters_to_positions = {}
    # find letter in position 2 and 5
    aux = [set(word) for word in pattern if len(word) in [2,3,4,7]]
    two = aux[0].intersection(aux[1], aux[2], aux[2])
    five = aux[0].intersection(aux[1], aux[2], aux[2])
    # find position zero
    aux = [set(word) for word in pattern if len(word) in [3]]
    zero = aux[0].difference(two)
    # find position six
    aux = [set(word) for word in pattern if len(word) not in [2, 3, 4]]
    six = aux[0].intersection(aux[0], aux[1], aux[2], aux[3], aux[4], aux[5], aux[6])
    six = six.difference(zero)
    # find position 3
    aux = [set(word) for word in pattern if len(word) in [5]]
    three = aux[0].intersection(aux[0], aux[1], aux[2])
    three = three.difference(zero, six)
    # find position 1
    aux = [set(word) for word in pattern if len(word) in [4]]
    one = aux[0].difference(two)
    one = one.difference(three)
    # find position 5
    aux = [set(word) for word in pattern if len(word) in [6]]
    five = aux[0].intersection(aux[1], aux[2])
    five = five.difference(zero, one, six)
    # find position 2
    two = two.difference(five)
    # find position 4
    aux = [set(word) for word in pattern if len(word) in [7]]
    four = aux[0].difference(zero, one, two, three, five, six)

    # build dictionaries
    letters_to_positions[list(zero)[0]] = 0
    letters_to_positions[list(one)[0]] = 1
    letters_to_positions[list(two)[0]] = 2
    letters_to_positions[list(three)[0]] = 3
    letters_to_positions[list(four)[0]] = 4
    letters_to_positions[list(five)[0]] = 5
    letters_to_positions[list(six)[0]] = 6
    return letters_to_positions

data = open('input.dat').read().splitlines()
patterns = [line.split('|')[0].split() for line in data]
outputs = [line.split('|')[1].split() for line in data]

num_outputs_part1 = 0
for output in outputs:
    for out in output:
        if len(out) in [2, 3, 4, 7]:
            num_outputs_part1 += 1
print("Times digits 1, 4, 7, 8 appear in the output:", num_outputs_part1)

"""Part 2: What do you get if you add up all of the output values?"""

total = 0
# letter positions start from 0
for pattern, output in zip (patterns, outputs):
    letters_to_positions = buildLetterToPositionMap(pattern)
    res = ""
    for out in output:
        p_out = [letters_to_positions[l] for l in out]
        res += str(returnNumber(p_out))
    total += int(res)

print("Sum up all output values:", total)