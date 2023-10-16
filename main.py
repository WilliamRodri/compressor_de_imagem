import os
from PIL import Image
from datetime import date
import PySimpleGUI as sg


layout = [
    [sg.Text("Selecione uma pasta:")],
    [[sg.FolderBrowse(initial_folder="Área de Trabalho/", key="select_past")]],
    [sg.Button("OK"), sg.Button("Cancelar")]
]

window = sg.Window("Exemplo FolderBrowser", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancelar":
        break
    elif event == "OK":
        selected_folder = values["select_past"]
        print(selected_folder)
        window.close()

window.close()

print("Comprimindo!!!")
data_atual = date.today()
print(selected_folder)
name_pasta_base = f"{data_atual}_{selected_folder}"
nome_pasta = os.path.basename(name_pasta_base)
print(nome_pasta)
if not os.path.exists(nome_pasta):
	os.mkdir(nome_pasta)

dir_lists = os.listdir(selected_folder)

for index in dir_lists:
	directory = f"{selected_folder}/{index}"
	picture = Image.open(directory)
	picture.save(f"{nome_pasta}/compressed_{index}", "JPEG", optimize=True, quality=50)
	os.system("cls")
	print("...")
	
os.system('cls')
print("Os arquivos foram comprimidos")
#files_path('C:/Users/WillBayers/Documents/FACEIRINHA/compressor_imagem')
#picture.save("Compressed_Image"+".jpg","JPEG",optimize=True,quality=50)