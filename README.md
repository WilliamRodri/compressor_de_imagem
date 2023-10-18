
# Compressor de Imagem

Projeto tem como principal função comprimir imagen(s), onde o seu peso em MegaBit esteja muito alto.

## Ponto Positivo

- Se caso deseja usar o programa sem ter o python na maquina e so baixar o arquivo (.exe).
- Não necessita esperar uploud e download, e so iniciar e escolher a pasta com as imagens e o programa ja comprime.
- Programa leve e bem intuitivo
- Em menos de alguns segundos as imagens ja estão comprimida, e não tem limite de imagens.

## Ponto Negativo
- Caso use Ubuntu, necessitará do Python instalado para iniciar o arquivo "main.py", porque está compilado somente para Windows.
- Programa não está 100%, então está sujeito a alguns bugs ou pequenos erros.

## Como usar

### Caso use Windows, siga o Processo abaixo
0. Caso use o arquivo .exe

1. Baixe e inicie o arquivo "Compressor de Imagem.exe".

2. O Console do seu computador era ser iniciado, aguarde até que um painel grafico seja inciado.

3. Ele pedira que selecione uma pasta, ai voce clica em "Browser" e selecione a pasta com as imagens a serem convertidas.

4. Logo apos escolher, clique em OK e aguarde as imagens serem convertidas.

5. Logo apos finalizar, o console fechará e na pasta que o programa foi inciado, será criado uma pasta com o mesmo nome da pasta que você escolheu e dentro dela estará os arquivos comprimidos, com um nome "compressed_nome do arquivo antes de ser comprimido".

##
0. Caso use o arquivo main.py.

1. Baixe e inicie o arquivo "main.py".

2. Abra o console do seu computador e usando o comando "cd" va até a pasta onde o arquivo main.py está, por exemplo "cd Downloads".

3. Verifique se o python está instalado no seu computador usando o comando "python --version" ou "python3 --version" ou abreviando "-v", se aparecer "Python e um numero de versão" significa que você tem o python instalado.

4. Agora precisa instalar as dependências, verifique se o "pip" está instalado no seu computador usando o comando "pip --version" ou "pip -v", normalmente ele vem junto com o python.

5. Agora instale as dependências.
```bash
pip install Pillow
```
```bash
pip install DateTime
```
```bash
pip install PySimpleGUI
```
6. Logo após finalizado, ainda com o console aberto digite o comando "python main.py" ou "python3 main.py" e aguarde o programa iniciar.

7. Aguarde até que um painel grafico seja inciado.
8. Ele pedira que selecione uma pasta, ai voce clica em "Browser" e selecione a pasta com as imagens a serem convertidas.

9. Logo apos escolher, clique em OK e aguarde as imagens serem convertidas.

10. Logo apos finalizar, o console fechará e na pasta que o programa foi inciado, será criado uma pasta com o mesmo nome da pasta que você escolheu e dentro dela estará os arquivos comprimidos, com um nome "compressed_nome do arquivo antes de ser comprimido".
