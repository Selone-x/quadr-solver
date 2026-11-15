def read_coefficients() -> tuple[float, float, float]:
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    return a, b, c


if __name__ == "__main__":
    a, b, c = read_coefficients()
    print(f"a = {a}, b = {b}, c = {c}")
