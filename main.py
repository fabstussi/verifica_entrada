# criar um código que identifica se a entrada é de um CPF ou um CNPJ

from re import fullmatch

entrada = input(
    'Entre com o CPF (XXX.XXX.XXX-XX) ou CNPJ (XX.XXX.XXX/XXXX-XX)'
)
if fullmatch(r'[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}', entrada):
    print('CPF')
elif fullmatch(
    r'[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}', entrada
):
    print('CNPJ')
else:
    print('Não é um CPF ou CNPJ')
