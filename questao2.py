import unittest
import re


def verbing(s):
    # SEU CODIGO AQUI
    if len(s) >= 3:
        if s.endswith('ing'):
            s += 'ly'
        else:
            s += 'ing'
    return s


# Dado uma string, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not'
# substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s):
    ocor_not = s.find('not')
    ocor_bad = s.find('bad')

    if ocor_not < ocor_bad:
        resultado = re.sub(r'not.*bad', 'good', s)
        return resultado
    else:
        return s

# Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frente (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a aprte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back


def front_back(a, b):

    comprimento_a = (len(a) + 1) // 2
    comprimento_b = (len(b) + 1) // 2

    a_front = a[:comprimento_a]
    a_back = a[comprimento_a:]
    b_front = b[:comprimento_b]
    b_back = b[comprimento_b:]

    return a_front + b_front + a_back + b_back


class MyTest(unittest.TestCase):

    def test_verbing(self):
        self.assertEqual(verbing('hail'), 'hailing')
        self.assertEqual(verbing('swiming'), 'swimingly')
        self.assertEqual(verbing('do'), 'do')

    def test_not_bad(self):
        self.assertEqual(not_bad('This movie is not so bad'),
                         'This movie is good')
        self.assertEqual(not_bad('This dinner is not that bad!'),
                         'This dinner is good!')
        self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
        self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

    def test_front_back(self):
        self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
        self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
        self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    unittest.main()
