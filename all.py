import math


def main():
    while True:
        print("Введите номер программы ")
        select_program = input()

        if select_program == "1.1":
            print(31, 18, 79)

        elif select_program == "1.2":
            print(47, 52, 150, sep='  ')

        elif select_program == "1.3":
            print(50)
            print(10)

        elif select_program == "1.4":
            print(5)
            print(10)
            print(21)

        elif select_program == "1.5":
            print(1)
            print(2)

        elif select_program == "1.6":
            print(f"{math.pi:.3f}")

        elif select_program == "1.7":
            print(f"{math.e:.1f}")

        elif select_program == "1.8":
            num = input("Введите число:")
            print("Вы вывели число", num)

        elif select_program == "1.9":
            num = input("число:")
            print(num, "вот такое число Вы ввели")

        elif select_program =="1.10":
            name = input("Введите ваше имя: ")
            print(name)

        elif select_program =="1.11" :
            team = input("Введите название футбольной команды: ")
            print(team + " - это чемпион!")

        elif select_program =="1.12" :
            name = input("Введите имя: ")
            print("Привет,", name + "!")

        elif select_program =="1.13" :
            n = int(input("Введите целое число: "))
            print(f"Следующее за числом {n} число - {n + 1}.")
            print(f"Для числа {n} предыдущее число - {n - 1}.")

        elif select_program == "1.14" :
            a = input("Введите первое число: ")
            b = input("Введите второе число: ")
            c = input("Введите третье число: ")
            print(a, b, c, sep="  ")

        elif select_program == "1.15" :
            a = input("Введите первое число: ")
            b = input("Введите второе число: ")
            c = input("Введите третье число: ")
            d = input("Введите четвёртое число: ")
            print(a, b, c, d)

        elif select_program == "1.16" :
            # а) 5 10
            #   7см
            print("5 10")
            print("7см")
            # б) 100t
            #   1949v
            print("100t")
            print("1949v")
            # в) x y
            #   5 y
            print("x y")
            print("5 y")
            

        else:
            print("вы ввели не верное число")


if __name__ == "__main__":
    main()
