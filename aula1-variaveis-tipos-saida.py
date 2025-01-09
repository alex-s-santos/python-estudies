#Comentário de linha
"""
    *Comentário
    *de 
    *multiplas
    *linhas
"""

print("Hello, World!"); #Comando de saída, o ponto e vírgula é opicional

nome = 'Alex'; #string, pode ser com aspas simples ou duplas
idade = 31; #int (number inteiro)
altura = 1.64; #float (com decimais)
gosta_de = "programação"; #convenção é o snake_case para nomes compostos de variveis
masculino = True; #Booleano Verdadeiro ou falso, iniciar sempre com letra maiúscula True ou False

print(f"Olá, eu sou o {nome}, eu tenho: {idade + 1} anos, tenho {altura}m de altura, gosto de: {gosta_de}. Sexo masculino: {masculino}."); #fstring ser para interpolar string com variáveis, inicia com f antes de abrir aspas e coloca o nome da variável entre chaves


gosta_de = "astronomia"; #redeclarando valor de variável
print(f"Olá, eu sou o {nome}, eu tenho: {idade + 1} anos, tenho {altura}m de altura, gosto de: {gosta_de}. Sexo masculino: {masculino}."); 