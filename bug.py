def media(valores):
    return sum(valores) / len(valores)   # quebra com lista vazia

def buscar(usuarios, nome):
    for u in usuarios:
        if u["nome"] == nome:
            return u
    # retorna None implicitamente, chamador não trata
