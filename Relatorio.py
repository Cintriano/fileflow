import os
from datetime import datetime, date

def generate(pasta: str) -> bool | str:
    """Gera os relatorios com base no intervalo de data definido"""
    intervalo: tuple[date,date] = gerar_intervalo_fixo(2025, "q1")
    data_inicio: date = intervalo[0]
    data_fim: date = intervalo[1]

    if not os.path.exists(pasta):
        return "Pasta não Existente"
    for arquivo in os.listdir(pasta):
        caminho_arquivo: str = os.path.join(pasta, arquivo)
        with open(caminho_arquivo, 'r') as arquivo_log:
            for registro in arquivo_log.readlines():
                try:
                    data_registro: date = datetime.strptime(registro[25:32], "%m.%Y").date()
                except Exception as e:
                    continue
                if data_inicio <= data_registro <= data_fim:
                    print(registro)
    return True


def gerar_intervalo_fixo(ano: int, tipo: str) -> tuple[date, date]:
    """Cria os intervalos de data para gerar os relatorios"""
    tipo = tipo.strip().lower()

    trimestres = {
        "t1": (date(ano, 1, 1), date(ano, 3, 31)),
        "t2": (date(ano, 4, 1), date(ano, 6, 30)),
        "t3": (date(ano, 7, 1), date(ano, 9, 30)),
        "t4": (date(ano, 10, 1), date(ano, 12, 31))
    }

    semestres = {
        "s1": (date(ano, 1, 1), date(ano, 6, 30)),
        "s2": (date(ano, 7, 1), date(ano, 12, 31))
    }

    quadrimestres = {
        "q1": (date(ano, 1, 1), date(ano, 4, 30)),
        "q2": (date(ano, 5, 1), date(ano, 8, 31)),
        "q3": (date(ano, 9, 1), date(ano, 12, 31))
    }

    if tipo in trimestres:
        return trimestres[tipo]
    elif tipo in semestres:
        return semestres[tipo]
    elif tipo in quadrimestres:
        return quadrimestres[tipo]
    else:
        raise ValueError("========== Tipo inválido ==========")


def gerar_intervalo_personalisado(data_inicio: str, data_fim: str) -> list[date]:
    """Criar intervalos personalizados"""
    date_list = [data_inicio, data_fim]
    date_list_final: list[date] = []
    for date_0 in date_list:
        data_format: list[str] = date_0.split(".")
        dia = int(data_format[0])
        mes = int(data_format[1])
        ano = int(data_format[2])
        data_inicio_format = date(ano, mes, dia)
        date_list_final.append(data_inicio_format)
    return date_list_final

if __name__ == "__main__":
    caminho = r"C:\Users\danil\OneDrive\Publicação\Upload\Log"
    generate(caminho)