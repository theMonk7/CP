def tower_of_hanoi(plates: int, s: str, d: str, h: str):
    if plates == 0:
        return
    tower_of_hanoi(plates - 1, s, h, d)
    print(f'{plates} :{s} -> {d}')
    tower_of_hanoi(plates - 1, h, d, s)

def last_occurrence_index(arr:list[int],target:int) -> int:
    if len(arr) == 0:
        return -1
    if arr[len(arr)-1] == target:
        return len(arr) - 1
    return last_occurrence_index(arr[:-1],target)


# tower_of_hanoi(3, "A", "B", "C")
print(last_occurrence_index([1,3,2,4,5,6,4,4,8,9,4,3,2,1,3],4))