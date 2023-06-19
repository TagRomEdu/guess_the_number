from random import randint
from utils import is_valid


print("Добро пожаловать в числовую угадайку!")
def main():
    counter = 1
    n = input("Введите правую границу диапазона для угадывания:\n")

    while not n.isdigit():
        n = input("Введи число, вредина!\n")

    number = randint(1, int(n))

    user_number = input(f"\nИтак, первая попытка.\
    \nВведите целое число от 1 до {n}:\n")

    while True:
        if not is_valid(user_number):
            user_number = input(f"А может быть все-таки введем целое число от 1 до {n}?\n")
        else:
            if int(user_number) == number:
                print(f"\nВы угадали, поздравляем! Количество Ваших попыток: {counter}")
                break
            elif int(user_number) > number:
                counter += 1
                user_number = input("Ваше число больше загаданного, попробуйте еще разок\n")
            else:
                counter += 1
                user_number = input("Ваше число меньше загаданного, попробуйте еще разок\n")


if __name__ == "__main__":
    main()

while True:
    answer = input("Желаете ещё угадать?\n")

    if answer.lower() == 'да':
        main()
    else:
        print("Ну и ладно!")
        break
