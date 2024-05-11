# import os
from datetime import datetime, timedelta

# Solicita ao usuário o código e o horário inicial
codigo = input("Digite o código: ")
horario_inicial = input("Digite o horário inicial (HH:MM): ")

os_pcaa = int(input("Digite a OS do PCAA: "))
os_pcaa = f"{os_pcaa:,}".replace(",", ".")

# os_gpuu = int(input("Digite a OS do GPUU: "))
# os_gpuu = f"{os_gpuu:,}".replace(",", ".")

os_rotunda = int(input("Digite a OS da rotunda: "))
os_rotunda = f"{os_rotunda:,}".replace(",", ".")

os_cabine = int(input("Digite a OS da cabine: "))
os_cabine = f"{os_cabine:,}".replace(",", ".")

class Posicao:
    def __init__(self, posicao , tag, splt_rotunda, splt_cabine):
        self.tag = tag
        self.posicao = posicao
        self.poem = "POEM" + tag
        self.gpuu = "GPUU" + tag
        self.pcaa = "PCAA" + tag
        self.splt_rotunda = "SPLT" + splt_rotunda
        self.splt_cabine = "SPLT" + splt_cabine

class Movel:
    def __init__(self, tag):
        self.tag = tag
class PcaMovel(Movel):
    def __init__(self, tag, num):
        super().__init__(tag)  # Chama o construtor da classe pai
        self.pcaa = "PCAA"
        self.num = num
class GpuMovel(Movel):
    def __init__(self, tag, num):
        super().__init__(tag)  # Chama o construtor da classe pai
        self.gpuu = "GPUU"
        self.num = num

A08 = Posicao("A08", "1001", "1901", "1902")
A06 = Posicao("A06", "1002", "1903", "1904")
A04 = Posicao("A04", "1003", "1905", "1906")
A02 = Posicao("A02", "1004", "1907", "1908") # comentarios

B07 = Posicao("B07", "1005", "1909", "1910")
B09 = Posicao("B09", "1006", "1911", "1912")
B11 = Posicao("B11", "1007", "1913", "1914")
B13 = Posicao("B13", "1008", "1915", "1916")

B02 = Posicao("B02", "1015", "1929", "1930")
B04 = Posicao("B04", "1014", "1927", "1928")
B06 = Posicao("B06", "1013", "1925", "1926")
B08 = Posicao("B08", "1012", "1923", "1924")
B10 = Posicao("B10", "1011", "1921", "1922")
B12 = Posicao("B12", "1010", "1919", "1920")
B14 = Posicao("B14", "1009", "1917", "1918")

C05 = Posicao("C05", "1016", "1931", "1932")
C07 = Posicao("C07", "1017", "1933", "1934")
C09 = Posicao("C09", "1018", "1935", "1936")
C11 = Posicao("C11", "1019", "1937", "1938")
C13 = Posicao("C13", "1020", "1939", "1940")
C15 = Posicao("C15", "1021", "1941", "1942")

C02 = Posicao("C02", "1028", "1955", "1956")
C04 = Posicao("C04", "1027", "1953", "1954")
C06 = Posicao("C06", "1026", "1951", "1952")
C08 = Posicao("C08", "1025", "1949", "1950")
C10 = Posicao("C10", "1024", "1947", "1948")
C12 = Posicao("C12", "1023", "1945", "1946")
C14 = Posicao("C14", "1022", "1943", "1944")

# Criando um objeto usando a classe PcaMovel
pcaa_movel_01 = PcaMovel(tag="1029", num="01")
pcaa_movel_02 = PcaMovel(tag="1030", num="02")
pcaa_movel_03 = PcaMovel(tag="1031", num="03")
pcaa_movel_04 = PcaMovel(tag="1032", num="04")

# Criando um objeto usando a classe GpuMovel
gpuu_movel_01 = GpuMovel(tag="1029", num="01")
gpuu_movel_02 = GpuMovel(tag="1030", num="02")
gpuu_movel_03 = GpuMovel(tag="1031", num="03")
gpuu_movel_04 = GpuMovel(tag="1032", num="04")

# Converte o horário inicial para um objeto datetime
horario = datetime.strptime(horario_inicial, "%H:%M")

def position_equipments(codigo):

    termino1 = horario + timedelta(minutes=29)
    horario2 = termino1 + timedelta(minutes=1)
    termino2 = horario2 + timedelta(minutes=29)
    horario3 = termino2 + timedelta(minutes=1)
    termino3 = horario3 + timedelta(minutes=29)

    equipamentos = {
        "a02": A02, "a04": A04, "a06": A06, "a08": A08,
        "b07": B07, "b09": B09, "b11": B11, "b13": B13,
        "b02": B02, "b04": B04, "b06": B06, "b08": B08, "b10": B10, "b12": B12, "b14": B14,
        "c05": C05, "c07": C07, "c09": C09, "c11": C11, "c13": C13, "c15": C15,
        "c02": C02, "c04": C04, "c06": C06, "c08": C08, "c10": C10, "c12": C12, "c14": C14,
        # Adicione mais códigos e instâncias de Equipamento conforme necessário
    }

    pcasmoveis = {
        "pcamovel01": pcaa_movel_01, "pcamovel02": pcaa_movel_02, "pcamovel03": pcaa_movel_03, "pcamovel04": pcaa_movel_04,
    }

    gpusmoveis = {
        "gpumovel01": gpuu_movel_01, "gpumovel02": gpuu_movel_02, "gpumovel03": gpuu_movel_03, "gpumovel04": gpuu_movel_04,
    }

    pcamovel = pcasmoveis.get(codigo.lower())
    gpumovel = gpusmoveis.get(codigo.lower())
    equipamento = equipamentos.get(codigo.lower())  # Ignora maiúsculas/minúsculas

    if equipamento:
        # os.system('clear')
        print(f"{equipamento.posicao} preventiva mensal\n")
        print(f"{equipamento.pcaa} O.S. {os_pcaa}")
        print(f"Início {horario.strftime('%H:%M')} \nTérmino {termino1.strftime('%H:%M')}")
        print(f"{equipamento.splt_rotunda} O.S. {os_rotunda}")
        print(f"Início {horario2.strftime('%H:%M')} \nTérmino {termino2.strftime('%H:%M')}")
        print(f"{equipamento.splt_cabine} O.S. {os_cabine}")
        print(f"Início {horario3.strftime('%H:%M')} \nTérmino {termino3.strftime('%H:%M')}")

    elif pcamovel:
        # os.system('clear')
        print(f"{pcamovel.pcaa}{pcamovel.tag} PCA móvel {pcamovel.num} preventiva mensal")
        print("")
        print(f"O.S. {os_pcaa}")
        print(f"Início {horario.strftime('%H:%M')} \nTérmino {termino1.strftime('%H:%M')}")

    elif gpumovel:
        # os.system('clear')
        print(f"{gpumovel.gpuu}{gpumovel.tag} GPU móvel {gpumovel.num} preventiva mensal")
        print("")
        print(f"O.S. {os_gpuu}")
        print(f"Início {horario.strftime('%H:%M')} \nTérmino {termino1.strftime('%H:%M')}")

    else:
        print("Opção inválida, saindo do programa...")
        exit()

# Gera e imprime as 3 mensagens com os horários de início e término
position_equipments(codigo)