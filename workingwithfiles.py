#Em Python, os nomes dos arquivos ou seus caminhos podem ser processados como dados de cadeia de caracteres e, 
#   como todos os dados de cadeia de caracteres, você deve colocá-los entre aspas.

#Ao abrir um arquivo usando with open(), você deve fornecer uma variável que possa armazenar o arquivo enquanto estiver na instrução with. 
#   você pode fazer isso por meio da palavra-chave "as" seguida do nome da variável. A palavra-chave as atribui uma variável que faz referência a outro objeto. 
#   o código with open("update_log.txt", "r") as file: atribui file para fazer referência à saída da função open() dentro do bloco de código recuado que o segue.
with open("update_log.txt", "r") as file:
    updates = file.read()
print(updates)

#O método .read() converte arquivos em Strings. Isso é necessário para usar e exibir o conteúdo do arquivo que foi lido.
#Para gravar em um arquivo, será necessário abrir o arquivo com "w" ou "a" como o segundo argumento de open().
#with, open() dentro de open pode vim "r", "w" e "a", as = para importações de arquivos
#.read(), write() = para leitura e gravação
#usar o argumento "a" se quiser anexar novas informações ao final de um arquivo existente em vez de escrever sobre ele.
#usar o argumento "w" quando quiser substituir o conteúdo de um arquivo existente.
#"r", que indica que você deseja ler o arquivo
# Os métodos que podem ajudá-lo a analisar seus dados incluem .split() e .join().
# Converter uma lista em uma string, também há um método para isso. O método .join() concatena os elementos de um iterável em uma string.
# usernames.index(2)
#     |       |    |
# variavel  método  argumento
#   