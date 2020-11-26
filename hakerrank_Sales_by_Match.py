def sockMerchant(n, ar):
    answer = 0
    no_dup_list = list(set(ar))
    for sock in no_dup_list:
        temp = ar.count(sock)
        answer += int(temp/2)
    return answer
