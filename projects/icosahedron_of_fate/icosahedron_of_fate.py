import random

answers = ['Бесспорно', 'Мне кажется - да',	'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да',	'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Скорее всего да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
print('Как звоту тебя, ищущий?')
name = input()
print('Привет', name, 'я магический шар, и я знаю ответ на любой твой вопрос.')
while True:
    print('Задавай свой вопрос!')
    input()
    print(random.choice(answers))
    print('Хочешь задать еще вопрос?  да\нет ')
    if input().lower in ['да', 'lf']:
        print('Задавай свой вопрос!')
    else:
        break

