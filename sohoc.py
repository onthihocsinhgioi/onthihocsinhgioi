# Số đối xứng (palindrome)
def doi_xung(n):
    return str(n) == str(n)[::-1]

# Số hoàn hảo (tổng ước = số đó)
def hoan_hao(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n
