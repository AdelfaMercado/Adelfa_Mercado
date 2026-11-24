#Arden Cristino S. Mercado II
#8-Adelfa
scores = []

for i in range(1,6):
    quiz_scores = int(input("Enter thy score peasant"))
    scores.append(quiz_scores)

average_score = sum(scores)/len(scores)
print("--quiz score report--")
print(len(f"quizes: {scores}"))
print(max(f"max score: {scores}"))
print(min(f"min score: {scores}"))
print(f"ascending: {sorted(scores)}")
print(f"descending: {sorted(scores, reverse=True)}")
print(f"original:{sorted(scores)}")
print(f"average: {average_score}")