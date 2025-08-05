Funcionalidade: Integração de Blockchain para Contratos do Detran DF

Contexto:
  Dado que o sistema deve permitir a consulta e download de documentos NFT para contratos registrados com sucesso no DF

# Cenários positivos
Cenário: Exibir documento com token NFT
  Dado que o contrato está registrado com sucesso no DF
  Quando o usuário clica no link "Exibir documento com token NFT"
  Então um pop-up com o certificado deve ser exibido

Cenário: Baixar documento com token NFT
  Dado que o contrato está registrado com sucesso no DF
  Quando o usuário clica no link "Baixar documento com token NFT"
  Então o arquivo .PDF deve ser baixado corretamente

Cenário: Exibir tooltip com informação sobre NFT
  Dado que o usuário está na tela de espelho do contrato
  Quando o usuário passa o mouse sobre o ícone de informação
  Então a mensagem do tooltip deve ser exibida corretamente

# Cenários negativos
Cenário: Links não exibidos para contratos não registrados
  Dado que o contrato não está registrado com sucesso no DF
  Quando o usuário acessa a tela de espelho do contrato
  Então os links para exibição e download do NFT não devem ser exibidos

Cenário: Tentativa de download com erro de rede
  Dado que o contrato está registrado com sucesso no DF
  E há um problema de rede
  Quando o usuário clica no link "Baixar documento com token NFT"
  Então uma mensagem de erro de download deve ser exibida

# Cenários de limite
Cenário: Tooltip com texto muito longo
  Dado que o usuário está na tela de espelho do contrato
  Quando o usuário passa o mouse sobre o ícone de informação
  Então o tooltip deve ser exibido corretamente sem cortar o texto

# Cenários de segurança
Cenário: Proteção contra XSS no tooltip
  Dado que o usuário está na tela de espelho do contrato
  Quando o usuário passa o mouse sobre o ícone de informação
  Então o sistema não deve executar scripts maliciosos

Cenário: Acesso não autorizado aos documentos NFT
  Dado que o usuário não está autenticado
  Quando o usuário tenta acessar o link de exibição ou download do NFT
  Então o sistema deve redirecionar para a tela de login

# Esquema do Cenário com exemplos
Esquema do Cenário: Validação de campos obrigatórios
  Dado que o usuário está na tela de registro de contrato
  Quando o usuário tenta submeter o formulário com campos obrigatórios vazios
  Então uma mensagem de erro deve ser exibida para cada campo vazio

  Exemplos:
    | campo          | valor  |
    | CPF            | ""     |
    | e-mail         | ""     |
    | telefone       | ""     |

📌 Dúvidas sobre a Atividade:
- Como será tratada a expansão para outros estados? Haverá diferenças no comportamento?
- Existem restrições específicas para o layout do arquivo PDF?
- Quais são os navegadores suportados para garantir compatibilidade?

Nenhuma dúvida identificada.