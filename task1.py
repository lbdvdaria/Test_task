def findzero(array):
    """ Найдет индекс первого нуля в строке, если его нет - вернет None """

    # обрабатываем случай первого нуля
    if int(array[0]) == 0:
        return 0

    # делаем бинарный поиск
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        num = int(array[middle])
        prevnum = int(array[middle - 1])
        if num == 1:
            left = middle + 1
        elif num == 0 and prevnum == 0:
            right = middle - 1
        elif num == 0 and prevnum == 1:
            return middle


if __name__ == '__main__':
    array = '111111111110000000000000000'
    print(findzero(array))
