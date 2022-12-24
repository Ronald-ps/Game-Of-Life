# Jogo da vida
## Regras:

O universo do Jogo da Vida é uma grade ortogonal bidimensional infinita de células quadradas, cada uma das quais está em um dos dois estados possíveis, viva ou morta (ou povoada e despovoada, respectivamente). Cada célula interage com seus oito vizinhos, que são as células que são adjacentes horizontal, vertical ou diagonalmente. A cada etapa no tempo, ocorrem as seguintes transições:

- Qualquer célula viva com menos de dois vizinhos vivos morre, como se por subpopulação.
- Qualquer célula viva com dois ou três vizinhos vivos passa para a próxima geração.
- Qualquer célula viva com mais de três vizinhos vivos morre, como se por superpopulação.
- Qualquer célula morta com exatamente três vizinhos vivos torna-se uma célula viva, como se por reprodução.


## Lógica de criação desse jogo da vida:

Observando as regras, percebe-se que a lógica do jogo está relacionada ao contexto de vizinhança: Dado o número de vizinhos vivos que uma célula tem, aplicamos alguma regra sobre elas. Ou seja, a "lei" de criação do jogo está em saber quais a célular vivas e quem são seus vizinhos. Cada célula viva tem um total de 8 vizinhos. E duas células distintas podem ter vizinhos em comum. É a partir desse "compartilhamento" de vizinhos que as regras são aplicadas.

### Dedução de regras do jogo:

Supondo uma célula **`Y`** ativa, que tenha uma célula vizinha **`W`**,
uma outra célula **`X`** ativa, que tenha **`W`** como vizinha,
e uma terceira célula **`H`** ativa, que tenha **`W`** como vizinha.

Ora, se **`W`** tem apenas esses vizinhos vivos:
- caso esteja desativa, ela é ativada;
- caso esteja ativa, ela permanece ativa.

Mas supondo que **`W`** tenha uma outra célula viznha , **`K`**, sendo **`K`** ativa (agora **`W`** tem 4 vizinhas):
- se **`W`** está ativa, ela é desativada;
- se **`W`** está desativa, ela permanece desativa.

Mas supondo um terceiro caso, em que **`W`** tenha apenas duas células vizinhas ativas, então:
- se **`W`** está ativa, ela é permanece ativa;
- se **`W`** está desativa, ela permanece desativa;

Com isso, percebe-se a elaboração de 4 regras principais:
- **Células com 1 vizinha ativa ou 0, estarão desativas no próximo momento.**
- **Células com 2 vizinhas ativas permancem com o estado atual**
- **Células com 3 vizinhas ativas, terão estado ativo no próximo momento.**
- **Células com 4 vizinhas ativas, estarão desativas no próximo momento.**

A primeira etapa de criação do jogo, então, é definir: *Como saber quantos vizinhos ativos uma célula tem?*

### Como saber quantos vizinhos ativos uma célula tem?

Pela lógica, teríamos um array bidimensional infinito, logo, sempre existirão mais células inativas do que ativas. Faz mais sentido então observar e deduzir vizinhos em comum de células ativas.

Por exemplo, dada uma célula **`(2, 2)`** ativa (coordenadas cartesianas), eu consigo facilmente saber quem são os 8 vizinhos dessa célula.
- `(1,1)`, `(1,2)`, `(1,3)`, `(2,1)`, `(2,3)`, `(3,1)`, `(3,2)`, `(3,3)`.

Se eu tiver uma outra célula **`(4, 4)`**, ativa, eu também consigo descobrir seus vizinhos.
- `(3,3)`, `(3,4)`, `(3,5)`, `(4,3)`, `(4,5)`, `(5,3)`, `(5,4)`, `(5,5)`

Percebe-se daí dois fatos:

- `(4, 4)` e `(2, 2)` tem a célula `(3,3)` em comum. Logo, `3,3` tem pelo menos dois vizinhos ativos.
- Dada uma célula **`(x, y)`**, suas vizinhas serão aquelas que tem os valores de coordenada com no máximo uma unidade de diferença:
  - `(x , y - 1)`, `(x, y + 1)`,`(x - 1, y)`, `(x + 1, y)`, `(x + 1, y + 1)`, `( x - 1, y - 1)`, `(x + 1, y + 1)` , `(x - 1, y + 1)`, `(x + 1, y - 1)`

Do primeiro fato se deduz que, ao armazenar as coordenadas dos vizinhos de x células, 8 vizinhos pra cada célula, poderíamos contar quantas vezes cada coordenadas (vizinhos) se repete. Então, se uma coordenada `(a, b)` se repete 4 vezes, ela terá pelo menos 4 vizinhas ativas.
E mais, se descrevermos os vizinhos de todas as células ativas em uma tabuleiro, e fizermos essa contagem, teremos os valores absolutos de vizinhos ativos que uma célula tem.

Por exemplo, depois de listarmos os vizinhos das células `(2, 2)` e `(4,4)`, vimos que a célula `(3, 3)` se repete 2 vezes, logo, ela tem pelo menos dois vizinhos ativos.

### Como descrever o estado de uma célula.

Se conseguirmos contar quantos vizinhos ativos uma célula tem, podemos alternar seu estado aplicando as regras do jogo. A aplicação das regras leva em consideração se a célula está ativa ou não, então devemos armazenar esse estado.
Ou seja, para cada célula de um tabuleiro, temos 3 informações:
- estado (ativa ou desativa)
- linha
- coluna

O fato é que estamos observando as células ativas, e a partir delas deduzindo seus vizinhos. Isso nos dá dois conjuntos de células:
- As células que temos certeza que está ativa, e pertecem ao conjunto de células ativas originais.
- As células que não temos certeza de seu estado, que é o conjunto de células vizinhas.

Se uma célula está no primeiro conjunto (ou em ambos), ela é ativa. Se está só no segundo, ela é inativa.

Mas dadas as regras, só estamos interessados no estado atual de células que tem duas vizinhas ativas, ou seja, só é necessário verificar o estado de uma célula se ela aparece duas vezes no segundo conjunto, para termos certeza se adicionamos ou não ela no conjunto de células ativas.
O ideal é que a cada "fase" do jogo, tenhamos um conjunto de células ativas, pois é a partir delas que o jogo se desenrola.


### Como descobrir o próximo estado de uma célula:
Depois de sabermos a quantidade de vizinhos ativos que uma célula tem, só precisamos aplicar as regras de estado.
Mas como aplicar essas regras?
Ora, depois de descrever e contar a quantidade de vizinhos ativos que uma célula tem, teremos 2 conjuntos de informação:
- As células ativas originais (as quais usamos para descobrir os vizinhos)
- As células vizinhas (que podem coincidir ter algumas das células originais) e sua quantidade de vizinhos ativos

Podem existir células que estejam ativas (então contaremos seus vizinhos), mas que não sejam vizinhas de nenhuma outra célula ativa - ou seja, não apareceriam no conjunto de células vizinhas, mas apareceriam no conjunto de células originais.
Por outro lado, podem existir células que ativas - que aparecem no conjunto de células ativas originais, e que também são vizinhas de células ativas - e , por isso, também aparecem no conjunto de células vizinhas.

O ideal é que a cada etapa do jogo, tenhamos um conjunto de células ativas, que deverá ser usada para criar o conjunto de células vizinhas, e a partir do conjunto de células vizinhas deverá ser criado um novo conjunto de células ativas para a próxima etapa, e assim por diante.

Desta forma:
- Se uma célula só aparece no primeiro conjunto, ela não deverá ir para o próximo conjunto de células ativas.
- Se uma célula aparece duas vezes no segundo conjunto, é interessante saber seu estado verificando sua existencia no primeiro (ou seja, se ela é ativa), se sim, ela permanece como ativa (é passada ao próximo conjunto de células ativas).
- Se uma célula aparece apenas 3 vezes no segundo conjunto, ela deverá ir para o conjunto de células ativas.
- Se uma célula aparece mais do que três, ela não deverá ir para o conjunto de células ativas.

***No fim do dia, então, estamos interessados apenas em células que aparecem duas ou três vezes no conjunto de células vizinhas.***


### Partes do jogo:
logo, os passos do jogo são os seguintes:
- ter uma lista de células ativas.
- Gerar uma lista de células vizinhas.
- Descobrir quantas vezes cada célula aparece no conjunto de células vizinhas.
    - se duas, verificamos sua existencia no conjunto de células ativas, e, se existe, passamos para o novo conjunto de células ativas da próxima rodada.
    - se 3, ela é adicionada para a próxima rodada.
    - Qualquer outro caso, não fazemos nada.
