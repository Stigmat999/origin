def seasons(a):

    if 2 < a <= 5:
        print("Весна")

    elif 5 < a <= 8:
        print("Лето")

    elif 8 < a <= 11:
        print("Осень")

    elif a == 12 or a <=2:
        print("Зима")

    else:
        print("Неа!")

if __name__ == '__main__':
    seasons(int(input("Введите номер месяца: ")))




