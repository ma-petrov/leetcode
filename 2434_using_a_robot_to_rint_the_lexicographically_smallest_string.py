# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/


import collections


class Solution:
    def robotWithString(self, string: str) -> str:
        # Минимальная возможная строка это та, которая начинается с "наименшей" буквы. Идея решения заключается в том,
        # что рука робота `stack` должная забирать буквы до тех пор, пока не наткнётся на наименьший символ в остатке.

        output, stack, smallest = [], [], "a"
        counter = collections.Counter(string)

        for letter in string:

            stack.append(letter)
            counter[letter] -= 1

            # Поиск наименьшего символа в оставшейся строке - увеличение smallest до тех пор, пока не встретится буква,
            # которая присутствует в строке (её количество не в счетчике не равно 0)
            while smallest < "z" and counter[smallest] == 0:
                smallest = chr(ord(smallest) + 1)
            
            # Так как в стек могут попадать символы, которые были больше минимального символа на предыдущем шаге, а на
            # текущем шаге меньше нового минимума в оставшейся строке, то они должны быть добавлены в `output` до того,
            # как в `output` попадет текущий минимальный символ в оставшейся строке.
            while stack and stack[-1] <= smallest:
                output.append(stack.pop())
            
        return "".join(output)
