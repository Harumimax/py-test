class Calculator:

    def __init__(self):
        self.memory = []
        self.a = 0
        self.b = 0
        self.operations = []

    def add(self, a, b):
        result = a + b
        self.operations.append([a, "+", b, result])
        print(f"{a} + {b} = {result}")

    def subtract(self, a, b):
        result = a - b
        self.operations.append([a, "-", b, result])
        print(f"{a} - {b} = {result}")

    def multiply(self, a, b):
        result = a * b
        self.operations.append([a, "*", b, result])
        print(f"{a} * {b} = {result}")

    def divide(self, a, b):
        result = a / b
        self.operations.append([a, "/", b, result])
        print(f"{a} / {b} = {result}")

    def memorize_result(self):
        for operation in self.operations:
            self.memory.append(operation)
        self.operations = []

    def show_results(self):
        for operation in self.memory:
            print(operation[3])

    def show_memory(self):
        for operation in self.memory:
            print(f"{operation[0]} {operation[1]} {operation[2]} = {operation[3]}")

# создаем объект калькулятора
calc = Calculator()

# выполняем операции
calc.add(6, 3)
calc.subtract(6, 3)
calc.multiply(6, 3)
calc.divide(6, 3)

# сохраняем результат в память калькулятора
calc.memorize_result()

# отображаем результаты операций
calc.show_results()

# отображаем результат, сохраненный в памяти калькулятора
calc.show_memory()