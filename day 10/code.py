from math import floor

data = [[str(value) for value in line] for line in open('input.dat').read().splitlines()]
open = {"<", "{", "[", "("} ; close = {">": "<", "}": "{", "]": "[", ")": "("} ; points = {">": 25137, "}": 1197, "]": 57, ")": 3}
open_close_map = {"(": ")", "[": "]", "{": "}", "<": ">"} ; points_clossures = {">": 4, "}": 3, "]": 2, ")": 1}

openings = [[] for _ in range (0, len(data))]
closings = []
errors = []

for i, line in enumerate (data):
    to_complete = True
    for j, chunk in enumerate (line):
        if chunk in open:
            openings[i].append(chunk)
        elif openings[i][-1] == close[chunk]:
            openings[i].pop()
        else:
            errors.append(chunk)
            err_msg = "Irregular closure chunk. Found {}.".format(chunk)
            print(err_msg)
            to_complete = False
            break
    if to_complete:
        closing = [open_close_map[c] for c in reversed(openings[i])]
        closings.append(closing)

print("Total syntax error score:",sum(points[c] for c in errors))

total_scores = []
for closing in closings:
    score = 0
    for c in closing:
        score = score * 5
        score += points_clossures[c]
    total_scores.append(score)
total_scores.sort()
print("Middle score:", total_scores[floor(len(total_scores)/2)])
