# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Para que serve? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |
| `Teste.csv`| CSV | Testar uso de texto com csv

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Adicionei mais um dado para trabalhar tentar inserir, no banco de dados, um arquivo de texto.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt.
```python
import pandas as pd
import json

#CSV's
historicos = pd.read_csv("data/historico_atendimento.csv")
transacoes = pd.read_csv("data/transacoes.csv")
teste = pd.read_csv("data/Teste.csv")

#JSON's
with open ("data/perfil_investidor.json", "r", "encoding = "utf-8") as f:
  perfil = json.load(f)

with open ("data/produtos_financeiros.json", "r", encoding = "utf-8") as f:
  produtos = json.load(f)

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```text
DADOS DO CLIENTE:
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSAÇÕES DO CLIENTE:
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

HISTÓRICO DE ATENDIMENTO:
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

PRODUTOS DISPONÍVEIS:
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

ROTEIRO DE POSTAGEM:
Do chocolate ao amor: a estratégia da Nestlé no Dia dos Namorados
Como a Nestlé transformou o Dia dos Namorados em tradição
Como a Nestlé criou uma tradição
Tradições nascem de boas estratégias
Marketing transforma produtos em cultura
Nestlé e a arte de vender emoção






Slide 1
Título


Slide 2
HISTÓRIA
"Criado em 1948 no Brasil para aquecer as vendas de junho, o Dia dos Namorados nasceu do comércio!"
"Dessa forma, a Nestlé enxergou uma oportunidade."
Foi pioneira em associar chocolates à data.


Slide 3
JOGADA DA NESTLÉ
"Nos anos 1960, a Nestlé lançou embalagens de chocolates especiais e campanhas temáticas."
O chocolate virou presente obrigatório.
"Essa inovação não só aumentou vendas, mas criou uma nova tradição cultural."


Slide 4
OPORTUNIDADE
A Nestlé usou um mês fraco para o seu nicho para criar uma nova tradição.
Empreendedores podem e devem fazer o mesmo em períodos de baixa demanda.


Slide 5
PERSONALIZAÇÃO E EXPERIÊNCIA
Caixas em formato de coração e mensagens românticas agregaram valor.
Produtos personalizados criam conexão emocional.
E conexão emocional gera boas experiências.
que gera valor!


Slide 6
MARKETING INTELIGENTE
"A Nestlé não vendeu apenas chocolate, vendeu amor."
"explorando a força da televisão recém-popularizada, embalagens diferenciadas e discursos persuasivos voltados às donas de casa."
Empreendedores devem criar produtos que despertem sentimentos.




Slide 7
A Nestlé transformou chocolate em oportunidade.
"Na Iniciativa, analisamos as suas oportunidades para que você 🫵 possa transformá-las em solução!"






Legenda:
✨ Nestlé e a arte de vender emoção no Dia dos Namorados ✨


"Nos anos 1960, a Nestlé não vendeu apenas chocolate. Ela vendeu amor, tradição e conexão."


"Assim como ela, você pode criar oportunidades em períodos de baixa demanda. Transforme produtos comuns em experiências memoráveis."


"Se a Nestlé conseguiu transformar chocolate em símbolo de romance, imagine o que você pode fazer com o seu negócio!"

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
