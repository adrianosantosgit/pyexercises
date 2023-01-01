notas = [50,60,70]

def passou(nota):
    if nota>50:
        print("Aprovado")
    else:
        print("Reprovado")
    return

aprovados = [passou(nota) for nota in notas]

print(notas[:])
