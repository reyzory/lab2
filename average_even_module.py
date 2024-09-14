def average_even(x, y):
    even_numbers = [i for i in range(x, y + 1) if i % 2 == 0]

    if len(even_numbers) == 0:
        return 0  # Якщо немає парних чисел, повертаємо 0

    return sum(even_numbers) / len(even_numbers)