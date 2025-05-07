# Hokama's Tower Defense 

## 🎮 Objetivo

Neste projeto, implementamos um algoritmo **exato** que encontra o caminho do jogador em um tabuleiro `nxn`, indo da posição inicial `(0, 0)` até a final `(n-1, n-1)` com **o menor dano possível**, evitando torres e sem passar por posições repetidas.

---

## 📁 Entrada

- O programa recebe um arquivo de texto com nome no formato: `instgXX.in`  
  (por exemplo: `instg01.in`, `instg20.in`, `instg99.in`)

- O conteúdo do arquivo segue este formato:
  1. A primeira linha contém o número `n`, que representa o tamanho do tabuleiro (`n x n`)
  2. As próximas `n` linhas representam o tabuleiro, com `n` caracteres em cada linha:
     - `0` → posição livre
     - `T` → posição com torre (não pode ser pisada)

### 🔍 Exemplo de entrada (`inst01.in`)
5
00T00
00TT0
00000
00000
0T000

Neste exemplo:
- O tabuleiro tem tamanho **5x5**
- As torres estão posicionadas nos quadrados marcados com `T`
- O jogador começa na posição `(0, 0)` e deve chegar até `(4, 4)` sem passar por torres e tomando o menor dano possível.

---

## 📤 Saída

- Um arquivo com o nome `solgXX.out`, onde `XX` corresponde ao sufixo da entrada (`instgXX.in` → `solgXX.out`).
- O conteúdo é uma única linha com letras representando as direções:
- `S` → Sul (baixo)  
- `N` → Norte (cima)  
- `L` → Leste (direita)  
- `O` → Oeste (esquerda)

- Exemplo de saída:
SSSLLLLS

---

## 🧠 Funcionamento do Algoritmo

- Usa um algoritmo semelhante ao **Dijkstra** com fila de prioridade (`heapq`) para sempre expandir o caminho com **menor dano acumulado**.
- Calcula o dano a cada movimento com base na presença de torres em diagonais adjacentes.
- Garante que:
- O jogador **não passe por cima de torres**
- **Não visite a mesma célula duas vezes**
- Sempre chegue ao final se for possível (garantido pelo enunciado)

---

## ▶️ Como Executar

1. Coloque o arquivo de entrada `instgXX.in` na mesma pasta do script `main.py`
2. No terminal, execute: python main.py
3. O programa vai gerar automaticamente o arquivo de saída solgXX.out.

## 🧪 Validação Manual

O código permite simular um caminho digitado pelo usuário para verificar:
1. Se ele é válido
2. Se chega ao destino
3. O dano total sofrido

Exemplo:

Digite um caminho: (ex: SSSLLL)
→ O programa irá mostrar passo a passo o dano e se chegou ao destino.

## 📌 Regras Atendidas (Checklist)
 
 ✅ Caminho com menor dano total  
 ✅ Não pisa em torres  
 ✅ Não repete posição  
 ✅ Dano das torres acumulado corretamente  
 ✅ Saída com direções corretas (S, N, L, O)  
 ✅ Arquivos nomeados conforme especificado  
 ✅ Algoritmo exato implementado com fila de prioridade (heapq)  
