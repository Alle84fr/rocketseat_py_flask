<h1> Observações </h1>

<h3>Comandos VS Code</h3>

<span style="color: #ff8922;"> ctrl J</span> para abrir terminal

<span style="color: #ff8922;"> ls</span> lista os arquivos e diretórios

<h3>Instalação requirements, requisitos</h3>

pip - não é aceito no PATH do sistema, então deve usar o comando com python

python - é o interpretador a ser usado

-m - module, executar o módulo todo

pip - gerenciador de pacotes do .py, instala as bibliotecas

-r - abreviação de requirementes, é para ler o arquivo, no caso requirements.txt

<span style="color: #ff8922;"> python -m pip install -r requirements.txt</span> lista os arquivos e diretórios

<h3>Resposta HTML</h3>

<span style="color: #ff8922;"> 200</span> solicitação bem sucedida

<span style="color: #ff8922;"> 201</span> Recurso criado

<span style="color: #ff8922;"> 202</span> solicitação aprovada, mas processo não iniciado ou concluido

<span style="color: #ff8922;"> 400</span> Erro do cliente, solicitação inválida

<span style="color: #ff8922;"> 401</span> Não autorizado, solicitação não processada devido erro na autentificação

<span style="color: #ff8922;"> 449</span> Tente novamente, servidor não processou a solicitação porque o cliente não forneceu informações necessárias

<span style="color: #ff8922;"> 500</span> Erro do servidor 

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