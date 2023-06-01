def study_schedule(permanence_period, target_time):

    if not target_time:
        return None

    count = 0

    for start_time, end_time in permanence_period:
        if not isinstance(start_time, int) or not isinstance(end_time, int):
            return None
        if start_time <= target_time <= end_time:
            count += 1
    return count
