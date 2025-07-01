# Wiki

Este é meu projeto final do curso CS50W, uma enciclopédia online parecida com a Wikipedia.

O objetivo foi criar um site onde fosse possível acessar, buscar, criar, editar e explorar páginas com conteúdo escrito em Markdown. Esse conteúdo é automaticamente convertido para HTML. O projeto foi desenvolvido usando Django e segue todos os requisitos propostos na especificação do curso.

## Funcionalidades implementadas

- Acesso direto a qualquer entrada pela URL `/wiki/NOME_DA_ENTRADA`
- Página de índice com links clicáveis para todas as entradas
- Campo de busca funcional:
  - Redireciona direto se a busca for exata
  - Lista resultados parciais se a busca for por substring
- Criação de novas entradas com título e conteúdo em Markdown
- Validação para impedir criação de páginas com título já existente
- Edição de entradas com preenchimento automático do conteúdo atual
- Redirecionamento automático para a página após a edição
- Página aleatória que exibe qualquer entrada existente
- Conversão do conteúdo Markdown para HTML usando o pacote `markdown2`

## Estrutura do projeto

- `encyclopedia/`: onde estão os arquivos de views, urls, templates e lógica do app
- `entries/`: pasta com os arquivos Markdown salvos para cada entrada
- `wiki/`: configurações principais do Django
- `manage.py`: arquivo principal para rodar a aplicação

## Como rodar localmente

1. Clone o repositório:
   git clone https://github.com/marcelledssantos/me50-marcelledssantos.git

2. Entre na pasta do projeto:
   cd me50-marcelledssantos

3. Crie e ative um ambiente virtual (opcional):
   python -m venv venv
   venv\Scripts\activate (no Windows)
   source venv/bin/activate (no Linux/macOS)

4. Instale as dependências:
   pip install -r requirements.txt

5. Execute o servidor:
   python manage.py runserver

6. Acesse no navegador:
   http://127.0.0.1:8000

---

Projeto desenvolvido como parte do curso CS50’s Web Programming with Python and JavaScript.
