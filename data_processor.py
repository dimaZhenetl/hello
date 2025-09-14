def analyze_data(data):
    """Анализирует переданный список чисел."""
    if not data:
        return None

    sorted_data = sorted(data)
    data_size = len(sorted_data)
    data_sum = sum(sorted_data)
    data_avg = data_sum / data_size
    data_max = max(sorted_data)
    data_min = min(sorted_data)

    # Расчет медианы
    if data_size % 2 == 0:
        # Для четного количества элементов
        mid1 = sorted_data[data_size // 2 - 1]
        mid2 = sorted_data[data_size // 2]
        median = (mid1 + mid2) / 2
    else:
        # Для нечетного количества элементов
        median = sorted_data[data_size // 2]

    analysis_result = {
        "sum": data_sum,
        "average": data_avg,
        "max": data_max,
        "min": data_min,
        "median": median,  # Новая метрика!
        "size": data_size,
        "sorted_data": sorted_data  # Новое поле!
    }
    return analysis_result

# Данные для примера (обновленный набор)
dataset = [15, 2, 78, 4, 91, 23, 8, 11, 56, 42]  # Добавили число 42
result = analyze_data(dataset)

print("Расширенный анализ данных:")
print(f"Исходный набор: {dataset}")
print(f"Отсортированный набор: {result['sorted_data']}")
print(f"Результат анализа:")
for key, value in result.items():
    if key != 'sorted_data':  # Чтобы не загромождать вывод
        print(f"  {key}: {value}")
