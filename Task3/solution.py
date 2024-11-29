def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    intervals = sorted(intervals)
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    return merged

def intersect_intervals(intervals1: list[tuple[int, int]], intervals2: list[tuple[int, int]]) -> int:
    i, j = 0, 0
    total_time = 0
    while i < len(intervals1) and j < len(intervals2):
        start1, end1 = intervals1[i]
        start2, end2 = intervals2[j]
        overlap_start = max(start1, start2)
        overlap_end = min(end1, end2)
        if overlap_start < overlap_end:
            total_time += overlap_end - overlap_start
        if end1 < end2:
            i += 1
        else:
            j += 1
    return total_time

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = merge_intervals(
        list(
            (max(lesson_start, start), min(lesson_end, end))
            for start, end in zip(intervals['pupil'][::2], intervals['pupil'][1::2])
            if start < lesson_end and end > lesson_start
        )
    )
    tutor_intervals = merge_intervals(
        list(
            (max(lesson_start, start), min(lesson_end, end))
            for start, end in zip(intervals['tutor'][::2], intervals['tutor'][1::2])
            if start < lesson_end and end > lesson_start
        )
    )
    return intersect_intervals(pupil_intervals, tutor_intervals)