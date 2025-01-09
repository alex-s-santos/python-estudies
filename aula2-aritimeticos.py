#Python é fortemente tipado e não aceita mudanças de tipos dinâmicas

numero_inteiro = 100;
numero_flutuante = 10.3;

novo_numero_inteiro = int(numero_flutuante); #convertendo ele vai excluir o que tem depois do ponto flutuante
print(novo_numero_inteiro);
print(type(novo_numero_inteiro));

novo_numero_float = float(numero_inteiro); #Cria uma casa decimal zerada
print(novo_numero_float);
print(type(novo_numero_float));

numero_string = '30';
novo_numero_vindo_da_string = int(numero_string);
print(novo_numero_vindo_da_string);
print(type(novo_numero_vindo_da_string));
#Se for em string e tentar mudar o tipo, ele só muda se for inteiro para inteiro e float para float

#OPERADORES ARITMÉTICOS EM PYTHON   
numero = 5;

print("Operadores Aritméticos");
print(numero + 3); #Soma
print(numero - 3); #Subtração
print(numero * 3); #Multiplicação
print(numero / 3); #Divisão
print(numero % 3); #Módulo
print(numero ** 3); #Exponenciação
print(numero // 3); #Float division (Divide e retira as casas decimais)