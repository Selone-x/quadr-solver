def read_coefficients() -> tuple[float, float, float]:
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    return a, b, c


def discriminant(a: float, b: float, c: float) -> float:
    return b * b - 4 * a * c


if __name__ == "__main__":
    a, b, c = read_coefficients()
    print(f"a = {a}, b = {b}, c = {c}")
    d = discriminant(a, b, c)
    print(f"Дискриминант D = {d}")
