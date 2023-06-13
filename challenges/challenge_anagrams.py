def is_anagram(input_first_string, input_second_string):
    if not input_first_string and not input_second_string:
        return '', '', False

    sorted_first_string = ''.join(merge_sort(list(input_first_string.lower())))
    sorted_second_string = ''.join(
        merge_sort(list(input_second_string.lower())))

    return sorted_first_string, sorted_second_string, sorted_first_string == sorted_second_string


def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    left, right = merge_sort(lst[:mid]), merge_sort(lst[mid:])

    merged_list = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged_list.append(left[left_idx])
            left_idx += 1
        else:
            merged_list.append(right[right_idx])
            right_idx += 1

    merged_list.extend(left[left_idx:])
    merged_list.extend(right[right_idx:])

    return merged_list
