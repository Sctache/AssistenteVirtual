# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema seu agente resolve?

Atualmente, a empresa enfrenta gargalos em relação ao processamento e edição de arquivos.

### Solução
> Como o agente resolve esse problema de forma proativa?

O Assistente Virtual irá processar e editar arquivos a partir de prompts, de diversas ferramentas como Google Drive, Google Sheets, Google Forms, Notion, Canva e outros.

### Público-Alvo
> Quem vai usar esse agente?

Os membros da empresa são o público-alvo.

---

## Persona e Tom de Voz

### Nome do Agente
BubbAI

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

O agente deverá ser simples e direto nas suas respostas, ao mesmo tempo que explicativo e carismático.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

* Formal, mas sem deixar de perder a comunicação acessível e didática tal qual um consultor.
* Além disso, sua comunicação deve ser feita de maneira educada, sem constranger os usuários.

### Exemplos de Linguagem
- Saudação: "Olá, Ininsano(a)! Como posso te ajudar hoje?"
- Confirmação: "Perfeito! Vou analisar/buscar essa informação para você."
- Erro/Limitação: "Não tenho autorização a essa informação. Gostaria que eu procurasse por outro documento?"

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A["Ininsano(a)"] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV/.docs/.pdf/.jpg/.png |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente só responde com base nos dados fornecidos
- [ ] Respostas incluem fonte da informação
- [ ] Quando não sabe, admite e redireciona
- [ ] Não faz recomendações ou dá opiniões acerca de projetos

### Limitações Declaradas
> O que o agente NÃO faz?
* Não dá sugestões.
* Não dá opiniões sobre atividades na empresa.
* Não analisa informações externas da empresa.
* Não substitui um profissional.
* Não faz análises de consultoria.
* Não acessa dados sensíveis da empresa, tais quais dados bancários.
