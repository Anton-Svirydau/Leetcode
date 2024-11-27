# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]


def is_valid(s: str) -> bool:
    # Словарь для хранения соответствующих пар скобок
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Стек для проверки правильности вложенности
    stack = []

    # Проходим по каждому символу в строке
    for char in s:
        # Если символ — закрывающая скобка
        if char in bracket_map:
            # Берем последний элемент из стека (или None, если стек пуст)
            top_element = stack.pop() if stack else None
            # Проверяем соответствие закрывающей скобки с верхней открытой
            if bracket_map[char] != top_element:
                return False
        else:
            # Если символ — открывающая скобка, добавляем в стек
            stack.append(char)

    # Если стек пустой, все скобки корректно закрыты
    return not stack


# Пример использования
s = "()[]{}"
print(is_valid(s))  # Вывод: True
