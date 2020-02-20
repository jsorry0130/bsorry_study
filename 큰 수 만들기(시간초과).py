def solution(number, k):
    num_list = list(number)
    #copy_list = num_list.copy()
    idx = 0
    k_num =0
    set = 0
    #print(num_list)
    while(True):
        #print("현재 copyList", num_list)
        #print("현재",num_list[idx],"탐색")
        if k_num == k:
            break
        if idx == len(num_list)-1:
            break
        #print(num_list[idx], "와", num_list[idx + 1], "비교")
        if int(num_list[idx]) < int(num_list[idx+1]):
            num_list.remove(num_list[idx])
            k_num +=1
            idx= 0
            set=1
            #print(num_list[idx],"제거")
        else:
            set = 0
        if set !=1:
            idx +=1

    if k_num !=k:
        for i in range(k_num):
            num_list.pop()

    answer = "".join(num_list)
    return answer