# PersonalCheff
<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
> Aplicativo de receitas, PersonalCheff, desenvolvido para o curso de Programação Web com Python na escola Senac Americana, o Foco dessa aplicação será apresentar receitas para o churrasco.
### Lista de tarefas
Segue a lista de tarefas a serem desenvolvidas no projeto:
- [X] Pré-requisitos
    - [X] Instalar o Python
    - [X] Instalar Visual Studio Code

- [X] Criar e ativar o ambiente virtual
- [X] Instalar o Django
- [X] Criar o Projeto PersonalCheff
- [X] Subir o Servidor e testar a aplicação
- [X] Alterar o idioma para `pt-br`
- [X] Alterar o timezone para `America/Sao_Paulo`
- [X] Registrar o App Receitas
```
    Adicionado no arquivo settings.py, no tópico INSTALLED_APPS, adicionado guia para o aplicativo receitas
````
- [X] Configurar a rota inicial (index)
- [X] Criar a View para a rota inicial
- [X] Registrar a rota inicial
- [X] Criar o arquivo index.html
    - Dentro da pasta receitas(app), crie a pasta `templates`
    - Dentro da pasta `templates`crie seus arquivos HTML começando pelo `index.html`
    - No arquivo `views.py` que está dentro da pasta do app faça a seguinte alteração de código: 
    ```python
    from django.shortcuts import render

    def index(request):
        return render(request,'index.html')
    ```
- [X] Integrar arquivos estáticos (CSS, JS, IMG)
- [X] Utilizando links
- [X] Criando o base.html
- na pasta `templates` crie o arquivo `base.html`.
- Este Arquivo contém todo o código de estrutura comum á todas as paginas. NEste arquivo deve ficar tudo que estiver antes do `body` e tudo que estiver depois do `/body`.
- Neste arquivo deve conter o `{% load static %}
- Neste arquivo, no local onde será carregado o conteudo das outras paginas, deve existir os delimitadores `{% block content %} e `{% endblock %}
- [X] Separando em partials
- [x] Renderizando dados dinamicamente
- [x] Criando um dicionario com as receitas
- [x] Criando o banco de dados(MySQL/MariaDB)
- [X] Instalando o conector do bando de dados MySQL
- [X] Criando o modelo da receita
- [X] Criando a migration (mapeamento)
- [X] Realizando a migration
- [X] Registrando um modelo no admin
- [X] Criando um usuário para o ambiente administrativo


### Criação e ativação do Venv(terminal cmd)
>python -m venv .\venv\
venv\Scripts\activate

### Instalação do Django
> python -m pip install django==3.2

## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE) para mais detalhes.
[⬆ Voltar ao topo](#PersonalCheff)<br>