# 2
# 1 2 3 4 5 6 7
# 0 5 7 8
# 12 8 7 3 0 5 4
# 8 8 0 3 5 5 6 4 7
def task1() -> list:
    n = int(input())

    set_list = []
    i = 0
    while i != (n * 2):
        set_list.append(set(map(int, input().split())))
        i += 1

    output = list()
    i = 0
    while i != (n * 2):
        output.append(set_list[i+1] - set_list[i])
        i += 2

    return output


def task2():
    # Ввод количества строк
    n = int(input("Введите количество строк: "))

    # Ввод строк с числами
    strings = []
    for i in range(n):
        string = input("Введите строку с числами через запятую и пробел: ")
        strings.append(string)

    # Ввод контрольной суммы
    control_sum = int(input("Введите контрольную сумму: "))

    # Проверка каждой строки
    for string in strings:
        numbers = list(map(int, string.split(", ")))
        first_number = numbers[0]
        sum_of_numbers = sum([num for num in numbers if num > first_number
                              and not any(digit in str(first_number) for digit in str(num))])

        if sum_of_numbers > control_sum:
            print("NO")
        else:
            print("OK")

# task2()


def task3():

    def filter_power_of_two(numbers):
        def is_power_of_two(num):
            while num % 2 == 0:
                num /= 2
            return num == 1

        filtered_numbers = [num for num in numbers if is_power_of_two(num)]
        numbers = [set(filtered_numbers), set(numbers)-set(filtered_numbers)]
        return numbers

    numbers_list = []

    # Input numbers in list
    while True:
        n = input()
        if n != '' and n is not None:
            numbers_list.append(int(n))
        else:
            break

    numbers = filter_power_of_two(numbers_list)

    first_set = numbers[0]
    second_set = numbers[1]

    print(f"""
    Множества:
    A = {first_set} ; B = {second_set}
    Объединение множеств:
    A | B >> {first_set | second_set}
    Пересечение множеств:
    A & B >> {first_set & second_set}
    Вычитание множеств:
    A - B >> {first_set - second_set}
    B - A >> {second_set - first_set}
    Симметричная разность: 
    A ^ B >> {first_set ^ second_set}
    """)


task3()




