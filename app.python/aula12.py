# aula12 requests - 03/082021

import requests


response = requests.get('https://viacep.com.br/ws/59092280/json/')
print(response.status_code)
print(response.json())
dados_cep = response.json()


if __name__ == '__main__':

    print(f'Meu endereço é: {dados_cep["logradouro"]}\n'
                  f'CEP: {dados_cep["cep"]}\n'
                  f'Bairro: {dados_cep["bairro"]}\n'
                  f'Cidade: {dados_cep["localidade"]}\n'
                  f'UF: {dados_cep["uf"]}')