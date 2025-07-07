
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

print(longest_common_prefix(["flower","flow","flight"]))

def test_plus2():
    prime_nums = []
    for num in range(1, 50):
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            prime_nums.append(num)
    assert plus2(prime_nums) == [3, 4, 5, 7, 9, 13, 15, 19, 21, 25, 31, 33, 39, 43, 45, 49]

def test_multiply2():
    prime_nums = []
    for num in range(1, 50):
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            prime_nums.append(num)
    assert multiply2(prime_nums) == [2, 4, 6, 10, 14, 22, 26, 34, 38, 46, 58, 62, 74, 82, 86, 94]

def test_exponent2():
    prime_nums = []
    for num in range(1, 50):
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            prime_nums.append(num)
    assert exponent2(prime_nums) == [1, 4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209]

def sum2(x, y):
    return x + y
