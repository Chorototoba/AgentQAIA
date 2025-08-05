# agente_qa.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Sua chave da API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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

# Chamar a API do Gemini
def gerar_cenarios(prompt):

    model = genai.GenerativeModel(model_name="gemini-1.5-pro")

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.3,
            "max_output_tokens": 3000,
        }
    )

    return response.text

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
    with open("output/cenarios_gerados.md", "w", encoding="utf-8") as f:
        f.write(resultado)

    print("\n✅ Arquivo salvo em output/cenarios_gerados.md")
