def countingValleys(steps, path):
    now = 0
    answer = 0
    for i in range(steps):
        if path[i] == "U":
            temp = 1
        else:
            temp = -1
        now += temp
        if now == 0 and temp == 1:
            answer += 1
    return answer