import abc
from unittest import TestCase, main

class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if (operacao == None):
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado

class OperacaoFabrica(object):
    def criar(self, operador):
        if (operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()
        elif (operador == 'multiplicacao'):
            return Multiplicacao()
        else:
            return 0

class Operacao(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado

class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado

class Testes(TestCase):
    def test_soma(self):
        calc = Calculadora()
        result = calc.calcular(20,20, 'soma')
        self.assertEqual(result, 40)

    def test_multiplicacao(self):
        calc = Calculadora()
        result = calc.calcular(10,20, 'multiplicacao')
        self.assertEqual(result, 200)

    def test_divisao(self):
        calc = Calculadora()
        result = calc.calcular(200,20, 'divisao')
        self.assertEqual(result, 10)

    def test_subtracao(self):
        calc = Calculadora()
        result = calc.calcular(20,10, 'subtracao')
        self.assertEqual(result, 2)
