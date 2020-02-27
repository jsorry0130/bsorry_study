def solution(array, commands):
    answer = []
    new_array = []
    for i in commands:
        for j in range(i[0]-1, i[1]):
            new_array.append(array[j])
        new_array.sort()
        answer.append(new_array[i[2]-1])
        new_array.clear()
    return answer
