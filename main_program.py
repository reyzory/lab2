import math
from average_even_module import average_even  # Імпортуємо функцію з модуля

def calculate_z(m):
    return math.sqrt(m) + 10

if __name__ == "__main__":
    m = float(input("Введіть число m: "))
    z = calculate_z(m)
    print(f"Значення z = sqrt(m) + 10: {z}")

    x = int(input("Введіть початкове значення x: "))
    y = int(input("Введіть кінцеве значення y: "))

    average = average_even(x, y)
    print(f"Середнє арифметичне парних чисел від {x} до {y}: {average}")
