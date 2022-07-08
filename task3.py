
def appearance(intervals):
    """ Возвращает время общего присутствия ученика и учителя на уроке"""

    # Шаг 1. Поскольку интервалы логин/логуат участника могут накладываться друг на друга, для начала их нужно выровнять
    # Создадим новый список для ученика и учителя, запишем корректные интервалы и обновим их в словаре

    # для ученика:
    pupil = intervals['pupil']
    newpupil = []
    # записываем в новый список первый интервал
    newpupil.append(pupil[0])
    newpupil.append(pupil[1])

    for i in range(2,len(pupil) - 1,2):
        if newpupil[-1] >= pupil[i]:
            newpupil[-1] = max(pupil[i+1],newpupil[-1])
        else:
            newpupil.append(pupil[i])
            newpupil.append(pupil[i+1])

    # для учителя:
    tutor = intervals['tutor']
    newtutor = []
    # записываем в новый список первый интервал
    newtutor.append(tutor[0])
    newtutor.append(tutor[1])

    for i in range(2,len(tutor) - 1,2):
        if newtutor[-1] >= tutor[i]:
            newtutor[-1] = max(tutor[i+1],newtutor[-1])
        else:
            newtutor.append(tutor[i])
            newtutor.append(tutor[i+1])

    intervals['tutor'] = newtutor
    intervals['pupil'] = newpupil

    # Шаг 2. Объединить три списка с интервалами в один список кортежей ('время','маркер логин(1)/логаут(-1)') и отсортировать

    time = []
    for key in intervals:
        for i in range(len(intervals[key])):
            time.append((intervals[key][i], 1 - 2*(i%2)))

    time.sort()

    # Шаг 3. Пройти по общему списку, ведя счетчик по маркерам логин/логаут
    # Счетчик = 3, значит началось пересечение и мы его запоминаем
    # Счетчик = 2 и сохранилось начало пересечения - значит случился логуат участника:
    # вычитаем начало и конец пересечения и обнуляем стартовое значение пересечения

    count = 0
    start = 0
    answer = 0

    for element in time:
        count += element[1]
        if count == 3:
            start = element[0]
        if count == 2 and start != 0:
            answer += element[0] - start
            start = 0

    return answer

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        intervals = test['data']
        test_answer = appearance(intervals)
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'