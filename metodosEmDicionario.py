# .CLEAR()

contatos = {
    'joaopedro@gmail.com': {'nome': 'João Pedro', 'profissao': 'Engenheiro de Dados', 'telefone': '1234-4321'},
    'vitoriaferre@gmail.com': {'nome': 'Vitória Ferre', 'profissao': 'Barbeira', 'telefone': '3465-7434'},
    'sunamitamagalhaes@gmail.com': {'nome': 'Sunamita', 'profissao': 'Analista de BI', 'telefone': '0192-9384'},
    'rodrigoreis@gmail.com': {'nome': 'Rodrigo', 'profissao': 'Especialista em Marketing', 'telefone': '6574-7382'},
}

contatos.clear() # .clear() limpa todos os dados presentes dentro do dicionário

print(contatos) # {} vazio

#===========================================================================================================================

# .COPY()

contatos = {
    'joaopedro@gmail.com': {'nome': 'João Pedro', 'telefone': '1234-1234'}
}

copia = contatos.copy() # criamos uma cópia e armazenamos o dicionário original dentro dela
copia['joaopedro@gmail.com'] = {'nome': 'JP', 'telefone': '0978-4656'} # alteramos os valores presentes da nossa cópia

contatos['joaopedro@gmail.com'] # O dicionário original permanece intacto
copia['joaopedro@gmail.com'] # Nossa cópia está criada com os dados que alteramos

print(contatos) # 'joaopedro@gmail.com'] = {'nome': 'João Pedro', 'telefone': '1234-1234'}
print(copia) # 'joaopedro@gmail.com'] = {'nome': 'JP', 'telefone': '0978-4656'}

#============================================================================================================================

# .FROMKEYS()

dict.fromkeys(['nome', 'telefone']) # {'nome': None, 'telefone': None}
# Usado pra criar um dicionário vazio, onde apenas criamos e depois adicionamos os valores quando precisarmos.abs

dict.fromkeys(['nome', 'telefone'], 'vazio') # {'nome': 'vazio', 'telefone': 'vazio}
# Adicionamos posteriormente o valor 'vazio' para integrar nosso dicionário já criado anteriormente

#============================================================================================================================

# .GET()

contatos = {
    'joaopedro@gmail.com': {'nome': 'João Pedro', 'telefone': '1234-1234'}
}

#contatos['chave'] # KeyError, essa chave não existe, então dará KeyError

contatos.get('chave') # None, o get() tenta procurar a chave especificada, que é ineistente, então ele retorna None

contatos.get('chave', {}) # {}, o get() se não achar a chave especificada, retornará um dicionário vazio

contatos.get('joaopedro@gmail.com', {}) # 'joaopedro@gmail.com': {'nome': 'João Pedro', 'telefone': '1234-1234'}
# Nesse último exemplo, o get() encontrou a chave existente em contatos, porém, se euel não achasse, retornaria {}

#============================================================================================================================

# .KEYS()

novo_dicionario = {'a': 100, 1: 'teste', 'b': 'python'}
print(novo_dicionario.keys()) # retorna apenas o nome das chaves do dicionário, ou seja, 'a', 1, 'b'

#=============================================================================================================================

# DEL

contato = {
    'joaopedro@gmail.com': {'nome': 'João Pedro', 'telefone': '1234-1234'},
    'vitoria@gmail.com': {'nome': 'Vitória', 'telefone': '5423-3576'},
    'jaumassis@gmail.com': {'nome': 'Djalma', 'telefone': '0987-9078'}
}

del contato ['joaopedro@gmail.com']['telefone'] # deletemos o 'telefone' da chave 'joaopedro@gmail.com'
print(contato)


#=============================================================================================================================

# COMO VERIFICAR SE DETERMINADO VALOR ESTÁ PRESENTE EM UM DICIONÁRIO?

emails = {
    'joaopedro@gmail.com': {'nome': 'João Pedro', 'telefone': '1234-1234'},
    'vitoria@gmail.com': {'nome': 'Vitória', 'telefone': '5423-3576'},
    'jaumassis@gmail.com': {'nome': 'Djalma', 'telefone': '0987-9078'}
}
# temos nosso dicionário, agora imagine que fosse um dicionário gigantesco, como iríamos validar se um valor está dentro ou não do nosso dicionário?

# Veja como:

resultado = 'joaopedro@gmail.com' in emails # eu tenho o valor 'joaopedro@gmail.com' dentro do meu dicionário emails?
print(resultado) # True >> Ou seja, sim, eu tenho

resultado2 = 'vitoria@gmail.com' in emails # eu tenho o valor 'vitoria@gmail.com' dentro do meu dicionário emails?
print(resultado2) # True >> Sim, temos 

resultado3 = 'rodolfo@gmail.com' in emails # eu tenho o valor 'rodolfo@gmail.com' dentro do meu dicionário emails?
print(resultado3) # False >> Não temos esse valor dentro do nosso dicionário







carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
