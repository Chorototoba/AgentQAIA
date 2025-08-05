import streamlit as st
import openai
import os
import base64
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Configuração de senha ---
SENHA_CORRETA = "QA123"

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.title("🔒 Acesso Restrito")
    senha_digitada = st.text_input("Digite a senha para acessar:", type="password")
    if st.button("Entrar"):
        if senha_digitada == SENHA_CORRETA:
            st.session_state.autenticado = True
            st.success("✅ Acesso liberado!")
            st.rerun()
        else:
            st.error("❌ Senha incorreta.")
    st.stop()

# --- Prompt principal ---
PROMPT_TEMPLATE = """
Você é um Engenheiro de QA Sênior, especialista em automação de testes e escrita de cenários BDD no formato Gherkin.
Sua tarefa é gerar cenários de teste extremamente completos, cobrindo todos os casos possíveis (positivos, negativos, alternativos, de exceção e limites) para a História de Usuário fornecida.

Instruções obrigatórias:
1. Use sempre o formato Gherkin com as palavras-chave Funcionalidade, Contexto, Cenário, Cenário de Exemplo, Esquema do Cenário, Dado, Quando, Então, E — tudo em português.
2. Considere:
   - Fluxo feliz (caminho principal)
   - Casos negativos (erros, dados inválidos, campos obrigatórios não preenchidos)
   - Casos de borda (limites numéricos, tamanhos máximos e mínimos de campos, formatos inválidos)
   - Validações de segurança (injeção de código, XSS, acessos não autorizados)
   - Restrições de negócio específicas
   - Comportamentos em navegadores diferentes (se aplicável)
   - Cenários de compatibilidade e performance quando necessário
   - Condições iniciais de tela, incluindo casos em que filtros padrão (como datePicker) não são alterados
   - Interações combinadas entre filtros (ex.: um filtro não é alterado, outro sim)
3. Para cada cenário:
   - O título deve ser claro e autoexplicativo
   - A descrição deve cobrir o objetivo do teste
   - As etapas devem estar ordenadas e ser reutilizáveis
4. Agrupe os cenários por tipo (Positivos, Negativos, Limite, Segurança, Regras de Negócio)
5. Inclua Esquema do Cenário com Exemplos para valores múltiplos, quando aplicável
6. Sempre validar mensagens de erro e confirmações esperadas
7. Aplique as seguintes técnicas de teste na criação dos cenários:
   - **Particionamento de Equivalência**
   - **Análise de Valor Limite**
   - **Tabela de Decisão**
   - **Planejamento e Execução**
   - Cobertura de diferentes fases do desenvolvimento

Formato de saída:
Funcionalidade: [Nome da funcionalidade]
  Contexto:
    Dado que [pré-condição]

  # Cenários positivos
  Cenário: [Descrição]
    Dado que ...
    Quando ...
    Então ...

  # Cenários negativos
  Cenário: [Descrição]
    Dado que ...
    Quando ...
    Então ...

  # Esquema do Cenário com exemplos
  Esquema do Cenário: [Descrição]
    Dado que ...
    Quando ...
    Então ...

    Exemplos:
      | campo1 | campo2 |
      | valor1 | valor2 |

📌 Dúvidas sobre a Atividade:
Liste todas as dúvidas ou pontos que precisam de esclarecimento sobre a história de usuário, regras de negócio ou critérios de aceitação. 
Se não houver dúvidas, escreva "Nenhuma dúvida identificada".

História de Usuário:
{historia_usuario}

Regras de Negócio:
{regras_negocio}

Critérios de Aceitação:
{criterios_aceitacao}
"""

# Função para gerar cenários
def gerar_cenarios(historia_usuario, regras_negocio, criterios_aceitacao, arquivos):
    prompt = PROMPT_TEMPLATE.format(
        historia_usuario=historia_usuario,
        regras_negocio=regras_negocio or "Não informado",
        criterios_aceitacao=criterios_aceitacao or "Não informado"
    )

    mensagens = [
        {"role": "system", "content": "Você é um Engenheiro de QA Sênior, especialista em testes BDD"},
        {"role": "user", "content": [{"type": "text", "text": prompt}]}
    ]

    # Adiciona arquivos (imagens/PDF) convertidos em base64
    for arquivo in arquivos:
        base64_data = base64.b64encode(arquivo.read()).decode("utf-8")
        mensagens[1]["content"].append(
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_data}"}}
        )

    resposta = openai.chat.completions.create(
        model="gpt-4o",
        messages=mensagens,
        temperature=0.3,
        max_tokens=3000
    )

    return resposta.choices[0].message.content

# --- Interface principal ---
st.set_page_config(page_title="Gerador de Cenários QA", layout="wide")

st.title("🧪 Agent IA - Gerador de Cenários BDD")
st.write("Forneça as informações abaixo para gerar cenários de teste completos em formato Gherkin.")

atividade = st.text_input("Nome da Atividade")
historia_usuario = st.text_area("História de Usuário")
regras_negocio = st.text_area("Regras de Negócio (opcional)")
criterios_aceitacao = st.text_area("Critérios de Aceitação (opcional)")

arquivos = st.file_uploader("Enviar imagens ou PDFs (opcional)", type=["png", "jpg", "jpeg", "pdf"], accept_multiple_files=True)

if st.button("Gerar Cenários"):
    if not atividade or not historia_usuario:
        st.warning("Por favor, informe pelo menos o Nome da Atividade e a História de Usuário.")
    else:
        with st.spinner("Gerando cenários, aguarde..."):
            resultado = gerar_cenarios(historia_usuario, regras_negocio, criterios_aceitacao, arquivos)
            st.success("Cenários gerados com sucesso!")
            st.download_button("📥 Baixar como .md", resultado, file_name=f"{atividade.replace(' ', '_')}.md")
            st.text_area("Resultado", resultado, height=500)
