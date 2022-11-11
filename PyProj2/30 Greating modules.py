"""
import calculator

print(calculator.add(2, 4))
print(calculator.subtract(2, 4))
print(calculator.divide(2, 4))
print(calculator.multiply(2, 4))
"""
# Горният е много по-добър вариант,
# импортва целия калкулатор с всички модули

from calculator import divide
from calculator import add
from calculator import subtract
from calculator import multiply

# тук импортваме всеки модул по отделно

print(divide(2, 4))
print(add(2, 4))
print(subtract(2, 4))
print(multiply(2, 4))