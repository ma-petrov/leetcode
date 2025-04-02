from __future__ import annotations

import collections, heapq, typing


# ---- Решение с использованием встроенной библиотеки heapq ----

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # Подсчет частоты чисел в списке, ключ словаря - число,
        # значение - частота.
        frequency = collections.defaultdict(int)
        for num in nums:
            frequency[num] += 1

        # Возврат top k элементов. Так метод __iter__ словаря возвращает ключи,
        # а метод heapq.nlargest возвращает значения итерируемого объекта, то
        # в качестве итерируемого объекта достаточно передать frequency.
        # Чтобы сортировка в куче выполнялась по значением словаря, в качестве
        # ключе передается функцию, которая по числу (ключу) возвращает его
        # частоту.
        return heapq.nlargest(k, frequency, key=lambda num: frequency[num])
    
        # Вообще, использование key не влияет на асимптотическую сложность
        # (в конкретном случае), но библиотека подмечает, что этот вариант
        # медленнее обычного. В продуктовом коде так скорее всего лучше не
        # делать. В данном решении оставил для красоты.


# ---- Решение без использования библиотеки ----

class Comparable(typing.Protocol):
    # Логика сравнения элементов отделена от реализации кучи, внутри кучи
    # сравнение выполняется операторами "<", ">". Чтобы можно было использовать
    # объекты типа данных в куче, тип должен релизовывать операции сравнения.

    def __lt__(self, other: Comparable) -> bool:
        ...

    def __gt__(self, other: Comparable) -> bool:
        ...


def nlargest(
    n: int,
    iterable: typing.Iterable[Comparable],
    key: callable | None = None,
) -> list[Comparable]:
    # реализация функции nlargest с тем же интерфейсом, что и функция из
    # библиотеки heapq

    assert len(iterable) <= n, "n must be less or equal to iterable length"

    if len(iterable) == n:
        return list(iterable)

    key = key or (lambda x: x)
    heap = list(iterable)

    for index in range(len(heap) // 2 - 1, -1, -1):
        heapify(heap, index, key)
    
    # Так как на каждом уровне в куче данные лежат неупорядочено, после
    # каждого извлечения из кучи нужно заново восстановить кучу и взять
    # самый большой элемент (из корня). Для более эффективного извлечения
    # первый элемент перезаписывается значением последнего, а последний
    # удаляется.
    largest = []
    for _ in range(n):
        largest.append(heap[0])
        heap[0] = heap.pop()
        heapify(heap, 0, key)
    return largest


def heapify(heap: list[Comparable], index: int, key: callable):
    # Восстановление кучи от элемента на позиции index
    
    while True:
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(heap) and key(heap[left]) > key(heap[largest]):
            largest = left

        if right < len(heap) and key(heap[right]) > key(heap[largest]):
            largest = right

        # Если наибольший элемент это корень, восстановление кучи закончено
        if largest == index:
            break

        # Иначе нужно поменять местами корень с наибольшим потомком
        heap[index], heap[largest] = heap[largest], heap[index]

        # Продолжение проверки для изменённого поддерева
        index = largest


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = collections.defaultdict(int)
        for num in nums:
            frequency[num] += 1

        return nlargest(k, frequency, key=lambda num: frequency[num])
