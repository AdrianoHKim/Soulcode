# **Projeto Final**

Bem-vindo ao repositório do projeto de análise de dados "PANORAMA NACIONAL DE ENERGIAS RENOVÁVEIS NO BRASIL: RISCOS E OPORTUNIDADES".

Este repositório contém alguns dos recursos utilizados para realizar análises de dados sobre tema proposto no projeto de conclusão do BOOTCAMP MARTECH SOULCODE ACADEMY - ANALISTA DE DADOS - AD2.

Foram utilizadas tecnologias e ferramentas como o Google Colab, Google Cloud Storage, BigQuery, Looker Studio, Power BI, MongoDB, Python Pandas e PySpark para realizar análises avançadas.

## Contexto 
A energia produzida em território nacional tem como principal fonte de geração as usinas hidrelétricas.

Entretanto, nos últimos anos, mais precisamente a partir de 2017, observa-se um crescimento acentuado de energias renováveis. Segundo as consultas realizadas no projeto, em bases de dados públicas, sejam governamentais ou particulares, parte da evolução da energia pode ser explicada pela grande expansão de geração e oferta de energia solar, que a partir de 2017 cresceu em ritmo acelerado, acompanhado também pela energia eólica, de forma mais discreta. 

O Brasil é um país de dimensões continentais e possui extensas áreas tem cobertura de radiação solar por longos meses, como parte do Sudeste e Centro-Oeste e principalmente a região Nordeste, onde concentra-se maior quantidade de usinas e fazendas para geração centralizada de energia solar. Contudo essa não é a única fonte de geração de energia solar. A longa exposição solar em todo o país, somada a incentivos e regulamentações inovadoras, favorecendo a utilização de energias renováveis, em especial, a energia solar fotovoltaica,  permitiu a instalação das mini e micro geradoras de energia solar, denominada de geração distribuída. 

A geração distribuída, principalmente resultante do excedente de energia produzida e da geração compartilhada tem aumentado consideravelmente ano a ano a disponibilidade de energia no sistema de distribuição, barateando a médio prazo os custos de geração, já que os investimentos necessários são diluídos ao longo do tempo.

Destaca-se, aqui, além do alívio à sobrecarga da matriz energética nacional, a utilização de novas tecnologias que demandem uso de energia elétrica, como o abastecimento de pontos de recarga para carros híbridos e elétricos, instalados em diversas localidades. Servindo como complemento de fonte de fornecimento, esses pontos ajudam a ampliar a oferta de local, próxima a pontos de recarga e/ou alta demanda consumidora, consequentemente, a aumentando a utilização de equipamentos e veículos a base de energia limpa.

## Recursos Utilizados
Neste projeto, utilizamos as seguintes ferramentas e tecnologias:

<a href="https://colab.research.google.com/" target="_blank">Google Colab</a>: Uma plataforma de notebooks interativos que permite escrever e executar código Python em um ambiente baseado na nuvem.

<a href="https://cloud.google.com/storage" target="_blank">Google Cloud Storage</a>: Um serviço de armazenamento na nuvem altamente escalável e durável oferecido pelo Google.

<a href="https://cloud.google.com/bigquery" target="_blank">BigQuery</a>: Um serviço de análise de dados que permite executar consultas SQL em conjuntos de dados extremamente grandes.

<a href="https://looker.com/" target="_blank">Looker Studio</a>: Uma plataforma de análise e visualização de dados que facilita a exploração de informações.

<a href="https://powerbi.microsoft.com/" target="_blank">Power BI</a>: Uma ferramenta de análise de negócios da Microsoft que permite visualizar dados e compartilhar insights.

<a href="https://www.mongodb.com/" target="_blank">MongoDB</a>: Um banco de dados NoSQL orientado a documentos, adequado para armazenar e gerenciar grandes volumes de dados não estruturados.

<a href="https://pandas.pydata.org/" target="_blank">Python Pandas</a>: Uma biblioteca popular para análise de dados em Python.

<a href="https://spark.apache.org/docs/latest/api/python/index.html" target="_blank">PySpark</a>: A biblioteca Python para Spark, uma estrutura de processamento de dados em grande escala.

## Notebooks e Scripts
Neste repositório, você encontrará os seguintes notebooks e scripts:

<a href="fator_capacidade_mwh_2015_2023.ipynb" target="_blank">notebook_fator_capacidade</a>: Notebook Colab com processo ETL e análise de dados com Pandas.

<a href="notebook_2_1_cap_instalada_por_regiao_e_uf_tratado.ipynb" target="_blank">notebook_2_1_cap_instalada</a>: Notebook Colab com processo ETL e análise de dados com Pandas.

<a href="2_2_cap_instalada_de_geracao_eletrica_por_fonte_mw.ipynb" target="_blank">notebook_2_2_cap_instalada</a>: Notebook Colab com processo ETL e análise de dados com Pandas.

<a href="notebook_2_3_geracao_eletrica_por_fonte_gwh_tratado.ipynb" target="_blank">notebook_2_3_geracao_eletrica</a>: Notebook Colab com processo ETL e análise de dados com Pandas.

<a href="notebook_geracao_distribuida_pyspark_tratado.ipynb" target="_blank">notebook_geracao_distribuida</a>: Consultas com PySpark.

<a href="notebook_global_horizontal_means_tratad.ipynb" target="_blank">notebook_global</a>: Notebook Colab com processo ETL usando Pandas.

<a href="notebook_iea_ponto_veiculos_pyspark_bruto.ipynb" target="_blank">notebook_iea</a>: Notebook Colab com processo ETL usando Pyspark.

<a href="notebook_mongoDB_carregamento.ipynb" target="_blank">notebook_mongoDB</a>: Notebook Colab com comandos para realização de backup no MongoDB.

## Dicionário e Conjuntos de Dados
Para auxiliar no entendimento do projeto, seguem o dicionário e amostragem do conjunto de dados utilizado:

<a href="documentation" target="_blank">dicionario de dados</a>: Acesso aos dicionários utilizados no processamento de dados já tratados.

<a href="datasets" target="_blank">conjuntos de dados</a>: Amostragem dos conjuntos de dados trabalhados no projeto em formato parquet.

## Licença
Este projeto é licenciado sob a licença MIT.
