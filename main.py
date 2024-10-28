from utils import *

if __name__ == '__main__':
    nome = get_string("Aluno: ")
    nota1 = get_float("Nota1: ")
    nota2 = get_float("Nota2: ")

    media = (nota1 + nota2) / 2

    print(f"{nome} \t {media:.2f}")