import pandas as pd

'''series_objeto = pd.Series([1, 7, 9, 13, 17, 99])
print(series_objeto)
series_objeto2 = pd.Series([4, 7, 8, -2], index=['alfa', 'beta', 'teta', 'gama'])
print(series_objeto2)

disciplinas = {'cursos' : ['Matemática', 'Python', 'Java','POO'], 'créditos' : [50, 60, 70, 80], 'requisitos' : [True, False, True, False]}
data = pd.DataFrame(disciplinas)
print(data)

nome_cidade = pd.Series(['Franca', 'São Paulo', 'Ribeirão Preto'])
populacao = pd.Series([100.000, 200.000, 300.000])
mostra = pd.DataFrame({'Cidade' : nome_cidade, 'Populacao' : populacao})
print(mostra)

cidades = ['Franca', 'São Paulo', 'Ribeirão Preto', 'Belo Horizonte', 'Uberlândia']
populacao = [100.000, 200.000, 300.000, 400.000, 500.000]
populacao_cidades = dict(zip(cidades, populacao))
print(populacao_cidades)
print(type(populacao_cidades))
print(populacao_cidades['Franca'])
print('Belo Horizonte' in populacao_cidades)
print('Salvador' in populacao_cidades)
populacao_cidades['Salvador'] = 600.000
print(populacao_cidades)
print('Salvador' in populacao_cidades)
del populacao_cidades['São Paulo']
print(populacao_cidades)
print('São Paulo' in populacao_cidades)

Autor = ['Sun Tzu', 'Fernando Pessoa', 'Thomas Mann', 'João Guimarães']
Livro = ['A Arte da Guerra', 'Poesias Selecionadas', 'A Montanha Mágica', 'Primeiras Estórias']
Ano = [2000, 2004, 2015, 2017]
dados = {'Autor': Autor, 'Livro': Livro, 'Ano': Ano}
autores = pd.DataFrame(dados)
#print(type(autores))
df = pd.DataFrame(autores)
#print(df)
df.to_csv("autores.csv")
autores = pd.read_csv('autores.csv', index_col=0)
#print(autores)
#print(autores.info())
#print(autores.columns)
print(autores.index)'''

california_house = pd.read_csv(r'C:\Users\thull\OneDrive\Documentos\Cursos\california_housing_train.csv')
#print(california_house)
#print(california_house.head())
#print(california_house.describe())
#print(california_house.columns)
print(california_house.index)