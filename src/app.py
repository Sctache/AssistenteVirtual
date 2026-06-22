import pandas as pd
import json
import streamlit as st

# CARREGANDO DADOS
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

#MONTANDO O CONTEXTO
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R${perfil['patrimonio_total']} | RESERVA: {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES: 
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

#SYSTEM PROMPT
SYSTEM_PROMPT = """
Você é o BubbAI, um assistente de consultoria carismático e profissional.

Objetivo: Processar arquivos de uma empresa de maneira rápida e eficaz.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Mostre os dados utilizados na sua resposta
5. Não dê opiniões
"""

#OLLAMA
def perguntar(msg):
    prompt = f'''
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}
'''

r = requests.post(OLLAMA_URL, json={'model': MODELO, 'prompt': prompt, 'stream': False})

#INTERFACE STREAMLIT
st.title("BubbAI, seu consultor!")

if pergunta := st.chat_input('Qual é a sua dúvida?'):
    st.chat_message('user').write(pergunta)
    with st.spinner('...'):
        st.chat_message('assistant').write(perguntar(pergunta)) #Perguntar é da OLLAMA 
