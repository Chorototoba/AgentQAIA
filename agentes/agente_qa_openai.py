import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def carregar_prompt_template():
    with open("prompt.txt", "r", encoding="utf-8") as file:
        return file.read()

def ler_historia(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def gerar_prompt(historia_usuario, regras_negocio, criterios_aceitacao):
    prompt_template = carregar_prompt_template()
    return prompt_template.format(
        historia_usuario=historia_usuario,
        regras_negocio=regras_negocio,
        criterios_aceitacao=criterios_aceitacao
    )

def gerar_cenarios(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Você é um engenheiro de QA sênior especialista em testes BDD."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=3000
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    historia_usuario = ler_historia("AgentIA_QA/historias/historia.txt")

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

    with open("output/cenarios_gerados.md", "w", encoding="utf-8") as f:
        f.write(resultado)

    print("\n✅ Arquivo salvo em output/cenarios_gerados.md")
