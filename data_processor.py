def analyze_data(data):
    """Анализирует переданный список чисел."""
    if not data:
        return None

    data_sum = sum(data)
    data_avg = data_sum / len(data)
    data_max = max(data)
    data_min = min(data)

    analysis_result = {
        "sum": data_sum,
        "average": data_avg,
        "max": data_max,
        "min": data_min,
        "size": len(data)
    }
    return analysis_result

# Данные для примера
dataset = [15, 2, 78, 4, 91, 23, 8, 11, 56]
result = analyze_data(dataset)

print("Анализ данных:")
print(f"Набор данных: {dataset}")
print(f"Результат анализа: {result}")
