import math

# Функція для обчислення z = sqrt(m) + 10
def calculate_z(m):
    return math.sqrt(m) + 10

# Функція для знаходження середнього арифметичного всіх парних чисел від x до y
def average_even(x, y):
    even_numbers = [i for i in range(x, y + 1) if i % 2 == 0]

    if len(even_numbers) == 0:
        return 0  # Якщо немає парних чисел, повертаємо 0

    return sum(even_numbers) / len(even_numbers)

if __name__ == "__main__":
    # Введення числа m
    m = float(input("Введіть число m: "))
    z = calculate_z(m)
    print(f"Значення z = sqrt(m) + 10: {z}")

    x = int(input("Введіть початкове значення x: "))
    y = int(input("Введіть кінцеве значення y: "))
    average = average_even(x, y)
    print(f"Середнє арифметичне парних чисел від {x} до {y}: {average}")