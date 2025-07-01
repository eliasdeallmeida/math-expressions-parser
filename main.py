import re
from sympy import symbols, Eq, solve, sympify

class MaquinaTuringEquacao:
    def __init__(self, expressao):
        self.expressao_original = expressao
        self.expressao = expressao.replace(' ', '')
        self.x = symbols('x')

    def validar(self):
        # Deve conter a variável x
        if 'x' not in self.expressao:
            return False
        # Apenas uma incógnita (x) e caracteres permitidos
        return bool(re.fullmatch(r'[0-9xX+\-*/.=()]+', self.expressao))

    def preparar_equacao(self):
        # Se não tiver '=', assume que é igual a 0
        if '=' not in self.expressao:
            self.expressao += "=0"

        # Corrigir multiplicações implícitas: 2x -> 2*x, (2)x -> (2)*x, etc.
        # Ex: 3x → 3*x
        self.expressao = re.sub(r'(\d)(x)', r'\1*\2', self.expressao)
        self.expressao = re.sub(r'(x)(\d)', r'\1*\2', self.expressao)  # x2 → x*2 (por segurança)
        return self.expressao

    def executar(self):
        if not self.validar():
            return f"REJEITADO: Expressão inválida ou não é uma equação com x → {self.expressao_original}"
        try:
            equacao_str = self.preparar_equacao()
            lados = equacao_str.split('=')
            lhs = sympify(lados[0])
            rhs = sympify(lados[1])
            eq = Eq(lhs, rhs)
            resultado = solve(eq, self.x)
            return f"ACEITO: x = {resultado}"
        except Exception as e:
            return f"REJEITADO: Erro ao processar a equação → {e}"

# Testes
expressoes = [
    "2x+4-1",       # aceito: x = -1.5
    "x+1=0",        # aceito: x = -1
    "3x - 9 = 0",   # aceito: x = 3
    "2+2",          # rejeitado
    "x+",           # rejeitado
    "x+y=5",        # rejeitado
]

for e in expressoes:
    mt = MaquinaTuringEquacao(e)
    print(f"Expressão: {e} -> {mt.executar()}")
