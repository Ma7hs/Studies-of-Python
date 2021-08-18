#!/usr/bin/env python
# coding: utf-8

# In[123]:


# Exemplo de tabela

import pandas as pd
tabelaValores = {
    'Curso':['Eletroeletônica', 'Desenvolvimento de Sistemas', 'Mecânica', 'Redes'],
    'Escola_Senai':['Jandira','Barueri','Osasco','Leopoldina'],
    'Vagas':[32,32,64,16],
}

criandoDataFrame = pd.DataFrame(tabelaValores, columns=['Curso','Escola_Senai', 'Vagas'])
criandoDataFrame


# In[124]:


# Se eu quero apenas alguns primeiros elementos do DataFrame .head() -> pode colocar o index que quiser dentro do ()
criandoDataFrame.head(2)


# In[125]:


# Se eu quero apenas os ultimos elementos do meu DataFrame .tail() -> pode colocar a quantidade de elementos finais ()
criandoDataFrame.tail(1)


# In[126]:


# .shape passa as informações sobre o DataFrame (linhas, colunas)
criandoDataFrame.shape


# In[90]:


# .index passa a descrição do index (indice)
criandoDataFrame.index


# In[91]:


# .count faz a contagem de dados não nulos(ausentes)
criandoDataFrame.count


# In[92]:


# Criando uma nova coluna no DataFrame

criandoDataFrame['Nota_aprovacao'] = None
criandoDataFrame['Ausentes'] = None
criandoDataFrame


# In[93]:


# Criando uma nova coluna no DataFrame

criandoDataFrame.drop(columns=['Ausentes'])
criandoDataFrame


# In[102]:


# Percebeu que não mudou nada no DataFrame? Isso se dá pois devemos criar uma nova variavel

# Criando uma nova variavel e aplicando a função .drop(columns=[])

novoData = criandoDataFrame
novoData = novoData.drop(columns=['Ausentes'])
novoData


# In[103]:


# Adicionando valores no DataFrame
novoData.loc[0,'Nota_aprovacao'] = 120
novoData.loc[1,'Nota_aprovacao'] = 150
novoData.loc[2,'Nota_aprovacao'] = 90
novoData.loc[3,'Nota_aprovacao'] = 120
novoData


# In[115]:


# Adicionando uma nova linha no DataFrame

novoData.loc[4,:] = ['Gráfica','Barueri',30,100]
novoData


# In[97]:


# Operadores lógicos 
# & -> and
# | -> or
# 


# In[99]:


# Adicionando filtros para nosso DataFrame com & (filtrando valores)

filtroData = novoData[(novoData['Nota_aprovacao'] >= 120) & (novoData['Vagas'] >= 32)]
filtroData


# In[100]:


# Filtro feito com OR | tendo aprovações diferentes quando usamos o & AND

filtroData = novoData[(novoData['Nota_aprovacao'] > 100) | (novoData['Vagas'] >= 32)]
filtroData


# In[101]:


# Podemos usar o .query() mas não deve-se usar o operador lógico, tem que escrever em forma de string.

novoData.query('Nota_aprovacao>=120 and Vagas >=32')
novoData


# In[108]:


# Desvio padrão entre Vagas e Nota_aprovacao
desvioData = novoData.std(axis=0)
desvioData


# In[109]:


filtroData = novoData[(novoData['Nota_aprovacao'] > 100) | (novoData['Vagas'] >= 32)].std(axis=0)
filtroData


# In[111]:


get_ipython().system('pip install seaborn')


# In[121]:


# Pra salvar o arquivo final, basta utlizar .to_csv()

novoData.to_csv('Tabela_de_Cursos.csv', sep='\t', index=False)


# In[ ]:




