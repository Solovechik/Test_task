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


def appearance(intervals):
    lesson_tutor = correct_overlapping(intervals['tutor'])
    lesson_pupil = correct_overlapping(intervals['pupil'])
    overall_time = 0
    for i in range(0, len(lesson_tutor), 2):
        lesson_tutor[i], lesson_tutor[i + 1] = correct_appearance(intervals['lesson'], lesson_tutor[i:i + 2])
    lesson_tutor = [i for i in lesson_tutor if i]  # удаление нулевых значений для предотвращения лишних операций
    for i in range(0, len(lesson_tutor), 2):
        for j in range(0, len(lesson_pupil), 2):
            temp = correct_appearance(lesson_tutor[i:i + 2], lesson_pupil[j:j + 2])
            overall_time += temp[1] - temp[0]
    return overall_time


def correct_overlapping(lst):  # корректировка наложения интервалов
    last_conn = 0
    for i in range(0, len(lst), 2):
        if lst[i] < last_conn < lst[i + 1]:
            lst[i] = last_conn
        if last_conn < lst[i + 1]:
            last_conn = lst[i + 1]
        else:
            lst[i] = lst[i + 1] = 0
    lst = [i for i in lst if i]
    return lst


def correct_appearance(borders, time):  # корректировка времени присутствия относительно заданных границ
    border_s, border_f = borders
    time_s, time_f = time
    start, finish = 0, 0
    if time_s < border_s < time_f:
        start = border_s
    elif border_s <= time_s <= border_f:
        start = time_s
    if border_f <= time_f and start != 0:
        finish = border_f
    elif border_s < time_f < border_f:
        finish = time_f
    return start, finish


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
