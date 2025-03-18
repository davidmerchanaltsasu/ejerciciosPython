
def expand(listas: list[str]):

    cadena = "".join([lista[::-1] for lista in listas])
    print(cadena)

def revertir(cadena: str):

    return cadena[::-1]

expand(["cadena1", "cadena2", "cadena3"])
expand(["abc", "abc", "abc"])