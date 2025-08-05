Funcionalidade: Integração de Blockchain para Contratos do Detran DF

  Contexto:
    Dado que o sistema está integrado com o Blockchain para contratos do Detran DF

  # Cenários Positivos
  Cenário: Exibir documento com token NFT
    Dado que o contrato está registrado com sucesso no DF
    Quando o usuário clica no link "Exibir documento com token NFT"
    Então um pop-up com o certificado deve ser exibido

  Cenário: Baixar documento com token NFT
    Dado que o contrato está registrado com sucesso no DF
    Quando o usuário clica no link "Baixar documento com token NFT"
    Então um arquivo .PDF deve ser baixado

  Cenário: Exibir tooltip com informação sobre NFT
    Dado que o usuário está na seção de TOKENIZAÇÃO
    Quando o usuário passa o mouse sobre o ícone de informação
    Então a mensagem explicativa sobre NFT deve ser exibida

  # Cenários Negativos
  Cenário: Contrato não registrado não exibe links
    Dado que o contrato não está registrado com sucesso
    Quando o usuário acessa a seção de TOKENIZAÇÃO
    Então os links para exibição e download do NFT não devem ser exibidos

  Cenário: Tentativa de exibir documento sem registro
    Dado que o contrato não está registrado com sucesso
    Quando o usuário tenta clicar no link "Exibir documento com token NFT"
    Então uma mensagem de erro deve ser exibida

  Cenário: Tentativa de baixar documento sem registro
    Dado que o contrato não está registrado com sucesso
    Quando o usuário tenta clicar no link "Baixar documento com token NFT"
    Então uma mensagem de erro deve ser exibida

  # Cenários Extras/Imaginados
  Cenário: Exibir documento em diferentes navegadores
    Dado que o contrato está registrado com sucesso no DF
    Quando o usuário clica no link "Exibir documento com token NFT" em diferentes navegadores
    Então o pop-up com o certificado deve ser exibido corretamente em todos os navegadores

  Cenário: Baixar documento em diferentes dispositivos
    Dado que o contrato está registrado com sucesso no DF
    Quando o usuário clica no link "Baixar documento com token NFT" em diferentes dispositivos
    Então o arquivo .PDF deve ser baixado corretamente em todos os dispositivos

  # Cenários para Regras de Negócio - Sucesso
  Cenário: Validação de campos obrigatórios
    Dado que todos os campos obrigatórios estão preenchidos corretamente
    Quando o usuário submete o contrato
    Então o contrato deve ser registrado com sucesso

  # Cenários para Regras de Negócio - Erros
  Cenário: Campos obrigatórios vazios
    Dado que um ou mais campos obrigatórios estão vazios
    Quando o usuário tenta submeter o contrato
    Então uma mensagem de erro deve ser exibida

  Cenário: CPF inválido
    Dado que o CPF informado é inválido
    Quando o usuário tenta submeter o contrato
    Então uma mensagem de erro deve ser exibida

  # Esquema do Cenário com exemplos
  Esquema do Cenário: Validação de campos obrigatórios
    Dado que os campos obrigatórios estão preenchidos
    Quando o usuário submete o contrato
    Então o sistema deve validar os campos corretamente

    Exemplos:
      | campo       | valor          |
      | CPF         | 123.456.789-00 |
      | E-mail      | teste@exemplo.com |
      | Telefone    | (61) 91234-5678 |

📌 Dúvidas sobre a Atividade:
- Como será tratado o caso de contratos parcialmente registrados?
- Existem restrições específicas para o layout do arquivo PDF?
- Há necessidade de testes de carga para o download dos documentos?