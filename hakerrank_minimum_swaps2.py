# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def minimumSwaps(arr):
    origin_dict = dict(enumerate(arr, 1))
    reverse_dict = {b: a for a,b in origin_dict.items()}
    cnt = 0
    for i in origin_dict:
        value = origin_dict[i]
        if value != i:
            re_value = reverse_dict[i]
            origin_dict[re_value] = value
            reverse_dict[value] = re_value
            cnt += 1
    return cnt


# print(minimumSwaps([2,3,4,1,5]))
# print(minimumSwaps([4,3,1,2]))
print(minimumSwaps([1,3,5,2,4,6,7]))