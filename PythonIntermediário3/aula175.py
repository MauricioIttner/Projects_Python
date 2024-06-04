# os.listdir para navegar em caminhos
# C:\Users\mauit\Documents\EXEMPLO
# caminho = r'C:\\Users\\mauit\\Documents\\EXEMPLO'
import os
caminho = os.path.join('/Users', 'mauit', 'Documents', 'EXEMPLO')

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    if not os.path.isdir(caminho_completo):
        continue

    for image in os.listdir(caminho_completo):
        print(image)
