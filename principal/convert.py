import os

# Diretório contendo os arquivos de imagem
diretorio = '/home/re/Documents/program/tornado/pixyolo/images'

# Lista todos os arquivos no diretório
arquivos = os.listdir(diretorio)

# Inicializa o contador para nomear as imagens
contador = 1

# Itera sobre cada arquivo no diretório
for arquivo in arquivos:
    # Separa a extensão do arquivo
    nome, extensao = os.path.splitext(arquivo)
    # Constrói o novo nome do arquivo
    novo_nome = f'img_{contador}{extensao}'
    # Renomeia o arquivo
    os.rename(os.path.join(diretorio, arquivo), os.path.join(diretorio, novo_nome))
    # Incrementa o contador
    contador += 1