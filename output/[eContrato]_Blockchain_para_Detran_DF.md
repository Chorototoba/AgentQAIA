Funcionalidade: Integração de NFT em contratos do Detran DF

  Contexto:
    Dado que o usuário está autenticado no sistema
    E está visualizando um contrato registrado com sucesso no DF

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
    Dado que o usuário está na seção de TOKENIZAÇÃO
    Quando o usuário passa o mouse sobre o ícone de informação
    Então a mensagem explicativa sobre NFT deve ser exibida

  # Cenários negativos
  Cenário: Links não exibidos para contratos não registrados
    Dado que o contrato não está registrado com sucesso no DF
    Quando o usuário visualiza a seção de TOKENIZAÇÃO
    Então os links para exibição e download não devem ser exibidos

  Cenário: Tentativa de exibir documento sem registro
    Dado que o contrato não está registrado com sucesso no DF
    Quando o usuário tenta clicar no link "Exibir documento com token NFT"
    Então uma mensagem de erro deve ser exibida

  # Cenários de borda
  Cenário: Verificar limites de tamanho do arquivo PDF
    Dado que o contrato está registrado com sucesso no DF
    Quando o usuário baixa o documento
    Então o tamanho do arquivo PDF não deve exceder 10MB

  # Cenários de segurança
  Cenário: Prevenir injeção de código nos campos de entrada
    Dado que o usuário está preenchendo um formulário
    Quando o usuário insere um script malicioso
    Então o sistema deve rejeitar a entrada e exibir uma mensagem de erro

  Cenário: Prevenir acesso não autorizado aos documentos
    Dado que o usuário não está autenticado
    Quando o usuário tenta acessar o documento NFT
    Então o acesso deve ser negado

  # Regras de Negócio
  Cenário: Validação de campos obrigatórios
    Dado que o usuário está preenchendo um formulário de contrato
    Quando o usuário tenta submeter o formulário com campos obrigatórios vazios
    Então uma mensagem de erro deve ser exibida

  Cenário: Validação de CPF, e-mail e telefone
    Dado que o usuário está preenchendo um formulário de contrato
    Quando o usuário insere um CPF, e-mail ou telefone inválido
    Então uma mensagem de erro deve ser exibida

  # Esquema do Cenário com exemplos
  Esquema do Cenário: Validação de campos obrigatórios
    Dado que o usuário está preenchendo um formulário de contrato
    Quando o usuário tenta submeter o formulário
    Então uma mensagem de erro deve ser exibida

    Exemplos:
      | campo         | valor inválido |
      | CPF           | 123.456.789-00 |
      | e-mail        | email@invalido |
      | telefone      | 123456789      |