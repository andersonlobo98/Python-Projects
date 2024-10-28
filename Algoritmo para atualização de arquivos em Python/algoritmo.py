#Abra o arquivo que contém a lista de permissões e Leia o conteúdo do arquivo
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open("allow_list.txt", "r") as file:
    ip_addresses = file.read()

#Converta a string em uma lista
ip_addresses = ip_addresses.split()

#Percorra a lista de remoção
for element in remove_list:

#Remova os endereços IP que estão na lista de remoção
    if element in ip_addresses:
        ip_addresses.remove(element)

#Atualize o arquivo com a lista revisada de endereços IP
ip_addresses = "\n".join(ip_addresses)

with open("allow_list.txt", "w") as file:
    file.write(ip_addresses)

