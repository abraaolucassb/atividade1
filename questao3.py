import unittest

# Dado um lista de strings `words`, retornar o total de strings
# se cada palavra for maior ou igual a dois e
# se o primeiro caracter coincidir com o último


def match_ends(words):
    total = [word for word in words if len(word) >= 2 and word[0] == word[-1]]
    return len(total)


# Dado uma lista de strings, retornar uma lista de string ordenadas,
# exceto todo grupo de strings que comece com "x" virá primeiro.
#
# Dica: isto pode ser feito com 2 listas ordenando cada uma delas e
# depois combinado-as. Veja os testes para maiores detalhes.


def front_x(words):
    words_com_x = sorted([word for word in words if word.startswith('x')])
    words_no_x = sorted([word for word in words if not word.startswith('x')])
    return words_com_x + words_no_x

# Dado uma lista de tuplas não vazias, retornar uma lista ordenada
# pelo último elemento de cada tupla.
#
# Dica: use um função personalizada `last()` para extrair
# o último elemento, ela deve ser passada no segundo parâmetro
# da função sorted()


def sort_last(tuples):
    return sorted(tuples, key=last)


def last(a):
    return a[-1]


class MyTest(unittest.TestCase):
    def test_match_ends(self):
        self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
        self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
        self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    def test_front_x(self):
        self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), [
                         'xaa', 'xzz', 'axx', 'bbb', 'ccc'])
        self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), [
                         'xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
        self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), [
                         'xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    def test_sort_last(self):
        self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]), [
                         (2, 1), (3, 2), (1, 3)])
        self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]), [
                         (3, 1), (1, 2), (2, 3)])
        self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [
                         (2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    unittest.main()
