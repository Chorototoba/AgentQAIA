import os
from dotenv import load_dotenv
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# Carregar variáveis do .env
load_dotenv()

# Inicializar cliente Anthropic com a chave da API
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Carregar o prompt template
def carregar_prompt_template():
    with open("prompt.txt", "r", encoding="utf-8") as file:
        return file.read()

# Ler história de usuário
def ler_historia(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

# Gerar prompt completo
def gerar_prompt(historia_usuario, regras_negocio, criterios_aceitacao):
    prompt_template = carregar_prompt_template()
    return prompt_template.format(
        historia_usuario=historia_usuario,
        regras_negocio=regras_negocio,
        criterios_aceitacao=criterios_aceitacao
    )

# Chamar a API do Claude 3.5 Sonnet
def gerar_cenarios(prompt):
    # Construir o prompt no formato esperado pelo Claude
    full_prompt = (
        HUMAN_PROMPT
        + prompt
        + AI_PROMPT
    )
    
    response = client.completions.create(
        model="claude-3.5-sonnet",
        prompt=full_prompt,
        max_tokens_to_sample=3000,
        temperature=0.3,
        stop_sequences=[HUMAN_PROMPT],
    )
    
    return response.completion.strip()

# MAIN
if __name__ == "__main__":
    historia_usuario = ler_historia("historias/historia1.txt")

    # Você pode colocar as regras e critérios direto aqui ou ler de um arquivo
    regras_negocio = """
    - Todos os campos obrigatórios devem ser validados.
    - Validar CPF, e-mail e telefone.
    - Não permitir submissão com campos obrigatórios vazios.
    """

    criterios_aceitacao = """
    - Aceita ficha completa e correta.
    - Exibe erros em caso de campos vazios ou inválidos.
    """

    prompt = gerar_prompt(historia_usuario, regras_negocio, criterios_aceitacao)

    resultado = gerar_cenarios(prompt)

    print("\n=== Resultado ===\n")
    print(resultado)

    # Salvar saída
    os.makedirs("output", exist_ok=True)
    with open("output/cenarios_gerados.md", "w", encoding="utf-8") as f:
        f.write(resultado)

    print("\n✅ Arquivo salvo em output/cenarios_gerados.md")
