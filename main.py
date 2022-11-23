'''
1. Пользователь запустил игру.
2. Игра приветствует игрока
3. Игра задает вопрос вида:
    "what is answer <слово на английском языке>
    1. <слово на русском языке>
    2. <слово на русском языке>
    3. <слово на русском языке>
    4. <слово на русском языке>
4. Пользователь вводит вариант ответа 1-4
5. Если правильный ответ, то распечатать "Correct"
5.1 Иначе распечатать "Incorrect. Correct answer is <слово на русском языке>
5.2 Пользователь играет до тех пор, пока не выйдет из игры
'''
import random
dictionary = {
    'hello': 'привет',
    'bye': 'пока',
    'run': 'запуск',
    'game': 'игра',
    'file': 'файл',
    'invite': 'пригласить',
    'try': 'пытаться',
    'app': 'приложение'
}
print('Hello, Gosha')
while True:
    answers = random.sample(list(dictionary.keys()),4)
    ans = random.choice(answers)
    print(f'What is answer {ans}?')
    dict={}
    for i in range(1,5):
        print(f'{i}. {dictionary[answers[i-1]]}')
        dict[i] = dictionary[answers[i-1]]
    answer=int(input('введите номер правильного ответа answer= '))
    print(f'вы ввели вариант ответа {answer}')
    if dict[answer]==dictionary[ans]:
        print('Correct')
    else:
        print('Incorrect. Correct answer is "привет"')
