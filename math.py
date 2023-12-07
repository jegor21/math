import random

print("Добро пожаловать!")
tase = int(input("Выберите сложность (1, 2, 3): "))
mode = input("Выберите действие (+, -, *, /, **): ")
numbr = int(input("Введите количество заданий: ")) 

õige = 0

while numbr > 0: #выбор уровня
    if tase == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif tase == 2:
        num1 = random.randint(10, 50)
        num2 = random.randint(1, 10)
    else:
        num1 = random.randint(50, 100)
        num2 = random.randint(10, 20)

    if mode == '+': #выбор операции
        question = f"{num1} + {num2}"
        õige = num1 + num2
    elif mode == '-':
        question = f"{num1} - {num2}"
        õige = num1 - num2
    elif mode == '*':
        question = f"{num1} * {num2}"
        õige = num1 * num2
    elif mode == '/':
        question = f"{num1} / {num2}"
        õige = num1 / num2
    elif mode == '**':
        question = f"{num1} ** {num2}"
        õige = num1 ** num2

    sanswer = float(input(f"Решите пример: {question} = "))

    if sanswer == õige:
        print("Верно!")
        õige += 1
    else:
        print(f"Неверно. Правильный ответ: {õige}")

    numbr -= 1

v = (õige / (numbr + õige)) * 100

print("Ваша оценка: ", end='')

if v < 60: #% решений
    print("Hinne 2")
elif 60 <= v < 75:
    print("Hinne 3")
elif 75 <= v < 90:
    print("Hinne 4")
else:
    print("Hinne 5")
