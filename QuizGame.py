import random

# вопросы и ответы в виде словаря
questions = {
    'Какой язык программирования был создан первым?': 'Fortran',
    'Какое название у первого спутника, запущенного в космос?': 'Спутник-1',
    'Какой газ является основным компонентом атмосферы Земли?': 'Азот',
    'Кто является создателем компании Tesla?': 'Илон Маск',
    'Какая столица Франции?': 'Париж'
}

categories = list(questions.keys())

# счетчик правильных ответов
score = 0

print('Добро пожаловать в викторину!')

# выбор категории
category = input(f'Выберите категорию: {", ".join(categories)}\n')

if category not in categories:
    print('Категория не найдена!')
else:
    print(f'Вы выбрали категорию "{category}". Поехали!')
    random.shuffle(categories) # перемешивание вопросов
    for q in categories:
        if q in questions and q.startswith(category):
            answer = input(q + '\n')
            if answer.lower() == questions[q].lower():
                print('Правильно!')
                score += 1
            else:
                print(f'Неправильно! Правильный ответ: {questions[q]}')
    print(f'Игра окончена. Ваш результат: {score}/{len(categories)}')
