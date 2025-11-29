# Defina 5 a 6 regras no formato SE [condição] ENTÃO [conclusão/ação].
## Exemplo: Regra 1: SE (tanque vazio) ENTÃO (carro não liga). Regra 2: SE (marcador no zero) ENTÃO (tanque vazio).

# Base de Conhecimento (Knowledge Base)
# Formato: { "PROBLEMA_MACRO": ["SINTOMA_1", "SINTOMA_2"], "SINTOMA_1": ["CAUSA_RAIZ"] }

base_conhecimento = {
    # Nível Superior: Problemas Macro
    "carro não liga": [
        "luzes do painel apagadas",
        "apenas som de clique ao girar chave",
        "motor gira mas não pega"
    ],
    "ar condicionado não gela": [
        "vento sai quente",
        "fluxo de vento muito fraco"
    ],
    "freios com mau funcionamento": [
        "chiado metálico ao frear",
        "pedal trepidando ao frear"
    ],

    # Nível Intermediário: Sintomas -> Causas Raízes
    "luzes do painel apagadas": ["bateria descarregada"],
    "apenas som de clique ao girar chave": ["motor de arranque com defeito"],
    "motor gira mas não pega": ["falta de combustível ou ignição"],

    "vento sai quente": ["falta de gás refrigerante"],
    "fluxo de vento muito fraco": ["filtro de cabine entupido"],

    "chiado metálico ao frear": ["pastilhas de freio gastas"],
    "pedal trepidando ao frear": ["discos de freio empenados"]
    
    # Nota: "bateria descarregada" não é chave, pois é uma "folha" (causa raiz).
}

# Defina os Fatos Iniciais (ex: "Carro não liga").

## carro não liga
## ar condicionado não gela
## freios com mau funcionamento

# Simule o Encadeamento Regressivo (Backward Chaining). Comece com a meta "Carro não liga" e vá voltando nas regras até provar a causa.

# No relatório
## Base de Conhecimento: Liste todas as suas regras escritas.

## Simulação: Escreva o passo a passo do raciocínio. "O sistema verificou a Regra X, mas precisava saber Y...".

## Conclusão: O diagnóstico final baseado nos fatos.
