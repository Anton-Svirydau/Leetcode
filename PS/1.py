# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]


# def is_valid(s: str) -> bool:
#     # Словарь для хранения соответствующих пар скобок
#     bracket_map = {')': '(', '}': '{', ']': '['}
#     # Стек для проверки правильности вложенности
#     stack = []
#
#     # Проходим по каждому символу в строке
#     for char in s:
#         # Если символ — закрывающая скобка
#         if char in bracket_map:
#             # Берем последний элемент из стека (или None, если стек пуст)
#             top_element = stack.pop() if stack else None
#             # Проверяем соответствие закрывающей скобки с верхней открытой
#             if bracket_map[char] != top_element:
#                 return False
#         else:
#             # Если символ — открывающая скобка, добавляем в стек
#             stack.append(char)
#
#     # Если стек пустой, все скобки корректно закрыты
#     return not stack
#
#
# # Пример использования
# s = "()[]{}"
# print(is_valid(s))  # Вывод: True


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         current = dummy
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next
#         if list1:
#             current.next = list1
#         elif list2:
#             current.next = list2
#         return dummy.next
#
#     def to_linked_list(values):
#         if not values:
#             return None
#         head = ListNode(values[0])
#         current = head
#         for val in values[1:]:
#             current.next = ListNode(val)
#             current = current.next
#         return head
#
#     def to_list(head):
#         result = []
#         while head:
#             result.append(head.val)
#             head = head.next
#         return result
