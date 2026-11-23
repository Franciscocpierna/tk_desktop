# Em Python, usar self faz parte do padrão da linguagem para acessar e alterar atributos de cada instância. E quando o assunto é get e set, o Python tem duas formas muito comuns:

# Métodos explícitos (get_... e set_...) — bem direto, lembra o estilo clássico de outras linguagens.

# @property e @<atributo>.setter — o jeito mais idiomático em Python, pois permite validar/calcular valores no set/get sem precisar mudar a chamada para obj.get_x() ou obj.set_x(10).

# Abaixo tem um exemplo completo com @property + setter e também como fica com get_... / set_..., reutilizando instâncias dentro de um sistema.

# Exemplo prático em Python (usando self e @property / setter)
# Imagine uma classe de parâmetros de orçamento/cálculo que você instancia várias vezes no sistema (para cenários ou clientes diferentes):








class ParametrosCalculo:
    def __init__(self, taxa_imposto: float = 0.10, desconto_percentual: float = 0.0):
        # Usa os setters no __init__ para já validar os valores iniciais
        self.taxa_imposto = taxa_imposto
        self.desconto_percentual = desconto_percentual

    @property
    def taxa_imposto(self) -> float:
        return self._taxa_imposto

    @taxa_imposto.setter
    def taxa_imposto(self, valor: float) -> None:
        if not (0.0 <= valor <= 1.0):
            raise ValueError("A taxa de imposto deve estar entre 0.0 (0%) e 1.0 (100%).")
        self._taxa_imposto = valor

    @property
    def desconto_percentual(self) -> float:
        return self._desconto_percentual

    @desconto_percentual.setter
    def desconto_percentual(self, valor: float) -> None:
        if not (0.0 <= valor <= 100.0):
            raise ValueError("O desconto deve estar entre 0 e 100.")
        self._desconto_percentual = valor

    def calcular_valor_final(self, valor_base: float) -> float:
        valor_com_desconto = valor_base * (1 - self._desconto_percentual / 100.0)
        return valor_com_desconto * (1 + self._taxa_imposto)


        # Instância 1: padrão
padrao = ParametrosCalculo()

# Instância 2: reutilizando a classe para um cenário promocional
promocao = ParametrosCalculo(taxa_imposto=0.12)
promocao.desconto_percentual = 15.0  # chama o setter e valida!

# Lendo os valores (chama o @property / getter)
print(padrao.taxa_imposto)         # 0.1
print(promocao.desconto_percentual) # 15.0

# Usando cada instância independentemente
print("Padrão:", padrao.calcular_valor_final(1000))
print("Promoção:", promocao.calcular_valor_final(1000))


# Detalhe importante sobre self e nomes internos: perceba que no setter usamos self._taxa_imposto (com underline). Se usássemos self.taxa_imposto = valor dentro do próprio setter, ele chamaria a si mesmo em loop infinito (RecursionError).

# Se você prefere métodos get_... e set_... explícitos
# Caso seu padrão de código ou equipe prefira métodos nomeados como get_... e set_..., também funciona perfeitamente com self:



class VariaveisSistema:
    def __init__(self, ambiente: str = "dev"):
        self._ambiente = ambiente

    def get_ambiente(self) -> str:
        return self._ambiente

    def set_ambiente(self, novo_ambiente: str) -> None:
        permitidos = {"dev", "homolog", "prod"}
        if novo_ambiente not in permitidos:
            raise ValueError(f"Ambiente inválido: {novo_ambiente}")
        self._ambiente = novo_ambiente



#         Dica extra para reutilizar sem dor de cabeça
# Evite mutar a mesma instância em vários lugares ao mesmo tempo: se uma função recebe params: ParametrosCalculo e altera params.desconto_percentual, isso afeta quem chamou aquela função.

# Se quiser reaproveitar uma base sem estragar a original, crie um método clonar() na classe usando copy.copy(self) (ou copy.deepcopy(self) se houver listas/dicionários dentro).

# Quais variáveis exatamente você quer colocar nessa classe? Se quiser me passar os nomes e regras delas, eu monto a estrutura já com os campos certos para o seu sistema.



# Aqui está um exemplo completo em Python com várias variáveis de tipos diferentes (texto, número inteiro, decimal, booleano, lista e dicionário),
# usando self, @property / @<campo>.setter (para leitura e escrita com validação) 
# e métodos auxiliares para reutilizar as instâncias com segurança no seu sistema.




import copy


class VariaveisOperacao:
    """Classe que reúne várias variáveis de um contexto/operação para reutilização
    em múltiplas instâncias independentes dentro do sistema.
    """

    def __init__(
        self,
        nome_fluxo: str = "fluxo_padrao",
        tentativas_maximas: int = 3,
        fator_multiplicador: float = 1.0,
        ativo: bool = True,
        tags: list[str] | None = None,
        metadados: dict[str, str] | None = None,
    ) -> None:
        # Chamamos os setters no __init__ para garantir que até os valores iniciais
        # passem pelas regras de validação da classe.
        self.nome_fluxo = nome_fluxo
        self.tentativas_maximas = tentativas_maximas
        self.fator_multiplicador = fator_multiplicador
        self.ativo = ativo

        # Evitamos mutabilidade compartilhada criando novas coleções quando None
        # ou copiando listas/dicionários recebidos de fora.
        self.tags = list(tags) if tags is not None else []
        self.metadados = dict(metadados) if metadados is not None else {}

    # --- 1. Variável de texto (str) ---
    @property
    def nome_fluxo(self) -> str:
        """Retorna o nome normalizado do fluxo (getter)."""
        return self._nome_fluxo

    @nome_fluxo.setter
    def nome_fluxo(self, valor: str) -> None:
        """Valida e salva o nome do fluxo sem espaços extras (setter)."""
        limpo = valor.strip()
        if not limpo:
            raise ValueError("nome_fluxo não pode ser vazio.")
        self._nome_fluxo = limpo

    # --- 2. Variável inteira (int) ---
    @property
    def tentativas_maximas(self) -> int:
        return self._tentativas_maximas

    @tentativas_maximas.setter
    def tentativas_maximas(self, valor: int) -> None:
        """Garante que o número de tentativas seja pelo menos 1."""
        if valor < 1:
            raise ValueError("tentativas_maximas deve ser maior ou igual a 1.")
        self._tentativas_maximas = int(valor)

    # --- 3. Variável decimal (float) ---
    @property
    def fator_multiplicador(self) -> float:
        return self._fator_multiplicador

    @fator_multiplicador.setter
    def fator_multiplicador(self, valor: float) -> None:
        """Impede fator negativo ou zero."""
        if valor <= 0:
            raise ValueError("fator_multiplicador deve ser maior que zero.")
        self._fator_multiplicador = float(valor)

    # --- 4. Variável booleana (bool) ---
    @property
    def ativo(self) -> bool:
        return self._ativo

    @ativo.setter
    def ativo(self, valor: bool) -> None:
        """Converte/valida explicitamente o estado booleano."""
        self._ativo = bool(valor)

    # --- 5. Variável de lista (list[str]) ---
    @property
    def tags(self) -> list[str]:
        return self._tags

    @tags.setter
    def tags(self, valores: list[str]) -> None:
        """Salva uma nova lista de tags removendo itens vazios."""
        self._tags = [item.strip() for item in valores if item and item.strip()]

    # --- 6. Variável de dicionário (dict[str, str]) ---
    @property
    def metadados(self) -> dict[str, str]:
        return self._metadados

    @metadados.setter
    def metadados(self, dados: dict[str, str]) -> None:
        """Salva uma cópia do dicionário de metadados."""
        self._metadados = dict(dados)

    # --- Métodos úteis para reutilizar instâncias ---
    def adicionar_tag(self, tag: str) -> None:
        """Adiciona uma tag à instância atual sem duplicar."""
        limpa = tag.strip()
        if limpa and limpa not in self._tags:
            self._tags.append(limpa)

    def definir_metadado(self, chave: str, valor: str) -> None:
        """Define ou atualiza uma chave específica dentro de metadados."""
        self._metadados[chave] = valor

    def clonar(self) -> "VariaveisOperacao":
        """Cria uma cópia independente desta instância (evita alterar a original)."""
        return copy.deepcopy(self)

    def resumo(self) -> str:
        """Retorna um resumo legível das variáveis atuais da instância."""
        return (
            f"Fluxo={self._nome_fluxo} | Ativo={self._ativo} | "
            f"Tentativas={self._tentativas_maximas} | Fator={self._fator_multiplicador} | "
            f"Tags={self._tags} | Metadados={self._metadados}"
        )


#Como utilizar e reutilizar as instâncias no sistema

# 1. Criando uma instância com valores padrão
base = VariaveisOperacao()
base.adicionar_tag("core")
base.definir_metadado("origem", "sistema_principal")

# 2. Reutilizando a instância 'base' via clone para criar uma variação segura
#    (alterar 'variacao_a' NÃO altera 'base')
variacao_a = base.clonar()
variacao_a.nome_fluxo = "processamento_lote"
variacao_a.tentativas_maximas = 5
variacao_a.fator_multiplicador = 1.25
variacao_a.adicionar_tag("lote")
variacao_a.definir_metadado("prioridade", "alta")

# 3. Criando outra instância independente para outro cenário
variacao_b = VariaveisOperacao(
    nome_fluxo="contingencia",
    tentativas_maximas=2,
    fator_multiplicador=0.8,
    ativo=False,
    tags=["fallback"],
    metadados={"canal": "fila_secundaria"},
)

# 4. Lendo valores com @property (get) e alterando com setter (set)
print(base.resumo())
print(variacao_a.resumo())
print(variacao_b.resumo())

# Por que essa estrutura funciona bem para reutilização?
# Isolamento entre instâncias: cada objeto guarda seus próprios dados em self._..., então base, variacao_a e variacao_b não se atropelam.

# Segurança em listas e dicionários: usar list(...), dict(...) e copy.deepcopy(self) evita que duas instâncias apontem para a mesma lista/dicionário na memória.

# Validação centralizada: sempre que você lê (instancia.fator_multiplicador) ou altera (instancia.fator_multiplicador = 1.5), o @property e o @setter rodam automaticamente com self.

# Se quiser adaptar os nomes das variáveis para o domínio exato do seu sistema (ex.: pedidos, sensores, usuários, relatórios), me diga quais campos você precisa e eu já ajusto a classe para você.




# A linha @nome_fluxo.setter é um decorador (decorator) em Python que define o método set (de escrita/validação) da propriedade nome_fluxo.

# Ela sempre depende de existir antes uma propriedade com o mesmo nome marcada com @property.

# Como essas partes se conectam
# Quando você escreve:




class Exemplo:
    def __init__(self, nome_fluxo: str):
        self.nome_fluxo = nome_fluxo  # 1. Chama o setter automaticamente

    @property
    def nome_fluxo(self) -> str:      # 2. Define o GET (leitura)
        return self._nome_fluxo

    @nome_fluxo.setter                # 3. Liga o SET (escrita) ao atributo "nome_fluxo"
    def nome_fluxo(self, valor: str) -> None:
        limpo = valor.strip()
        if not limpo:
            raise ValueError("nome_fluxo não pode ser vazio.")
        self._nome_fluxo = limpo



# O que acontece por baixo dos panos quando você usa
# Ao ler (obj.nome_fluxo):
# O Python executa a função decorada com @property e devolve self._nome_fluxo.

# Ao atribuir (obj.nome_fluxo = "  novo_fluxo  "):
# Em vez de apenas sobrescrever o atributo cru, o Python intercepta a atribuição e executa a função decorada com @nome_fluxo.setter, passando self e o valor ("  novo_fluxo  ").

# Dentro do setter:

# A variável valor recebe o que foi passado à direita do =.

# A validação roda (se estiver vazio, lança ValueError e bloqueia a alteração).

# O resultado final é salvo em self._nome_fluxo (com underline _ para diferenciar do nome da propriedade e evitar recursão infinita).

# Por que o nome tem um ponto (@nome_fluxo.setter)?
# Porque o decorador @property cria um objeto de propriedade chamado nome_fluxo na classe, e esse objeto possui um método .setter(...) que registra qual função vai tratar as atribuições (=) feitas em instancia.nome_fluxo.

# Em outras palavras:

# @property = o GET de nome_fluxo

# @nome_fluxo.setter = o SET de nome_fluxo        