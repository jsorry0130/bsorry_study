'''
프로그래머스 탐욕법 > 큰 수 만들기(lEVEL2)

어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
    number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
    k는 1 이상 number의 자릿수 미만인 자연수입니다.
'''

def solution(number, k):
    num_list = list(number) #문자열 number를 리스트로
    stack = [num_list[0]] #스택으로 활용할 리스트 초기화(첫 값은 넣어준다)
    print("문자열 number : ",num_list)
    n_idx = 0 #num_list를 탐색할 인덱스 초기화
    while(True):
        if n_idx == len(num_list)-1:
            break   #인덱스가 num_list의 범위를 넘어 탐색하려하면 탈출
        n_idx +=1
        top = int(stack[-1]) #스택의 탑 초기화
        pnt = int(num_list[n_idx]) # num_list에서의 현재 탐색 원소의 값, 즉 "스택에 넣을 다음 값"초기화,
        if k > 0 and top < pnt: #만약 pnt가 스택 탑보다 작으면
            while top < pnt: #탑 바로 직전 원소도 pnt보다 작을수도있으므로 반복하면서
                print("현재 스택의 탑", top, "이 다음에 들어올",pnt,"보다 작으므로 탑을 제거합니다")
                k -= 1 #실제 제거 전에 k값 감소
                print("현재 k", k)
                stack.pop()
                if len(stack) == 0:
                    break
                top = int(stack[-1]) #탑 제거 후 또 다시 비교를 위한 스택 탑 초기화

                if k == 0:
                    break
            print("다음에 올 값이었던 ", pnt," 추가 합니다")
            stack.append(num_list[n_idx]) #나중에 리스트를 문자열로 합쳐야하므로 추가는 문자형태로
        else:
            print(pnt,"스택에 추가 ")
            stack.append(num_list[n_idx])
        print("현재 스택", stack)
    print(stack)
    # num_list가 일정부분 내림차순이면 k 만큼 제거하기도 전에 탐색이 완료되어
    # k 만큼 다 빼지 못하고 종료될 수 있다.
    if k != 0:
        for i in range(k):
            stack.pop()
    #남은 k 만큼 팝팝
    answer ="".join(stack)
    return answer

'''
number = "4177252841"
k = 4
print(solution(number,k))
'''