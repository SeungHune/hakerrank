def jumpingOnClouds(c):
    check = 0
    answer = 0
    for cloud in c:
        if cloud == 0:
            check += 1
        else:
            check = 0
            answer += 1
        if check == 2:
            answer += 1
            check = 0

    return answer
