import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)
score = 0

for questions in data:
    print(questions["question"])
    for index, alternatives in enumerate(questions["alternatives"]):
        print(f"{index + 1} - {alternatives}")
    user_choice = int(input("Enter your answer: "))
    questions["user_choice"] = user_choice


for question in data:
    if question["user_choice"] == question["answer"]:
        score += 1
        result = "correct answer"
    else:
        result = "wrong answer"
    message = f"{result} Your answer: {question['user_choice']},"\
    f"correct answer: {question['answer']}"
    print(message)


print(score, "/", len(data))