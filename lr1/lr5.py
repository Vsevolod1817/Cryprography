# № 8 Реализовать решение квадратичного сравнения по составному модулю.

def jacobi_symbol(a, n):
    """Вычисление символа Якоби (a/n)"""
    if n <= 0 or n % 2 == 0:
        return 0
    j = 1
    if a < 0:
        a = -a
        if n % 4 == 3:
            j = -j
    while a != 0:
        while a % 2 == 0:
            a = a // 2
            if n % 8 in [3, 5]:
                j = -j
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            j = -j
        a = a % n
    if n == 1:
        return j
    else:
        return 0

def inverse_mod(a, m):
    """Нахождение обратного элемента для 'a' по модулю 'm'"""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def quadratic_residue_modulo(d, m):
    """Решение квадратичного сравнения x^2 ≡ d (mod m)"""
    solutions = []
    if jacobi_symbol(d, m) == -1:
        return solutions  # Нет решений
    for x in range(m):
        if (x*x - d) % m == 0:
            solutions.append(x)
    return solutions

# Пример использования:
d = 1
m = 31
print(f"Решения x^2 ≡ {d} (mod {m}): {quadratic_residue_modulo(d, m)}")