from collections import Counter

def analyze_data(data):
    """Анализирует переданный список чисел с расширенной статистикой."""
    if not data or not all(isinstance(x, (int, float)) for x in data):
        return {"error": "Некорректные данные. Ожидается список чисел."}

    sorted_data = sorted(data)
    data_size = len(sorted_data)
    
    # Базовые метрики
    metrics = {
        "sum": sum(sorted_data),
        "average": sum(sorted_data) / data_size,
        "max": max(sorted_data),
        "min": min(sorted_data),
        "range": max(sorted_data) - min(sorted_data),  # Новый показатель: размах
        "size": data_size,
        "sorted": sorted_data
    }

    # Медиана
    mid = data_size // 2
    metrics["median"] = (sorted_data[mid] + sorted_data[~mid]) / 2 if data_size % 2 == 0 else sorted_data[mid]

    # Мода и частота (новый блок)
    freq = Counter(data)
    metrics["mode"] = [k for k, v in freq.items() if v == max(freq.values())]  # Все моды
    metrics["frequency"] = dict(freq.most_common(3))  # Топ-3 самых частых значений

    return metrics

# Тестовые данные с повторениями
dataset = [15, 2, 78, 4, 91, 23, 8, 11, 56, 42, 4, 8]  # Добавлены повторения 4 и 8
result = analyze_data(dataset)

print("Расширенный анализ данных:")
print(f"Исходный набор: {dataset}")
print(f"Отсортированный набор: {result['sorted']}")
print("\nСтатистика:")
for key, value in result.items():
    if key not in ('sorted', 'frequency'):
        print(f"  {key}: {value}")

print("\nТоп-3 частых значений:")
for num, count in result['frequency'].items():
    print(f"  Число {num}: {count} раз(а)")
