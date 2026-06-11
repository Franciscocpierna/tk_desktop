"""
Contas a Pagar - 200 registros com datas completas
--------------------------------------------------
Campos por registro:
  - id
  - fornecedor
  - categoria
  - valor
  - data_emissao    (quando a NF foi emitida)
  - data_compra     (quando a compra foi efetuada)
  - data_vencimento (quando vence)
  - data_pagamento  (None se ainda nao foi pago)
  - status          ("Em atraso" | "A pagar em dia" | "Pago")
  - mes_compra      (1..12)

Distribuicao alvo:
  - 20% Em atraso
  - 60% A pagar em dia
  - 20% Pago

Gera 5 graficos de barras em ./contas_charts_v2/
Requisitos: pip install matplotlib
"""

import json
import random
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path

import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Configuracao
# ---------------------------------------------------------------------------
random.seed(42)
HOJE = date(2026, 6, 5)
TOTAL = 200

FORNECEDORES = [
    "Alfa Distribuidora", "Beta Industria", "Gamma Servicos", "Delta Logistica",
    "Epsilon Tech", "Zeta Materiais", "Eta Energia", "Theta Telecom",
    "Iota Software", "Kappa Transportes", "Lambda Quimica", "Mi Embalagens",
]
CATEGORIAS = [
    "Materia-prima", "Servicos", "Energia", "Aluguel",
    "Telecom", "Software", "Frete", "Manutencao", "Impostos",
]
SAIDA_DIR = Path("/mnt/documents/contas_charts_v2")
SAIDA_DIR.mkdir(parents=True, exist_ok=True)
'''
# Antes do shuffle:
[
  "Em atraso", "Em atraso", ..., (40 vezes),
  "A pagar em dia", "A pagar em dia", ..., (120 vezes),
  "Pago", "Pago", ..., (40 vezes)
]

'''    


# ---------------------------------------------------------------------------
# Geracao dos registros
# ---------------------------------------------------------------------------
# Quotas exatas: 40 atraso, 120 em dia, 40 pago
# 1. Cria uma lista (pool) com 200 elementos baseados em proporções específicas:
#    - 40 elementos serão "Em atraso" (20%)
#    - 120 elementos serão "A pagar em dia" (60%)
#    - 40 elementos serão "Pago" (20%)
status_pool = (
    ["Em atraso"] * 40
    + ["A pagar em dia"] * 120
    + ["Pago"] * 40
)

# 2. Embaralha a lista original diretamente na memória (in-place).
#    Isso garante que a ordem dos status seja completamente aleatória,
#    mas mantendo a proporção exata de cada um (40, 120, 40).
random.shuffle(status_pool)


contas = []
for i in range(1, TOTAL + 1):
    status = status_pool[i - 1]
    fornecedor = random.choice(FORNECEDORES)
    categoria = random.choice(CATEGORIAS)
    valor = round(random.uniform(150, 8500), 2)

    # data_compra ao longo dos ultimos ~5 meses
    dias_atras_compra = random.randint(5, 150)
    data_compra = HOJE - timedelta(days=dias_atras_compra)
    # emissao 0-3 dias apos a compra
    data_emissao = data_compra + timedelta(days=random.randint(0, 3))
    # prazo padrao 30 dias (com variacao)
    prazo = random.choice([15, 21, 28, 30, 30, 30, 45, 60])
    data_vencimento = data_emissao + timedelta(days=prazo)

    data_pagamento = None
    if status == "Pago":
        # pago ate o vencimento (ou ate 5 dias antes)
        data_pagamento = data_vencimento - timedelta(days=random.randint(0, 5))
        if data_pagamento > HOJE:
            data_pagamento = HOJE - timedelta(days=1)
    elif status == "Em atraso":
        # vencimento ja passou e nao foi pago -> force vencimento < hoje
        if data_vencimento >= HOJE:
            data_vencimento = HOJE - timedelta(days=random.randint(3, 40))
    else:  # A pagar em dia
        # vencimento ainda no futuro
        if data_vencimento <= HOJE:
            data_vencimento = HOJE + timedelta(days=random.randint(2, 30))

    contas.append({
        "id": i,
        "fornecedor": fornecedor,
        "categoria": categoria,
        "valor": valor,
        "data_emissao": data_emissao.isoformat(),
        "data_compra": data_compra.isoformat(),
        "data_vencimento": data_vencimento.isoformat(),
        "data_pagamento": data_pagamento.isoformat() if data_pagamento else None,
        "status": status,
        "mes_compra": data_compra.month,
    })

# Salva JSON
json_path = SAIDA_DIR / "contas_pagar.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(contas, f, ensure_ascii=False, indent=2)

# ---------------------------------------------------------------------------
# Resumo
# ---------------------------------------------------------------------------
cont_status = Counter(c["status"] for c in contas)
print("Distribuicao de status:")
for k, v in cont_status.items():
    print(f"  {k:18s} {v:4d}  ({v/TOTAL:.0%})")

# ---------------------------------------------------------------------------
# Graficos
# ---------------------------------------------------------------------------
CORES_STATUS = {
    "Em atraso": "#d9534f",
    "A pagar em dia": "#f0ad4e",
    "Pago": "#5cb85c",
}

def salvar(fig, nome):
    caminho = SAIDA_DIR / nome
    fig.tight_layout()
    fig.savefig(caminho, dpi=130)
    plt.close(fig)
    print(f"  salvo: {caminho}")

# # Grafico 1 - Status (quantidade)
# fig, ax = plt.subplots(figsize=(8, 5))
# labels = list(cont_status.keys())
# valores = [cont_status[l] for l in labels]
# cores = [CORES_STATUS[l] for l in labels]
# barras = ax.bar(labels, valores, color=cores, edgecolor="black")
# for b, v in zip(barras, valores):
#     ax.text(b.get_x() + b.get_width()/2, v + 1, f"{v}\n({v/TOTAL:.0%})",
#             ha="center", fontweight="bold")
# ax.set_title("Contas a Pagar - Quantidade por Status (200 registros)")
# ax.set_ylabel("Quantidade")
# ax.set_ylim(0, max(valores) * 1.18)
# #salvar(fig, "g1_status_qtd.png")
# plt.show()

# ==============================================================================
# GRÁFICO 1 - STATUS (QUANTIDADE)
# ==============================================================================

# 1. Configuração da Janela e Área de Desenho:
# plt.subplots() cria dois objetos essenciais:
#   - 'fig': A janela/página em branco (objeto Figure) que conterá tudo.
#   - 'ax': O quadro interno (objeto Axes) onde as barras e eixos serão desenhados.
# 'figsize=(8, 5)' define o tamanho dessa janela: 8 polegadas de largura por 5 de altura.
fig, ax = plt.subplots(figsize=(8, 5))

# 2. Extração dos Rótulos (Labels):
# Pega as chaves do dicionário/Counter 'cont_status' (ex: ["A pagar em dia", "Em atraso", "Pago"])
# e as converte explicitamente em uma lista de strings para serem usadas no eixo X.
labels = list(cont_status.keys())

# 3. Mapeamento de Valores:
# Cria uma lista com as quantidades numéricas correspondentes a cada status.
# É uma "compreensão de lista" (list comprehension) que busca no Counter o valor de cada label.
# Resultado ex: [120, 40, 40]
valores = [cont_status[l] for l in labels]

# 4. Mapeamento de Cores Personalizadas:
# Cria uma lista de cores buscando as chaves dentro de um dicionário chamado 'CORES_STATUS'.
# Isso garante que a barra "Pago" use sempre a cor definida para pago (ex: verde), "Em atraso" use vermelho, etc.
cores = [CORES_STATUS[l] for l in labels]

# 5. Desenho das Barras Verticais:
# ax.bar() renderiza as colunas na tela cruzando os 'labels' (eixo X) com os 'valores' (eixo Y).
#   - 'color=cores': Aplica a lista de cores criada no passo anterior para cada barra.
#   - 'edgecolor="black"': Desenha um contorno preto fino ao redor de cada barra, melhorando o acabamento.
# O resultado é guardado na variável 'barras' (uma coleção de objetos visuais do Matplotlib).
barras = ax.bar(labels, valores, color=cores, edgecolor="black")

# 6. Laço de Repetição para Adicionar Rótulos de Dados:
# O comando zip() junta a lista de objetos visuais ('barras') com a lista de números ('valores').
# O loop 'for' passa por cada par (b = objeto da barra, v = número da quantidade) um por um.
for b, v in zip(barras, valores):
    
    # 7. O Comando que Escreve o Texto no Gráfico:
    # ax.text(X, Y, texto, ...) desenha um texto flutuante em coordenadas cartesianas específicas:
    #   - Posição X: 'b.get_x() + b.get_width()/2' calcula o início da barra horizontalmente e soma
    #     metade da sua largura, encontrando o centro exato da coluna.
    #   - Posição Y: 'v + 1' pega a altura máxima da barra e soma 1 unidade, fazendo o texto flutuar logo acima dela.
    #   - Texto: f"{v}\n({v/TOTAL:.0%})" monta uma f-string com o valor bruto, quebra a linha (\n) 
    #     e calcula a porcentagem na hora (:.0% transforma 0.60 em 60%).
    #   - 'ha="center"': Alinha o texto horizontalmente pelo centro dele mesmo.
    #   - 'fontweight="bold"': Aplica o estilo negrito na fonte do texto para dar destaque.
    ax.text(b.get_x() + b.get_width()/2, v + 1, f"{v}\n({v/TOTAL:.0%})",
            ha="center", fontweight="bold")

# 8. Configuração do Título Principal:
# Adiciona o texto do título centralizado no topo do quadro do gráfico.
ax.set_title("Contas a Pagar - Quantidade por Status (200 registros)")

# 9. Etiqueta do Eixo Y:
# Escreve o texto indicador na vertical ao lado esquerdo do gráfico, informando o que a escala representa.
ax.set_ylabel("Quantidade")

# 10. Ajuste de Limite do Eixo Y (Teto do Gráfico):
# Define onde o eixo vertical começa (0) e termina.
# 'max(valores) * 1.18' pega o maior valor (ex: 120) e adiciona uma margem de 18% para cima (vai para ~141).
# Isso cria um "respiro visual" indispensável para que os textos do topo não batam na borda ou fiquem cortados.
ax.set_ylim(0, max(valores) * 1.18)

# 11. Linha de Salvamento (Desativada):
# Está comentada com '#'. Se ativada, a função exportaria o gráfico atual como uma imagem física PNG
# na pasta de saída do projeto antes de exibi-lo na tela.
#salvar(fig, "g1_status_qtd.png")

# 12. Renderização Final:
# Interrompe a execução do script Python e abre a janela interativa na tela do computador do usuário,
# exibindo o gráfico desenhado com todas as suas barras, cores, títulos e textos posicionados.
plt.show()

# # Grafico 2 - Valor por status
# valor_por_status = defaultdict(float)
# for c in contas:
#     valor_por_status[c["status"]] += c["valor"]
# fig, ax = plt.subplots(figsize=(8, 5))
# labels = list(valor_por_status.keys())
# valores = [valor_por_status[l] for l in labels]
# cores = [CORES_STATUS[l] for l in labels]
# barras = ax.bar(labels, valores, color=cores, edgecolor="black")
# for b, v in zip(barras, valores):
#     ax.text(b.get_x() + b.get_width()/2, v + max(valores)*0.01,
#             f"R$ {v:,.0f}".replace(",", "."), ha="center", fontweight="bold")
# ax.set_title("Valor Total (R$) por Status")
# ax.set_ylabel("Valor (R$)")
# plt.show()
# #salvar(fig, "g2_valor_status.png")

# ==============================================================================
# GRÁFICO 2 - VALOR POR STATUS (EM REAIS)
# ==============================================================================

# 1. Cria um dicionário especial (defaultdict) focado em números decimais (float).
# O 'defaultdict(float)' é excelente porque se um status ainda não existir no dicionário,
# ele cria o status automaticamente com o valor zero (0.0), evitando erros no código.
valor_por_status = defaultdict(float)

# 2. Laço de repetição (for) para acumular os valores financeiros:
# Ele passa por cada conta dentro da lista 'contas', busca o status daquela conta
# e soma o 'valor' dela ao total acumulado daquele status específico.
for c in contas:
    valor_por_status[c["status"]] += c["valor"]

# 3. Cria a janela do gráfico (fig) e a área de desenho interna (ax) no tamanho 8x5 polegadas.
fig, ax = plt.subplots(figsize=(8, 5))

# 4. Extrai os nomes dos status acumulados (ex: ["A pagar em dia", "Pago", "Em atraso"]) em formato de lista.
labels = list(valor_por_status.keys())

# 5. Cria uma lista com a soma total em dinheiro para cada um dos status presentes em 'labels'.
valores = [valor_por_status[l] for l in labels]

# 6. Mapeia e cria a lista de cores correspondente para cada barra usando o dicionário 'CORES_STATUS'.
cores = [CORES_STATUS[l] for l in labels]

# 7. Renderiza as colunas verticais na tela cruzando os status (eixo X) com os valores em Reais (eixo Y).
barras = ax.bar(labels, valores, color=cores, edgecolor="black")

# 8. Laço 'for' usando o 'zip()' para combinar cada objeto de barra com o seu respectivo valor somado.
for b, v in zip(barras, valores):
    
    # 9. O comando que desenha o texto financeiro no topo de cada barra:
    #   - Posição X: Centraliza o texto calculando a quina da barra + metade da sua largura.
    #   - Posição Y: 'v + max(valores)*0.01' faz o texto flutuar acima da barra. Em vez de somar um número fixo (como +1),
    #     ele calcula 1% da maior barra do gráfico. Isso garante que a folga seja proporcional ao tamanho do gráfico.
    #   - Formatação: f"R$ {v:,.0f}".replace(",", ".") faz um truque. Primeiro, formata o número com vírgula para milhares
    #     e sem centavos (:,.0f). Depois, o .replace(",", ".") troca essa vírgula americana por um ponto, gerando "R$ 15.420".
    #   - 'ha="center"' e 'fontweight="bold"': Centraliza o texto horizontalmente e aplica o negrito.
    ax.text(b.get_x() + b.get_width()/2, v + max(valores)*0.01,
            f"R$ {v:,.0f}".replace(",", "."), ha="center", fontweight="bold")

# 10. Define o título principal do gráfico na tela.
ax.set_title("Valor Total (R$) por Status")

# 11. Define o rótulo do eixo vertical Y indicando que a escala é financeira (Reais).
ax.set_ylabel("Valor (R$)")

# 12. Executa a máquina de estados e abre a janela com o gráfico completo na tela do usuário.
plt.show()

# 13. Linha comentada: Se ativada, salvaria a imagem do gráfico de valores como um arquivo PNG.
#salvar(fig, "g2_valor_status.png")

# # Grafico 3 - Compras por mes (data_compra)
# meses_nome = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
# por_mes = Counter(c["mes_compra"] for c in contas)
# meses_ord = sorted(por_mes.keys())
# vals = [por_mes[m] for m in meses_ord]
# fig, ax = plt.subplots(figsize=(9, 5))
# barras = ax.bar([meses_nome[m-1] for m in meses_ord], vals,
#                 color="#4a90e2", edgecolor="black")
# for b, v in zip(barras, vals):
#     ax.text(b.get_x() + b.get_width()/2, v + 0.5, str(v),
#             ha="center", fontweight="bold")
# ax.set_title("Compras por Mes (data da compra)")
# ax.set_ylabel("Quantidade de compras")
# plt.show()
# #salvar(fig, "g3_compras_mes.png")

# ==============================================================================
# GRÁFICO 3 - COMPRAS POR MÊS (EVOLUÇÃO TEMPORAL)
# ==============================================================================

# 1. Cria uma lista de mapeamento com os nomes dos meses abreviados em português.
# Ela serve para substituir os números (1 a 12) por texto legível no gráfico.
meses_nome = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]

# 2. Utiliza o 'Counter' para contar a quantidade de compras feitas em cada mês.
# O miolo extrai o número do mês (ex: 1 para Janeiro, 2 para Fevereiro) de cada conta.
# Resultado ex: Counter({6: 25, 1: 14, 3: 18...}) - os meses vêm bagunçados.
por_mes = Counter(c["mes_compra"] for c in contas)

# 3. Garante a ordem cronológica correta:
# O método sorted() pega as chaves do Counter (os números dos meses presentes)
# e as coloca em ordem crescente. Isso impede que Fevereiro apareça antes de Janeiro.
# Resultado ex: [1, 2, 3, 4, 5, 6...]
meses_ord = sorted(por_mes.keys())

# 4. Cria a lista de quantidades de compras seguindo a ordenação rigorosa dos meses feita acima.
vals = [por_mes[m] for m in meses_ord]

# 5. Configura a janela do gráfico (fig) e a área de desenho (ax) com um tamanho ligeiramente
# mais largo (9x5 polegadas) para acomodar os 12 meses sem esmagar o texto.
fig, ax = plt.subplots(figsize=(9, 5))

# 6. Renderiza as colunas verticais na tela:
#   - Eixo X: A lista '[meses_nome[m-1] for m in meses_ord]' converte os números em nomes.
#     O 'm-1' é necessário porque os meses vão de 1 a 12, mas os índices da lista começam em 0 (Jan é 0).
#   - Eixo Y: 'vals' entrega a quantidade de compras de cada mês.
#   - 'color="#4a90e2"': Aplica uma cor azul clássica uniforme para todas as barras.
#   - 'edgecolor="black"': Adiciona um contorno preto fino para destacar as colunas.
barras = ax.bar([meses_nome[m-1] for m in meses_ord], vals,
                color="#4a90e2", edgecolor="black")

# 7. Laço 'for' com 'zip()' para colocar as etiquetas de texto no topo de cada coluna.
for b, v in zip(barras, vals):
    # ax.text() carimba a quantidade exata de compras:
    #   - Posição X: Centraliza o texto calculando o meio da barra.
    #   - Posição Y: 'v + 0.5' faz o texto flutuar exatamente meia unidade acima da barra.
    #   - 'str(v)': Converte o número em texto simples para exibição.
    #   - 'ha="center"' e 'fontweight="bold"': Centraliza e coloca o número em negrito.
    ax.text(b.get_x() + b.get_width()/2, v + 0.5, str(v),
            ha="center", fontweight="bold")

# 8. Define o título do gráfico na parte superior.
ax.set_title("Compras por Mes (data da compra)")

# 9. Define o rótulo do eixo vertical Y, explicando que a altura indica o volume de transações.
ax.set_ylabel("Quantidade de compras")

# 10. Finaliza a máquina de estados e abre a tela exibindo a linha do tempo em formato de barras.
plt.show()

# 11. Linha comentada: Se ativada, exportaria esse gráfico cronológico como "g3_compras_mes.png".
#salvar(fig, "g3_compras_mes.png")



# Grafico 4 - Top 10 fornecedores por valor
valor_fornec = defaultdict(float)
for c in contas:
    valor_fornec[c["fornecedor"]] += c["valor"]
top = sorted(valor_fornec.items(), key=lambda x: x[1], reverse=True)[:10]
nomes = [t[0] for t in top][::-1]
vals = [t[1] for t in top][::-1]
fig, ax = plt.subplots(figsize=(9, 6))
ax.barh(nomes, vals, color="#7e57c2", edgecolor="black")
for i, v in enumerate(vals):
    ax.text(v, i, f"  R$ {v:,.0f}".replace(",", "."), va="center")
ax.set_title("Top 10 Fornecedores por Valor (R$)")
ax.set_xlabel("Valor (R$)")
ax.set_ylabel("Quantidade de compras")
plt.show()
#salvar(fig, "g4_top_fornecedores.png")

# Grafico 5 - Atrasos por categoria
atraso_cat = Counter(c["categoria"] for c in contas if c["status"] == "Em atraso")
cats = sorted(atraso_cat.keys(), key=lambda k: atraso_cat[k], reverse=True)
vals = [atraso_cat[c] for c in cats]
fig, ax = plt.subplots(figsize=(9, 5))
barras = ax.bar(cats, vals, color="#d9534f", edgecolor="black")
for b, v in zip(barras, vals):
    ax.text(b.get_x() + b.get_width()/2, v + 0.1, str(v),
            ha="center", fontweight="bold")
ax.set_title("Contas Em Atraso por Categoria")
ax.set_ylabel("Quantidade em atraso")
plt.xticks(rotation=20, ha="right")
plt.show()
#salvar(fig, "g5_atraso_categoria.png")

print(f"\nJSON: {json_path}")
print(f"Graficos em: {SAIDA_DIR}")