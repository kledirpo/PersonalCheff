### Tips
> ### django-admin.py help 
> Exibe a lista de comandos suportados pelo Django

> ### django-admin.py startproject <nome do projeto>
> Cria um projeto com o nome informado

>### cd [nome do projeto]
> #### python manage.py runserver
> roda o projeto e inicia o servidor 

> Alteração de Idioma e timezone, fica no arquivo settings.py
> #### Proximo a linha 106


> Cria o modulo(app) com o nome informado
> #### python manage.py startapp NOME-DO-MODULO

> Para adicionar código python em uma pagina HTML podemos utilizar dois tipos de limitadorees
- {% <codigopython> %} # Desta maneira o código é processado, porém não é exibido nada
- {{ <codigopython> }} # Desta maneira é utilizada para o caso de querermos resgatar o valor do código python na pagina, um exemplo é printar o valor de uma variavel.
> em todos os arquivos HTML que forem trabalhar com arquivos estaticos deve ser adicionado no começo do HTML o seguinte comando
``` {% load static %}```

>Por exemplo, caso formos adicionar uma imagem de uma logo, o código fica da seguinte maneira
`` <img src="{% static 'logo.png' %}">``

> Para adicionar uma URL para links de paginas utilizamos o seguinte comando

``<a href="{% url 'pagina' %}">NOME DA PAGINA</a>``



> Padrão de exemplo para estrutura de projeto
- Static
    style.css
    app.js
    img

- templates
    index.html
    partials
        header.html
        menu.html
        footer.html 