import math

# Hàm đảo ngược số
def dao_nguoc(n):
    return int(str(n)[::-1])

# Hàm kiểm tra số thân thiện
def than_thien(n):
    dn = dao_nguoc(n)

    if math.gcd(n, dn) == 1:
        return True
    return False

# Nhập a, b
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

dem = 0

print("Cac so than thien:")

for i in range(a, b + 1):
    if than_thien(i):
        print(i, end=" ")
        dem += 1

print("\nSo luong:", dem)
