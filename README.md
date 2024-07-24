# Projeto de Tecnologias Emergentes

Este projeto é uma API que extrai dados de produtos do Mercado Livre e do Google Shopping. Permite que os utilizadores pesquisem produtos e obtenham informações como preços, avaliações e links.

Nesse projeto foram utilizadas as seguintes tecnologias:
- Python - Linguagem de programação
- MongoDB - Banco de dados não relacional
- FastAPI - API
- BeautifulSoup - Biblioteca de web-scraping para extrair os dados dos sites
- Docker e Docker Compose para colocar em containers as dependências necessárias e executar o projeto

Projeto seguindo requisitos de código limpo nos nomes de variáveis, cada função com um propósito e não vários

# Testes

Para rodar os testes:

```
python -m unittest discover -v -s tests/ -p '*_test.py'
```

## Características

- Extrai dados de produtos do Mercado Livre e do Google Shopping
- Suporta a busca de produtos por nome
- Recupera informações como preços, avaliações e links para cada produto
- Fornece endpoints para recuperar e excluir produtos de um banco de dados


## Uso

Para executar basta instalar o `Docker` e `Docker Compose` no seu sistema operacional e seguir os passos seguintes:

1. Clone o repositório:
```bash
git clone https://github.com/your-username/your-project.git
```

2. Navegue até o diretório:
```bash
cd your-project
```


3. Instale as dependências:
`Docker e docker-compose`

4. Dê build no docker-compose
```bash
docker-compose build
```

5. Execute
```bash
docker-compose up
```

5. Os endpoints estão no Swagger, no endereço: `https://localhost:8000/docs`

# Para colaborar com o projeto

Clone o repositório e instale `Docker e Docker Compose` e as dependências nos `requirements.txt` e criar as devidas issues e pull requests que serão analisadas e aprovadas, após revisão, quando de acordo.
