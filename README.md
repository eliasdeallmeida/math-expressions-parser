# math-expressions-parser
Analisador de expressões matemáticas

## 🧠 Máquina de Turing Simulada — Parser e Resolução de Equações Matemáticas

Este projeto simula o comportamento de uma **Máquina de Turing** que recebe uma **expressão algébrica com incógnita `x`**, valida a sintaxe, resolve a equação e exibe o valor de `x`. Expressões inválidas são rejeitadas.

---

## 📌 Funcionalidades

- ✅ Aceita expressões com incógnita `x`, como:
  - `2x+4-1`
  - `3x - 9 = 0`
  - `x+1=0`
- ❌ Rejeita expressões inválidas ou que não contenham `x`, como:
  - `2+2`
  - `x+`
  - `x + y = 5`

---

## ⚙️ Tecnologias e Bibliotecas

- Python 3
- [SymPy](https://www.sympy.org/) — biblioteca para álgebra simbólica

---

## 🛠 Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/eliasdeallmeida/math-expressions-parser.git
cd math-expressions-parser
