# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 ,610, 987……
def fib_item(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_item(n - 1) + fib_item(n - 2)

def test_fib_item():
    assert fib_item(0) == 0 # 0
    assert fib_item(1) == 1
    assert fib_item(2) == 1
    assert fib_item(3) == 2
    assert fib_item(4) == 3
    assert fib_item(16) == 987
