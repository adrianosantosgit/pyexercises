detalhes = {"nome":"Fulana","profissao":"secretaria","idade":30}

try:
    idade = detalhes["idade"]
except:
    raise NameError("Sem valor de idade no registro")
else:
    print(f"Batimento cardiaco maximo é {220 - idade}")
