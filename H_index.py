
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    avg = citations[round(len(citations)/2)]
    high = 0
    low = 0
    for j in range(avg):
        for i in citations:
            if i <= avg:
                low +=1
            if i >= avg:
                high +=1
        if high >= avg and low <= avg:
            answer = avg
            break
        low = 0
        high = 0
        avg -=1

    return answer
