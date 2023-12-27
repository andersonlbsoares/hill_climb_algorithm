# Repositório do Caixeiro Viajante com Algoritmo de Subida de Encosta
### Descrição

- Este repositório contém uma implementação de um algoritmo de subida de encosta para resolver o problema do caixeiro viajante. O código possui oito variações que exploram diferentes abordagens, incluindo variações no estado inicial, tipos de operadores e o uso de randomização.
### Resumo dos Resultados

- Os resultados obtidos a partir da execução das oito variações do código para resolver o problema do caixeiro viajante revelaram diferenças significativas. Em geral, as variações que utilizaram operadores de permutação mostraram desempenho superior em comparação com aquelas que empregaram operadores de substituição. A introdução de randomização também se mostrou benéfica, superando as variações sem randomização.

### Informações Importantes

- Estado Inicial: Variações que adotaram um estado inicial aleatório apresentaram resultados superiores em relação àquelas com um estado inicial ordenado. Mesmo que mais imprevisíveis, os resultados mostraram-se ligeiramente melhores.

- Tipo de Operador: Variações que utilizaram operadores de permutação obtiveram melhor desempenho do que aquelas que empregaram operadores de substituição. Os operadores de permutação permitiram que o algoritmo explorasse mais possibilidades de solução.

- Randomização: Variações que incorporaram randomização apresentaram resultados superiores em comparação com aquelas sem randomização. A randomização contribuiu para evitar que o algoritmo ficasse preso em um local.

- Número de Passos: O número de passos total até a solução final foi utilizado como parâmetro adicional de análise de desempenho, dada a pequena variação de custo entre as soluções.

### Discussões

- Considerando o número de passos até a solução, a Variação 6 (estado inicial aleatório, operador 1, com randomização de circuitos filhos) obteve o melhor resultado. No entanto, ao avaliar o custo do circuito escolhido, essa variação teve a pior média. A Variação 1 (estado inicial ordenado, operador 1, sem randomização de circuitos filhos) teve a pior média de passos, mas juntamente com a Variação 3 (estado inicial ordenado, operador 2, sem randomização de circuitos filhos), alcançou o melhor custo entre todas as variações.

- O menor número de passos encontrado foi 21, obtido pela Variação 6, enquanto o maior foi 88, obtido pela Variação 5. Apesar dessa grande diferença, a média de passos de cada execução não variou significativamente, com uma variação máxima de 16 passos.
### Conclusão

- Os resultados indicam que as variações que utilizaram operadores de permutação e randomização tiveram desempenho superior. A análise do número de passos necessário para alcançar a solução demonstrou uma correlação inversa com o custo, indicando que quanto maior o número de passos, menor será o custo.

- Com base nos resultados, é recomendado que, se o objetivo for obter o menor custo possível, deve-se optar pelo estado inicial ordenado e evitar a randomização dos circuitos filhos. Por outro lado, para obter o melhor desempenho possível, recomenda-se o uso do operador 1 com randomização dos circuitos filhos.
