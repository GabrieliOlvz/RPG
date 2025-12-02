import random
import math

class Paises:
    def __init__(self, nome, descricao, influencia, militar, estabilidade, economia):
        self.codigo = None
        self.nome = nome
        self.descricao = descricao
        self.influencia = influencia
        self.militar = militar
        self.estabilidade = estabilidade
        self.economia = economia
        self.hp = 100

    def esta_vivo(self):
        return self.hp > 0

    def receber_dano(self, dano, silenciar=False):
        dano_aplicado = min(self.hp, dano)
        self.hp -= dano_aplicado
        if not silenciar:
            print(f"{self.nome} sofreu {dano_aplicado} de dano, vida restante: {max(0, self.hp)}")
            if self.hp <= 0:
                print(f"{self.nome} foi eliminado da simulação.\n")
        return dano_aplicado

    def _score_para_prob(self, score_att, score_def, k=0.6, minimo=0.05, maximo=0.85):
        val = 1 / (1 + math.exp(-k * (score_att - score_def)))
        return max(minimo, min(maximo, val))

    def _rolar(self, prob):
        return random.random() < prob

    def _calc_scores(self, tipo, alvo, tensao, afinidade):
        if tipo == "atacar":
            att = self.militar * 1.0 + self.estabilidade * 0.8 + tensao / 20.0
            defe = alvo.estabilidade * 1.0 + alvo.militar * 0.5
            if afinidade == "aliado": att -= 3.0
            if afinidade == "inimigo": att += 2.0
            k = 0.6
        elif tipo == "negociar":
            att = self.influencia * 1.2 + self.economia * 1.0 - tensao / 30.0
            defe = alvo.influencia * 1.0 + alvo.economia * 0.8
            if afinidade == "aliado": att += 3.0
            if afinidade == "inimigo": att -= 3.0
            k = 0.7
        else:  # dialogo
            att = self.influencia * 1.0 + self.estabilidade * 0.9 - tensao / 40.0
            defe = alvo.influencia * 0.9 + alvo.estabilidade * 1.0
            if afinidade == "aliado": att += 2.0
            if afinidade == "inimigo": att -= 2.0
            k = 0.6

        att += random.uniform(-1.0, 1.0)
        defe += random.uniform(-0.5, 0.5)
        return att, defe, k

    def executar_acao(self, tipo, alvo, tensao=0, afinidade="neutro", silenciar=False):
        if not self.esta_vivo() or not alvo.esta_vivo():
            return (False, 0, 0.0) if silenciar else (False, 0)

        att, defe, k = self._calc_scores(tipo, alvo, tensao, afinidade)
        prob = self._score_para_prob(att, defe, k=k)

        if not silenciar:
            print(f"{self.nome} tenta {tipo} {alvo.nome}... Probabilidade de sucesso: {prob:.2f}")

        sucesso = self._rolar(prob)
        dano = 0

        if sucesso and tipo == "atacar":
            if silenciar:
                dano_aplicado = min(alvo.hp, 20)
                alvo.hp -= dano_aplicado
                dano = dano_aplicado
            else:
                dano = alvo.receber_dano(20)
                print("Ataque bem-sucedido!")
        elif sucesso:
            if not silenciar:
                print(f"{tipo.capitalize()} bem-sucedido!")
        else:
            if not silenciar:
                print(f"{tipo.capitalize()} falhou.")

        return (sucesso, dano, prob) if silenciar else (sucesso, dano)

class Brasil(Paises):
    def __init__(self):
        super().__init__(
            nome="Brasil",
            descricao="""Brasil (BRA) - PIB de aproximadamente US$ 2,3 trilhões. Com cerca de 203 milhões de habitantes, é a maior economia
da América do Sul, com destaque em agropecuária, mineração, energia e serviços. República presidencialista com
influência regional, grande biodiversidade e relevância em commodities.""",
            influencia=6, militar=5, estabilidade=7, economia=6
        )

class EstadosUnidos(Paises):
    def __init__(self):
        super().__init__(
            nome="Estados Unidos",
            descricao="""Estados Unidos (USA) - Maior economia do mundo, com PIB de US$ 30,34 trilhões. Localizado na América do Norte,
tem 347 milhões de habitantes e forte presença em tecnologia, defesa e finanças. É uma república
presidencialista com influência global em política, cultura e inovação.""",
            influencia=9, militar=9, estabilidade=8, economia=10
        )

class China(Paises):
    def __init__(self):
        super().__init__(
            nome="China",
            descricao="""China (CHN) - Segunda maior economia, com PIB de US$ 19,53 trilhões. Com mais de 1,4 bilhão de habitantes,
lidera em manufatura, exportações e infraestrutura. Governada pelo Partido Comunista, investe em tecnologia 
e expansão internacional.""",
            influencia=8, militar=9, estabilidade=7, economia=9
        )

class Alemanha(Paises):
    def __init__(self):
        super().__init__(
            nome="Alemanha",
            descricao="""Alemanha (DEU) - Principal economia da Europa, com PIB de US$ 5,2 trilhões. Tem 84 milhões de habitantes e 
é referência em engenharia, automóveis e exportações. É uma república parlamentarista com forte presença
na União Europeia.""",
            influencia=8, militar=6, estabilidade=9, economia=8
        )

class India(Paises):
    def __init__(self):
        super().__init__(
            nome="Índia",
            descricao="""Índia (IND) - Quarta maior economia, com PIB de US$ 4,2 trilhões. Com mais de 1,4 bilhão de habitantes, 
cresce em tecnologia, serviços e indústria. É uma república federal com desafios sociais e grande potencial 
de mercado.""",
            influencia=7, militar=7, estabilidade=6, economia=7
        )

class Japao(Paises):
    def __init__(self):
        super().__init__(
            nome="Japão",
            descricao="""Japão (JPN) - Economia avançada com PIB de US$ 4,1 trilhões. Tem 125 milhões de habitantes e é líder em 
robótica, automóveis e inovação. Monarquia constitucional com alto padrão de vida e envelhecimento populacional.""",
            influencia=8, militar=6, estabilidade=9, economia=8
        )

class ReinoUnido(Paises):
    def __init__(self):
        super().__init__(
            nome="Reino Unido",
            descricao="""Reino Unido (GBR) - PIB de US$ 3,6 trilhões. Com 68 milhões de habitantes, destaca-se em finanças, serviços
e cultura. Monarquia parlamentar com influência histórica e desafios pós-Brexit.""",
            influencia=7, militar=6, estabilidade=8, economia=7
        )

class Franca(Paises):
    def __init__(self):
        super().__init__(
            nome="França",
            descricao="""França (FRA) - PIB de US$ 3,2 trilhões. Tem 67 milhões de habitantes e é forte em turismo, energia e
agricultura. República semipresidencialista com papel ativo na política europeia e global.""",
            influencia=7, militar=6, estabilidade=8, economia=7
        )

class Italia(Paises):
    def __init__(self):
        super().__init__(
            nome="Itália",
            descricao="""Itália (ITA) - PIB de US$ 2,5 trilhões. Com 59 milhões de habitantes, é referência em moda, design e turismo. 
República parlamentarista com economia regionalizada e rica herança cultural.""",
            influencia=6, militar=5, estabilidade=7, economia=6
        )

class Canada(Paises):
    def __init__(self):
        super().__init__(
            nome="Canadá",
            descricao="""Canadá (CAN) - PIB de US$ 2,3 trilhões. Com 40 milhões de habitantes, tem economia baseada em recursos naturais,
tecnologia e serviços. Monarquia constitucional com alto índice de qualidade de vida.""",
            influencia=6, militar=5, estabilidade=9, economia=7
        )

class CoreiaSul(Paises):
    def __init__(self):
        super().__init__(
            nome="Coreia do Sul",
            descricao="""Coreia do Sul (KOR) - PIB de US$ 2,1 trilhões. Com 52 milhões de habitantes, é líder em tecnologia, eletrônicos 
e cultura pop. República presidencialista com alto nível de inovação e educação.""",
            influencia=7, militar=6, estabilidade=8, economia=7
        )

class Russia(Paises):
    def __init__(self):
        super().__init__(
            nome="Rússia",
            descricao="""Rússia (RUS) - PIB de US$ 1,9 trilhões. Com 144 milhões de habitantes, tem economia baseada em energia e metais.
Federação presidencialista com forte presença militar e influência geopolítica.""",
            influencia=6, militar=9, estabilidade=5, economia=6
        )

class Mexico(Paises):
    def __init__(self):
        super().__init__(
            nome="México",
            descricao="""México (MEX) - PIB de US$ 1,8 trilhões. Com 130 milhões de habitantes, é forte em manufatura, petróleo e turismo. 
República federal com desafios sociais e integração econômica com os EUA.""",
            influencia=5, militar=5, estabilidade=6, economia=6
        )

class Espanha(Paises):
    def __init__(self):
        super().__init__(
            nome="Espanha",
            descricao="""Espanha (ESP) - PIB de US$ 1,7 trilhões. Com 48 milhões de habitantes, destaca-se em turismo, agricultura e 
energia. Monarquia parlamentar com economia diversificada e rica cultura.""",
            influencia=6, militar=5, estabilidade=7, economia=6
        )

class Australia(Paises):
    def __init__(self):
        super().__init__(
            nome="Austrália",
            descricao="""Austrália (AUS) - PIB de US$ 1,6 trilhões. Com 27 milhões de habitantes, tem economia voltada para mineração,
educação e serviços. Monarquia constitucional com alto padrão de vida e estabilidade.""",
            influencia=6, militar=5, estabilidade=8, economia=7
        )

listpaises = ["USA","CHN","DEU","IND","JPN","GBR","FRA","ITA","CAN","BRA","KOR","RUS","MEX","ESP","AUS"]
codigo_para_classe = {
    "BRA": Brasil, "USA": EstadosUnidos, "CHN": China, "DEU": Alemanha, "IND": India,
    "JPN": Japao, "GBR": ReinoUnido, "FRA": Franca, "ITA": Italia, "CAN": Canada,
    "KOR": CoreiaSul, "RUS": Russia, "MEX": Mexico, "ESP": Espanha, "AUS": Australia
}

lista_paises = []
codigo_obj = {}
for codigo in listpaises:
    cls = codigo_para_classe.get(codigo)
    if cls:
        obj = cls()
        obj.codigo = codigo
        lista_paises.append(obj)
        codigo_obj[codigo] = obj

tensao = {p.codigo: {q.codigo: 20 for q in lista_paises if q.codigo != p.codigo} for p in lista_paises}
afinidade = {p.codigo: {q.codigo: "neutro" for q in lista_paises if q.codigo != p.codigo} for p in lista_paises}
afinidade["USA"]["CHN"] = "inimigo"
afinidade["CHN"]["USA"] = "inimigo"

populacao_estimada = {
    "USA":347_000_000,"CHN":1_400_000_000,"DEU":84_000_000,"IND":1_400_000_000,"JPN":125_000_000,
    "GBR":68_000_000,"FRA":67_000_000,"ITA":59_000_000,"CAN":40_000_000,"BRA":203_000_000,
    "KOR":52_000_000,"RUS":144_000_000,"MEX":130_000_000,"ESP":48_000_000,"AUS":27_000_000
}
pib_relativo = {
    "USA":30.34,"CHN":19.53,"DEU":5.20,"IND":4.20,"JPN":4.10,"GBR":3.60,"FRA":3.20,"ITA":2.50,
    "CAN":2.30,"BRA":2.30,"KOR":2.10,"RUS":1.90,"MEX":1.80,"ESP":1.70,"AUS":1.60
}

def efeitos_informativos(ator, alvo, acao, dano, sucesso):
    pop = populacao_estimada.get(alvo.codigo, 50_000_000)
    pib = pib_relativo.get(alvo.codigo, 1.0)
    if acao == "atacar":
        if sucesso:
            mortos = int(max(1, dano * (pib / 2.0)))
            feridos = int(mortos * 1.5)
            desloc = int(mortos * 5)
            perda_pct = min(30, dano * 2 + pib)
            desc = (f"Ataque bem sucedido contra {alvo.nome}.\nEstimativa: ~{mortos} mortos, ~{feridos} feridos, ~{desloc} deslocados.\n"
                    f"Impacto econômico aproximado: ~{perda_pct:.1f}% do indicador econômico relativo ({pib}).")
        else:
            desc = (f"Ataque falhou contra {alvo.nome}. Danos materiais limitados; aumento de tensão e perda de reputação.")
    elif acao == "negociar":
        desc = (f"Negociação {'bem-sucedida' if sucesso else 'falhou'} entre {ator.nome} e {alvo.nome}.")
    else:
        desc = (f"Diálogo {'bem-sucedido' if sucesso else 'falhou'} entre {ator.nome} e {alvo.nome}.")
    print("\n--- Informações sobre impacto ---")
    print(desc)
    print("--- Fim das informações ---\n")

def escolher_pais(prompt):
    while True:
        print(prompt)
        print("Códigos disponíveis:", " ".join(listpaises))
        escolha = input("Digite o código do país: ").strip().upper()
        if escolha in codigo_obj:
            return codigo_obj[escolha]
        print("Código inválido. Tente novamente.\n")

def aplicar_efeitos_colaterais(ator, alvo, acao, sucesso):
    if sucesso:
        if acao == "atacar":
            tensao[ator.codigo][alvo.codigo] = min(100, tensao[ator.codigo][alvo.codigo] + 10)
        elif acao == "negociar":
            tensao[ator.codigo][alvo.codigo] = max(0, tensao[ator.codigo][alvo.codigo] - 5)
            afinidade[ator.codigo][alvo.codigo] = "aliado"
        else:
            tensao[ator.codigo][alvo.codigo] = max(0, tensao[ator.codigo][alvo.codigo] - 5)
    else:
        tensao[ator.codigo][alvo.codigo] = min(100, tensao[ator.codigo][alvo.codigo] + 5)
        if acao == "atacar":
            afinidade[ator.codigo][alvo.codigo] = "inimigo"

def escolher_alvo_aleatorio(ator):
    poss = [p for p in lista_paises if p.codigo != ator.codigo and p.esta_vivo()]
    return random.choice(poss) if poss else None

jogador = escolher_pais("Escolha seu país:")
print(f"\nVocê escolheu: {jogador.nome}\n")
print("Descrição do país escolhido:\n" + jogador.descricao + "\n")

turno = 1
max_turnos = 50
while turno <= max_turnos:
    print(f"--- TURNO {turno} ---")
    vivos = [p for p in lista_paises if p.esta_vivo()]
    if not jogador.esta_vivo():
        print("Você foi eliminado. Fim de jogo."); break
    if len(vivos) <= 1:
        print("Simulação terminou: apenas um país restante."); break

    mensagens_jogador = []
    impacto_jogador = None

    print(f"\nSeu turno ({jogador.nome}) - HP: {jogador.hp}")
    print("Ações: 1) atacar 2) negociar 3) dialogar 4) passar")
    escolha = input("Escolha (1-4): ").strip()
    if escolha in ("1","2","3"):
        alvos = [p for p in lista_paises if p.codigo != jogador.codigo and p.esta_vivo()]
        if not alvos:
            print("Nenhum alvo disponível.")
        else:
            for p in alvos:
                print(f"{p.codigo} - {p.nome} (HP:{p.hp} Tensão:{tensao[jogador.codigo].get(p.codigo,0)} Afinidade:{afinidade[jogador.codigo].get(p.codigo,'neutro')})")
            cod = input("Digite o código do alvo: ").strip().upper()
            alvo = codigo_obj.get(cod)
            if alvo and alvo.esta_vivo() and alvo.codigo != jogador.codigo:
                acao = {"1":"atacar","2":"negociar","3":"dialogar"}[escolha]
                tens = tensao[jogador.codigo].get(alvo.codigo, 0)
                afin = afinidade[jogador.codigo].get(alvo.codigo, "neutro")

                sucesso, dano, prob = jogador.executar_acao(acao, alvo, tensao=tens, afinidade=afin, silenciar=True)

                mensagens_jogador.append(f"{jogador.nome} tenta {acao} {alvo.nome}... Probabilidade de sucesso: {prob:.2f}")
                if sucesso and acao == "atacar":
                    mensagens_jogador.append(f"{alvo.nome} sofreu {dano} de dano, vida restante: {max(0, alvo.hp)}")
                    mensagens_jogador.append("Ataque bem-sucedido!")
                elif sucesso:
                    mensagens_jogador.append(f"{acao.capitalize()} bem-sucedido!")
                else:
                    mensagens_jogador.append(f"{acao.capitalize()} falhou.")

                impacto_jogador = (jogador, alvo, acao, dano, sucesso)
                aplicar_efeitos_colaterais(jogador, alvo, acao, sucesso)
            else:
                print("Alvo inválido.")
    else:
        print("Passou o turno.")

    for pais in lista_paises:
        if pais.codigo == jogador.codigo or not pais.esta_vivo(): continue
        alvo = escolher_alvo_aleatorio(pais)
        if not alvo: continue
        tens_med = tensao[pais.codigo].get(alvo.codigo, 20)
        afin = afinidade[pais.codigo].get(alvo.codigo, "neutro")
        prob_atacar = min(0.6, 0.2 + tens_med/100.0)
        prob_neg = 0.2 if afin == "aliado" else 0.1
        r = random.random()
        if r < prob_atacar:
            sucesso, dano = pais.executar_acao("atacar", alvo, tensao=tens_med, afinidade=afin)
            efeitos_informativos(pais, alvo, "atacar", dano, sucesso)
            aplicar_efeitos_colaterais(pais, alvo, "atacar", sucesso)
        elif r < prob_atacar + prob_neg:
            sucesso, _ = pais.executar_acao("negociar", alvo, tensao=tens_med, afinidade=afin)
            efeitos_informativos(pais, alvo, "negociar", 0, sucesso)
            aplicar_efeitos_colaterais(pais, alvo, "negociar", sucesso)
        else:
            sucesso, _ = pais.executar_acao("dialogar", alvo, tensao=tens_med, afinidade=afin)
            efeitos_informativos(pais, alvo, "dialogar", 0, sucesso)
            aplicar_efeitos_colaterais(pais, alvo, "dialogar", sucesso)

    if mensagens_jogador:
        for linha in mensagens_jogador:
            print(linha)
    if impacto_jogador is not None:
        ator, alvo, acao, dano, sucesso = impacto_jogador
        efeitos_informativos(ator, alvo, acao, dano, sucesso)

    print("\nEstado ao fim do turno:")
    for p in lista_paises:
        print(f"{p.codigo} - {p.nome}: HP={max(0,p.hp)} | Status={'vivo' if p.esta_vivo() else 'eliminado'}")
    print()
    turno += 1

print("Simulação encerrada.")