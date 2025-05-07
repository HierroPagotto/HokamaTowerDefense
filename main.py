import heapq

# Lê o tabuleiro do arquivo
def ler_tabuleiro(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        linhas = f.read().splitlines()

    if not linhas or len(linhas) < 2:
        raise ValueError("❌ Arquivo de entrada está vazio ou incompleto!")

    n = int(linhas[0])
    if len(linhas[1:]) != n:
        raise ValueError(f"❌ Número de linhas do tabuleiro ({len(linhas)-1}) não corresponde ao tamanho indicado ({n})!")

    tabuleiro = [list(linha.strip()) for linha in linhas[1:]]
    return n, tabuleiro

# Calcula o mapa de dano para cada célula
def calcular_mapa_dano(tabuleiro):
    n = len(tabuleiro)
    dano_mapa = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if tabuleiro[i][j] == 'T':
                for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and tabuleiro[ni][nj] != 'T':
                        dano_mapa[ni][nj] += 10
    return dano_mapa

# Dijkstra para encontrar o menor dano até o destino
def encontrar_melhor_caminho(tabuleiro):
    n = len(tabuleiro)
    dano_mapa = calcular_mapa_dano(tabuleiro)
    movimentos = {'S': (1, 0), 'N': (-1, 0), 'L': (0, 1), 'O': (0, -1)}
    heap = [(dano_mapa[0][0], 0, 0, "")]  # (dano acumulado, x, y, caminho)
    visitado = {}

    while heap:
        dano, x, y, caminho = heapq.heappop(heap)
        if (x, y) in visitado and visitado[(x, y)] <= dano:
            continue
        visitado[(x, y)] = dano

        if (x, y) == (n - 1, n - 1):
            return caminho

        for dir, (dx, dy) in movimentos.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and tabuleiro[nx][ny] != 'T':
                novo_dano = dano + dano_mapa[nx][ny]
                heapq.heappush(heap, (novo_dano, nx, ny, caminho + dir))
    return ""  # Se não encontrou caminho

# Salva o caminho no arquivo de saída
def salvar_saida(nome_arquivo, caminho):
    with open(nome_arquivo, "w") as f:
        f.write(caminho)

# Simula um caminho manual digitado pelo usuário
def simular_caminho(tabuleiro, caminho): 
    movimentos = {'S': (1, 0), 'N': (-1, 0), 'L': (0, 1), 'O': (0, -1)}
    x, y = 0, 0
    n = len(tabuleiro)
    dano_mapa = calcular_mapa_dano(tabuleiro)
    total_dano = dano_mapa[x][y]
    print(f"\n🔍 Início em (0, 0) | Dano inicial: {total_dano}")

    visitados = {(0, 0)}

    for i, direcao in enumerate(caminho): 
        if direcao not in movimentos:
            print(f"❌ Direção inválida '{direcao}' na posição {i+1}")
            return

        dx, dy = movimentos[direcao]
        x += dx
        y += dy

        if not (0 <= x < n and 0 <= y < n):
            print(f"❌ Movimento fora do tabuleiro na posição ({x}, {y})")
            return

        if (x, y) in visitados:
            print(f"❌ Caminho passou por posição repetida em ({x}, {y})")
            return
        visitados.add((x, y))

        if tabuleiro[x][y] == 'T':
            print(f"❌ Caminho passou por cima de uma torre em ({x}, {y})")
            return

        dano = dano_mapa[x][y]
        total_dano += dano
        print(f"Passo {i+1}: {direcao} → posição ({x}, {y}) | Dano: {dano} | Dano acumulado: {total_dano}")

    if (x, y) == (n - 1, n - 1):
        print(f"\n✅ Caminho completo até o destino final! Dano total: {total_dano}")
    else:
        print(f"\n❌ Caminho NÃO chegou ao destino final ({n-1}, {n-1}). Dano total: {total_dano}")

# Executa com um arquivo qualquer
def resolver_instancia(nome_entrada):
    nome_saida = "sol" + nome_entrada[4:-3] + ".out"
    n, tabuleiro = ler_tabuleiro(nome_entrada)

    if tabuleiro[0][0] == 'T' or tabuleiro[n-1][n-1] == 'T':
        raise ValueError("❌ Posição inicial ou final contém uma torre. Caminho impossível!")

    caminho = encontrar_melhor_caminho(tabuleiro)

    if not caminho:
        print("⚠️ Nenhum caminho possível foi encontrado.")
    else:
        print(f"✅ Caminho encontrado: {caminho}")

    salvar_saida(nome_saida, caminho)
    print(f"📝 Solução salva em {nome_saida}")
    return tabuleiro  # retorna para simulação posterior

# Execução principal
if __name__ == "__main__":
    try:
        print("🚀 Iniciando resolução do tabuleiro...")
        nome_entrada = "instgXX.in"  # Altere este nome conforme a instância desejada
        tabuleiro = resolver_instancia(nome_entrada)

        # Permitir teste manual após resolver automaticamente
        print("\n🔎 Teste de caminho manual:")
        caminho_teste = input("Digite um caminho (ex: SSSLLLS): ").strip().upper()
        simular_caminho(tabuleiro, caminho_teste)

    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
