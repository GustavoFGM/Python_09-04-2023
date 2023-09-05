    
'''    
ExercÃ­cio 39 - Enunciado: Crie um dicionÃ¡rio contendo nomes de paÃ­ses e 
suas capitais. PeÃ§a ao usuÃ¡rio para adivinhar a capital de um paÃ­s escolhido aleatoriamente.
'''

import random

paises = {'Brasil': 'BrasÃ­lia', 'EUA': 'Washington', 'FranÃ§a': 'Paris'}
pais = random.choice(list(paises.keys()))
guess = input(f"Qual Ã© a capital de {pais}? ")
if guess == paises[pais]:
    print("Resposta correta!")
else:
    print(f"Resposta incorreta. A capital de {pais} Ã© {paises[pais]}.")

'''
ExercÃ­cio 40 - Enunciado: Crie um dicionÃ¡rio com palavras-chave e suas 
definiÃ§Ãµes. Desafie o usuÃ¡rio a adivinhar uma definiÃ§Ã£o 
a partir de uma palavra-chave.
'''

definicoes = {'python': 'Linguagem de programaÃ§Ã£o de alto nÃ­vel', 'database': 'Conjunto organizado de dados'}
palavra_chave = random.choice(list(definicoes.keys()))
definicao = input(f"Qual Ã© a definiÃ§Ã£o de '{palavra_chave}'? ")
if definicao == definicoes[palavra_chave]:
    print("Resposta correta!")
else:
    print(f"Resposta incorreta. A definiÃ§Ã£o de '{palavra_chave}' Ã© '{definicoes[palavra_chave]}'.")

'''
ExercÃ­cio 41 - Enunciado: Crie um programa de cadastro de funcionÃ¡rios 
utilizando dicionÃ¡rios para armazenar informaÃ§Ãµes como nome, cargo e salÃ¡rio.
'''

empregados = []
while True:
    print("1. Cadastrar funcionÃ¡rio")
    print("2. Listar funcionÃ¡rios")
    print("3. Sair")
    choice = int(input("choice uma opÃ§Ã£o: "))
    
    if choice == 1:
        empregado = {}
        empregado['nome'] = input("Nome: ")
        empregado['cargo'] = input("Cargo: ")
        empregado['salario'] = float(input("SalÃ¡rio: "))
        empregados.append(empregado)
        print("FuncionÃ¡rio cadastrado.")
    elif choice == 2:
        for empregado in empregados:
            print(f"Nome: {empregado['nome']}, Cargo: {empregado['cargo']}, SalÃ¡rio: {empregado['salario']:.2f}")
    elif choice == 3:
        break

'''
ExercÃ­cio 42 - Enunciado: Crie um dicionÃ¡rio com nomes de filmes e seus anos
de lanÃ§amento. PeÃ§a ao usuÃ¡rio para digitar um ano e exiba os filmes lanÃ§ados naquele ano.
'''

filmes = {'Matrix': 1999, 'Senhor dos AnÃ©is': 2001, 'Avatar': 2009}
ano = int(input("Digite um ano: "))
filmes_no_ano = [movie for movie, release_ano in filmes.items() if release_ano == ano]
if filmes_no_ano:
    print(f"Filmes lanÃ§ados em {ano}: {', '.join(filmes_no_ano)}")
else:
    print(f"Nenhum filme lanÃ§ado em {ano}.")
'''
ExercÃ­cio 43 - Enunciado: Crie um dicionÃ¡rio representando uma agenda de compromissos. 
Permita ao usuÃ¡rio adicionar e listar compromissos para um determinado dia.
'''

compromissos = {}
while True:
    print("1. Adicionar compromisso")
    print("2. Listar compromissos")
    print("3. Sair")
    choice = int(input("escolha uma opÃ§Ã£o: "))
    
    if choice == 1:
        date = input("Digite a data (DD/MM/AAAA): ")
        compromisso = input("Digite o compromisso: ")
        if date in compromissos:
            compromissos[date].append(compromisso)
        else:
            compromissos[date] = [compromisso]
        print("Compromisso adicionado.")
    elif choice == 2:
        date = input("Digite a data para istar os compromissos: ")
        compromissos_list = compromissos.get(date, [])
        if compromissos_list:
            print(f"Compromissos em {date}:")
            for idx, compromisso in enumerate(compromissos_list, start=1):
                print(f"{idx}. {compromisso}")
        else:
            print(f"Nenhum compromisso marcado para {date}.")
    elif choice == 3:
        break

'''
ExercÃ­cio 44 - Enunciado: Crie um dicionÃ¡rio com nomes de animais como keys 
e suas caracterÃ­sticas como valores. 
PeÃ§a ao usuÃ¡rio para adivinhar um animal a partir de uma caracterÃ­stica.
'''


animais = {'cachorro': 'late', 'gato': 'mia', 'elefante': 'trumpeta'}
caracteristica = input("Digite uma caracterÃ­stica: ")
matching_animais = [animal for animal, char in animais.items() if char == caracteristica]
if matching_animais:
    print(f"Animais que {caracteristica}: {', '.join(matching_animais)}")
else:
    print(f"Nenhum animal encontrado com a caracterÃ­stica '{caracteristica}'.")

'''
ExercÃ­cio 45 - Enunciado: Crie um dicionÃ¡rio com nomes de pratos de 
diferentes paÃ­ses e suas receitas. 
Permita ao usuÃ¡rio escolher um prato e exibir a receita.
'''

pratos = {'feijoada': 'Receita da feijoada...', 'sushi': 'Receita de sushi...', 'pasta': 'Receita de pasta...'}
prato = input("Digite o nome de um prato: ")
receita = pratos.get(prato, "Prato nÃ£o encontrado")
print(f"Receita de {prato}: {receita}")


'''
ExercÃ­cio 46: - Enunciado: Crie um programa de quiz com perguntas sobre 
capitais de paÃ­ses. 
Use um dicionÃ¡rio para armazenar as perguntas e respostas corretas.
'''

questoes = {'Qual Ã© a capital do Brasil?': 'BrasÃ­lia', 'Qual Ã© a capital dos Estados Unidos?': 'Washington'}
score = 0
for questao, correct_answer in questoes.items():
    user_answer = input(questao + " ")
    if user_answer == correct_answer:
        print("Resposta correta!")
        score += 1
    else:
        print(f"Resposta incorreta. A resposta correta Ã©: {correct_answer}")
print(f"VocÃª acertou {score}/{len(questoes)} perguntas.")


'''
'''
ExercÃ­cio 47 - Enunciado: Crie um dicionÃ¡rio com palavras-chave relacionadas a
um tÃ³pico de interesse. Implemente um sistema de busca para exibir 
informaÃ§Ãµes sobre a palavra-chave inserida pelo usuÃ¡rio.
'''

palavra_keys = {'python': 'Linguagem de programaÃ§Ã£o', 'machine learning': 'TÃ©cnica de aprendizado de mÃ¡quina', 'web development': 'Desenvolvimento de sites'}
pesquisar_termo = input("Digite uma palavra-chave: ")
definicao = palavra_keys.get(pesquisar_termo, "Palavra-chave nÃ£o encontrada")
print(f"{pesquisar_termo}: {definicao}")

'''
ExercÃ­cio 48 - Enunciado: Crie um jogo de adivinhaÃ§Ã£o onde o programa escolhe 
uma palavra e o jogador precisa adivinhar as letras. 
Use um dicionÃ¡rio para controlar as letras corretas e incorretas.
'''

import random

palavras = ['python', 'programming', 'dictionary', 'challenge']
palavra = random.choice(palavras)
correct_letters = set()
letras_incorretas = set()

while len(letras_incorretas) < 6:
    display_palavra = ''.join([letter if letter in correct_letters else '_' for letter in palavra])
    print(f"Palavra: {display_palavra}")
    print(f"Letras incorretas: {', '.join(letras_incorretas)}")
    
    guess = input("Digite uma letra: ")
    if guess in correct_letters or guess in letras_incorretas:
        print("VocÃª jÃ¡ tentou essa letra.")
    elif guess in palavra:
        correct_letters.add(guess)
        if all(letter in correct_letters for letter in palavra):
            print(f"ParabÃ©ns! A palavra era '{palavra}'.")
            break
    else:
        letras_incorretas.add(guess)
else:
    print(f"VocÃª errou muito! A palavra era '{palavra}'.")

'''
ExercÃ­cio 49: - Enunciado: Crie um dicionÃ¡rio com nomes de ingredientees 
e suas quantidades em gramas. PeÃ§a ao usuÃ¡rio para digitar o nome de um ingredientee
e a quantidade desejada, e ajuste o dicionÃ¡rio.
'''

ingredientes = {'farinha': 500, 'aÃ§Ãºcar': 300, 'ovos': 4}
ingrediente = input("Digite o nome do ingredientee: ")
quantidade = int(input("Digite a quantidade desejada (em gramas): "))
ingredientes[ingrediente] = quantidade
print(f"ingrediente '{ingrediente}' atualizado para {quantidade}g.")


'''
ExercÃ­cio 50 - Enunciado: Crie um programa que simule um carrinho de compras. 
Use um dicionÃ¡rio para armazenar os itens e suas quantidades. 
Permita ao usuÃ¡rio adicionar, remover e listar itens do carrinho.
'''

carrinho_de_compras = {}
while True:
    print("1. Adicionar item ao carrinho")
    print("2. Remover item do carrinho")
    print("3. Listar itens do carrinho")
    print("4. Sair")
    choice = int(input("choice uma opÃ§Ã£o: "))
    
    if choice == 1:
        item = input("Digite o nome do item: ")
        quantidade = int(input("Digite a quantidade desejada: "))
        if item in carrinho_de_compras:
            carrinho_de_compras[item] += quantidade
        else:
            carrinho_de_compras[item] = quantidade
        print(f"{quantidade} {item}(s) adicionado(s) ao carrinho.")
    elif choice == 2:
        item = input("Digite o nome do item a ser removido: ")
        if item in carrinho_de_compras:
            del carrinho_de_compras[item]
            print(f"{item} removido do carrinho.")
        else:
            print(f"{item} nÃ£o encontrado no carrinho.")
    elif choice == 3:
        print("Itens no carrinho:")
        for item, quantidade in carrinho_de_compras.items():
            print(f"{item}: {quantidade}")
    elif choice == 4:
        break
'''
ExercÃ­cio 51 - Gerenciamento de Estoque
Enunciado - VocÃª Ã© responsÃ¡vel por desenvolver um sistema de gerenciamento de estoque 
para uma loja. O sistema deve permitir a adiÃ§Ã£o de novos produtos, 
atualizaÃ§Ã£o de quantidades em estoque, venda de produtos e exibiÃ§Ã£o de relatÃ³rios. 
VocÃª deve usar um dicionÃ¡rio para armazenar as informaÃ§Ãµes dos produtos.
 - Implemente as seguintes funcionalidades:
*1* - Adicionar Produto: O usuÃ¡rio pode adicionar um novo produto ao estoque. Cada produto terÃ¡ um nome, preÃ§o unitÃ¡rio e quantidade inicial em estoque.
*2* - Atualizar Estoque: O usuÃ¡rio pode atualizar a quantidade em estoque de um produto existente.
*3* - Vender Produto: O usuÃ¡rio pode registrar uma venda de um produto, diminuindo a quantidade
      em estoque. Se a quantidade vendida for maior que a quantidade em estoque, 
      informe que nÃ£o Ã© possÃ­vel realizar a venda.
*4* - RelatÃ³rio de Estoque: Exiba um relatÃ³rio com todos os produtos, 
      seus preÃ§os e quantidades em estoque.
estoque = {}  # DicionÃ¡rio para armazenar o estoque (nome do produto: {'preÃ§o': X, 'quantidade': Y})
'''
#definicao de funcoes:
    
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    price = float(input("Digite o preÃ§o unitÃ¡rio do produto: "))
    quantity = int(input("Digite a quantidade inicial em estoque: "))
    estoque[nome] = {'preÃ§o': price, 'quantidade': quantity}
    print(f"Produto '{nome}' adicionado ao estoque.")

def atualizar_estoque():
    nome = input("Digite o nome do produto para atualizaÃ§Ã£o: ")
    if nome in estoque:
        nova_quantidade = int(input(f"Atualize a quantidade de '{nome}' em estoque: "))
        estoque[nome]['quantidade'] = nova_quantidade
        print(f"Estoque de '{nome}' atualizado para {nova_quantidade}.")
    else:
        print(f"Produto '{nome}' nÃ£o encontrado no estoque.")

def vender_produto():
    nome = input("Digite o nome do produto vendido: ")
    if nome in estoque:
        quantidade_vendida = int(input(f"Digite a quantidade de '{nome}' vendida: "))
        if quantidade_vendida <= estoque[nome]['quantidade']:
            estoque[nome]['quantidade'] -= quantidade_vendida
            print(f"{quantidade_vendida} unidades de '{nome}' vendidas.")
        else:
            print(f"NÃ£o hÃ¡ quantidade suficiente de '{nome}' em estoque para realizar a venda.")
    else:
        print(f"Produto '{nome}' nÃ£o encontrado no estoque.")

def estoque_relatorio():
    print("RelatÃ³rio de Estoque:")
    for product, info in estoque.items():
        print(f"Produto: {product} | PreÃ§o: R${info['preÃ§o']} | Quantidade em Estoque: {info['quantidade']}")


def linha_separacao():
    return print(' -'*30)


# Menu principal
while True:
    linha_separacao()
    print("\n=== Sistema de Gerenciamento de Estoque ===")
    linha_separacao()
    print("1. Adicionar Produto")
    linha_separacao()
    print("2. Atualizar Estoque")
    linha_separacao()
    print("3. Vender Produto")
    linha_separacao()
    print("4. RelatÃ³rio de Estoque")
    linha_separacao()
    print("5. Sair")
    linha_separacao()
    choice = int(input("choice uma opÃ§Ã£o: "))
    
    if choice == 1:
        adicionar_produto()
    elif choice == 2:
        atualizar_estoque()
    elif choice == 3:
        vender_produto()
    elif choice == 4:
        estoque_relatorio()
    elif choice == 5:
        print("Saindo do sistema.")
        break
    else:
        print("OpÃ§Ã£o invÃ¡lida. choice uma opÃ§Ã£o vÃ¡lida.")

