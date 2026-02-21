# Titanic_analise_SCTEC

Análise Exploratória de Dados do Titanic

Este projeto tem como objetivo realizar uma Análise Exploratória de Dados (AED) utilizando a base pública do Titanic. O desenvolvimento foi feito em Python, utilizando as bibliotecas pandas e matplotlib para manipulação e visualização dos dados.

Inicialmente foi realizada a leitura do arquivo CSV com a função read_csv(). Em seguida, foram exibidas as primeiras linhas do dataset utilizando head(), além das informações gerais com info() e estatísticas descritivas com describe().

Depois disso, foi feita a verificação de valores nulos com isnull().sum(). Os valores ausentes da coluna Age foram preenchidos com a média das idades, enquanto os valores ausentes da coluna Embarked foram preenchidos com o valor mais frequente.

Na etapa de análise exploratória, foi calculada a taxa geral de sobrevivência utilizando a média da coluna Survived. Também foram realizados agrupamentos utilizando groupby() para analisar a sobrevivência por sexo e por classe social.

Por fim, foi criado um gráfico de barras utilizando matplotlib para mostrar a quantidade de sobreviventes e não sobreviventes.

A análise permitiu identificar padrões importantes, como maior taxa de sobrevivência entre mulheres e passageiros de classes mais altas.
