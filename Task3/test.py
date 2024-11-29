from solution import appearance

def test_case_1():
    intervals = {
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
    }
    assert appearance(intervals) == 3117

def test_case_2():
    intervals = {
        'lesson': [1594702800, 1594706400],
        'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                  1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                  1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                  1594706524, 1594706524, 1594706579, 1594706641],
        'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
    }
    assert appearance(intervals) == 3577

def test_case_3():
    intervals = {
        'lesson': [1594692000, 1594695600],
        'pupil': [1594692033, 1594696347],
        'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
    }
    assert appearance(intervals) == 3565

# Дополнительные тесты

def test_no_overlap():
    intervals = {
        'lesson': [1000, 2000],
        'pupil': [3000, 4000],
        'tutor': [5000, 6000]
    }
    assert appearance(intervals) == 0

def test_full_overlap():
    intervals = {
        'lesson': [1000, 2000],
        'pupil': [1000, 2000],
        'tutor': [1000, 2000]
    }
    assert appearance(intervals) == 1000

def test_partial_overlap():
    intervals = {
        'lesson': [1000, 3000],
        'pupil': [1500, 2500],
        'tutor': [2000, 3500]
    }
    assert appearance(intervals) == 500

def test_multiple_intervals():
    intervals = {
        'lesson': [1000, 5000],
        'pupil': [1100, 1200, 2000, 2100, 3000, 3500],
        'tutor': [1150, 1250, 2050, 2150, 3050, 3550]
    }
    assert appearance(intervals) == 150

def test_complex_intervals():
    intervals = {
        'lesson': [1000, 10000],
        'pupil': [1500, 2500, 3000, 4000, 4500, 6000],
        'tutor': [2000, 3000, 3500, 5000, 5500, 7000]
    }
    assert appearance(intervals) == 2500