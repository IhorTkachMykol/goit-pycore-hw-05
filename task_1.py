def caching_fibonacci():
    cache = {}  # Кеш у замиканні

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Якщо результат уже є в кеші — повертаємо його
        if n in cache:
            return cache[n]

        # Інакше — обчислюємо рекурсивно і зберігаємо в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))   # 55
print(fib(15))   # 610
print(fib(30))   # 832040 — миттєво завдяки кешу
