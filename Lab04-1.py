import random
top_scores = []
MAX_LEN = 50
for i in range(MAX_LEN):
    if i < 5:
        top_scores.append(random.randint(1,99))
    if i > 5:
        a = random.randint(1,99)
        index = top_scores.index(min(top_scores))
        if a > b:
            top_scores[index] = a

print(top_scores)
