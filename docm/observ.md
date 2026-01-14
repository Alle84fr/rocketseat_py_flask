<h1> Observações </h1>

<h3>Comandos VS Code</h3>

<span style="color: #ff8922;"> ctrl J</span> para abrir terminal

<span style="color: #ff8922;"> ls</span> lista os arquivos e diretórios

<span style="color: #ff8922;"> shift alt tecla cima pu baixo</span> copia a linha que esta marcada ou cok cursor

<span style="color: #ff8922;"> python app.py</span> mesmo que apertar play

<h3>Instalação requirements, requisitos</h3>

pip - não é aceito no PATH do sistema, então deve usar o comando com python

python - é o interpretador a ser usado

-m - module, executar o módulo todo

pip - gerenciador de pacotes do .py, instala as bibliotecas

-r - abreviação de requirementes, é para ler o arquivo, no caso requirements.txt

<span style="color: #ff8922;"> python -m pip install -r requirements.txt</span> lista os arquivos e diretórios

<h3>Resposta HTML</h3>

<span style="color: #ff8922;"> 200 OK</span> solicitação bem sucedida

<span style="color: #ff8922;"> 201 Created</span> Recurso criado

<span style="color: #ff8922;"> 202 Accepted </span> solicitação aprovada, mas processo não iniciado ou concluido, ex tarefa assíncrona, fila

<span style="color: #ff8922;"> 204 No Content </span> Sem conteúdo, deu certo mas não tem retorno, ex de uso, quando deletado com sucesso.

<span style="color: #ff8922;"> 400 Bad request </span> Erro do cliente, solicitação inválida, tipo errado do dado(int e não string), sem campo obrigatório, payload mal feito

<span style="color: #ff8922;"> 401 Unauthorized </span> Não autorizado, solicitação não processada devido erro na autentificação, é para login/autenticação

<span style="color: #ff8922;"> 403 Forbidden </span> Proibido, autenticado porém sem permissão "de uso, login"

<span style="color: #ff8922;"> 404 Not Found </span> Não encontrado, recurso inexistente, produto não encontrado, rota inexistente

<span style="color: #ff8922;"> 405 Method Not Allowed </span> Método não permitido, ex verbo é post e colocou-se get

<span style="color: #ff8922;"> 409 Conflict </span> Conflito, email já existente, produto duplicado

<span style="color: #ff8922;"> 500 Internal Server Error </span> Erro do servidor, bug do cod, erro do banco, exceção não tratada, nunca culpa do cliente, Erro interno, falha no backend

<h3>Erro flask shell</h3>

1° ver versão do flask

<span style="color: #ff8922;"> python -m flask --version</span> 

> Python 3.13.3
Flask 2.3.0
Werkzeug 2.3.0

usar <span style="color: #ff8922;"> python -m flask shell</span>

<h3>Métodos HTTP</h3>

<span style="color: #ff8922;"> GET</span> BUSCAR, LER, não altera, geralmente não tem payload
<span style="color: #ff8922;"> POST</span> CRIAR, CADASTRAR possui paylaod
<span style="color: #ff8922;"> PUT</span> ATUALIZAR TUDO
<span style="color: #ff8922;"> PATCH</span>  ATUALIZA PARTE, alguns campos 
<span style="color: #ff8922;"> DELETE</span> REMOVE, geralmente não tem payload