import random
from questions_answers import questions_answers

# Функция для проверки ответа
def check_answer(question, answer):
    correct_answer = questions_answers.get(question)
    if correct_answer == answer:
        return "Правильно!"
    else:
        return f"Неправильно. Правильный ответ: {correct_answer}"

# Основная игра
def play_game():
    topics = {
        "Git": [q for q in questions_answers if "(Git)" in q],
        "Docker": [q for q in questions_answers if "(Docker)" in q],
        "Terraform": [q for q in questions_answers if "(Terraform)" in q],
        "Ansible": [q for q in questions_answers if "(Ansible)" in q],
        "Kubernetes": [q for q in questions_answers if "(Kubernetes)" in q],
        "Bash": [q for q in questions_answers if "(Bash)" in q],
        "Python": [q for q in questions_answers if "(Python)" in q],
    }
    
    print("Выберите тему для вопросов:")
    for i, topic in enumerate(topics.keys(), 1):
        print(f"{i}. {topic}")
    
    topic_choice = int(input("Введите номер выбранной темы: "))
    chosen_topic = list(topics.keys())[topic_choice - 1]
    questions = topics[chosen_topic]
    random.shuffle(questions)
    
    score = 0
    for question in questions:
        print(f"Вопрос: {question}")
        user_answer = input("Ваш ответ: ").strip()
        result = check_answer(question, user_answer)
        print(result)
        if result == "Правильно!":
            score += 1
    
    print(f"Игра окончена. Ваш счет: {score}/{len(questions)}")

# Запуск игры
if __name__ == "__main__":
    play_game()
