def repeatedString(s, n):
    if s == "a":
        return n
    a_from_s = s.count("a")
    a,b = divmod(n, len(s))
    answer = a_from_s*a + s[:b].count("a")
    return answer

print(repeatedString("aba", 10)) # 7