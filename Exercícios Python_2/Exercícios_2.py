# Mensagem para inseria a senha.
senha = str(input('Insira a senha: '))
# Declaração da senha CORRETA.
senha_correta = 'Senha123@'
# Declaração de : se a senha que for inserida entiver correta vc esta LOGADO se não: esta INCORRETO.
if senha == senha_correta:
    print('Você está logado')
else:
    print('Senha ou Usuario incorreto ')
# Fim...