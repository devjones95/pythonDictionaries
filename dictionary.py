# INTRODUÇÃO AOS DICIONÁRIOS EM PYTHON

# Exemplo 1:

pessoa = {'nome': 'João Pedro', 'idade': 28, 'profissão': 'Engenheiro de Dados'}

# Exemplo 2:
# Particularmente, essa forma ao meu ver, é melhor.
pessoa = dict(nome= 'João Pedro ', idade= 28, profissao = 'Engenheiro de Dados')

# Adicionando dados ao dicionário:
pessoa['telefone'] = '1234-4321' # Adicionamos o dado telefone ao nosso dicionário PESSOA

print(pessoa) # {'nome': 'João Pedro ', 'idade': 28, 'profissao': 'Engenheiro de Dados', 'telefone': '1234-4321'}

# Acessando dados individualmente no dicionário:

print(pessoa['nome']) # João Pedro 

print(pessoa['idade']) # 28

print(pessoa['profissao']) # Engenheiro de Dados

print(pessoa['telefone']) # 1234-4321

print(pessoa['nome'] , pessoa['profissao']) # João Pedro Engenheiro de Dados

#===========================================================================================================================

# DICIONÁRIOS ANINHADOS

contatos = {
    'joaopedro@gmail.com': {'nome': 'João Pedro', 'profissao': 'Engenheiro de Dados', 'telefone': '1234-4321'},
    'vitoriaferre@gmail.com': {'nome': 'Vitória Ferre', 'profissao': 'Barbeira', 'telefone': '3465-7434'},
    'sunamitamagalhaes@gmail.com': {'nome': 'Sunamita', 'profissao': 'Analista de BI', 'telefone': '0192-9384'},
    'rodrigoreis@gmail.com': {'nome': 'Rodrigo', 'profissao': 'Especialista em Marketing', 'telefone': '6574-7382'},
}

# Repare acima, dicionários dentro de dicionários

# Acessando dados dentro desses dicionários aninhados:

print(contatos['joaopedro@gmail.com']['telefone']) # A chave de email é a referência, onde dizemos onde se encontra o dado TELEFONE que queremos acessar.

print(contatos['vitoriaferre@gmail.com']['profissao']) # Barbeira

#==================================================================================================================================================================

# USANDO O FOR EM DICIONÁRIOS

for chave , valor in contatos.items():
    print(chave, valor)
    
    
    

