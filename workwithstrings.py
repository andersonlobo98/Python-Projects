####Trabalhando com Strings e listas####

# A notação de colchetes refere-se aos índices colocados entre colchetes
# Os dados String são dados que consistem em uma sequência ordenada de caracteres
# A função str() converte seu objeto de entrada em uma string
# O método .index()  encontra a primeira ocorrência da entrada em uma cadeia de caracteres e retorna sua localização.
# len() retorna o número de elementos em um objeto.
# Localização de substrings com .index(). Uma substring é uma sequência contínua de caracteres em uma string.
# Quando você extrai uma fatia de uma lista, o resultado é outra lista.
# Para alterar um elemento da lista, use sintaxe semelhante à que usaria ao reatribuir uma variável, 
#   mas coloque o elemento específico a ser alterado entre colchetes após o nome da variável. 
# O método .insert() adiciona um elemento em uma posição específica dentro de uma lista. Ele tem dois parâmetros:
#    o primeiro é o índice em que você inserirá o novo elemento e o segundo é o elemento que deseja inserir.
# O método .remove() remove a primeira ocorrência de um elemento específico em uma lista. Ele tem apenas um parâmetro, o elemento que você deseja remover.
# O método .append() adiciona uma entrada ao final de uma lista. Seu único parâmetro é o elemento que deseja adicionar ao final da lista.
# O método .append() é frequentemente usado com loops for para fazer a População de uma lista vazia com elementos
# Semelhante ao método .index() usado para strings, o método .index() usado para listas encontra a primeira ocorrência de um elemento 
#   em uma lista e retorna seu índice. Ele usa o elemento que está sendo pesquisado como entrada.




#Em ambos os casos, a notação de colchetes gera o caractere h quando essa notação de colchetes é colocada dentro de uma função print(). 
# podemos observar isso executando o código:

device_id = "h32rb17"
print("h32rb17"[0])
print(device_id[0])

#talvez precise dos três primeiros caracteres para determinar algo:
print("h32rb17"[0:3])

#verificar se um determinado ID de dispositivo está em conformidade com um padrão de contenção de sete caracteres, 
#poderá usar a função len() e uma condicional.
device_id_length = len("h32rb17")
if device_id_length == 7:
    print("The device ID has 7 characters.")


#O método .index()  encontra a primeira ocorrência da entrada em uma cadeia de caracteres e retorna sua localização.
print("h32rb17".index("r"))

#extrai o elemento com um índice de 2 da variável username_list
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
print(username_list[2])
#ou
print(["elarson", "fgarcia", "tshah", "sgilmore"][2])

# obtém uma fatia de uma lista e explora a sublista que ela retorna:
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
print(username_list[0:3])

# Para alterar um elemento da lista, use sintaxe semelhante à que usaria ao reatribuir uma variável, 
#  mas coloque o elemento específico a ser alterado entre colchetes após o nome da variável:
username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
print("Before changing an element:", username_list)
username_list[1] = "bmoreno"
print("After changing an element:", username_list)

#Método .insert()
username_list = ["elarson", "bmoreno", "tshah", "sgilmore"]
print("Before inserting an element:", username_list)
username_list.insert(2,"wjaffrey")
print("After inserting an element:", username_list)

#Método .remove()
username_list = ["elarson", "bmoreno", "wjaffrey", "tshah", "sgilmore"]
print("Before removing an element:", username_list)
username_list.remove("elarson")
print("After removing an element:", username_list)

#Método .append()
username_list = ["bmoreno", "wjaffrey", "tshah", "sgilmore"]
print("Before appending an element:", username_list)
username_list.append("btang")
print("After appending an element:", username_list)

#Método .append() com loop
numbers_list = []
print("Before appending a sequence of numbers:", numbers_list)
for i in range(10):
    numbers_list.append(i)
print("After appending a sequence of numbers:", numbers_list)


username_list = ["bmoreno", "wjaffrey", "tshah", "sgilmore", "btang"]
username_index = username_list.index("tshah")
print(username_index)

###Expressões Regulares####