# meuGabarito
Uma webaplicação para criar e corrigir seus próprios gabaritos durante alguma sessão de estudo que esteja fazendo.



## Tecnologias utilizadas
- [Python](https://www.python.org/)
  - [Django](https://www.djangoproject.com/)
  - [Django Widgets Tweaks](https://pypi.org/project/django-widget-tweaks/)
- [Bootstrap](https://getbootstrap.com/)
- [JQuery](https://jquery.com/)


Para o backend do site eu usei o **Django** com o banco de dados **SQLite3** que já vem configurado por padrão com ele;

As telas foram feitas com os componentes do **Bootstrap**, deixei tudo bem simples, não fiz nenhuma modificação;

O **Django widget tweaks** foi usado na renderização dos formulários nos templates do django;

O **JQuery** foi usado para implmentação de requisições assíncronas nas partes de marcar alternativa e corrigir gabarito
para que a página não precisasse regarregar a cada clique do usuário e ele tivesse que sempre rolar a página para a questão
em que estava modificando.

Além dessas tecnologias, eu utilizei o programa [GIMP](https://www.gimp.org/) e a ferramenta online <https://realfavicongenerator.net/> para a criação do favicon do site.



## Ideia do projeto
Quando eu estava estudando para o ENEM em 2020, eu costumava resolver as questões das provas anteriores e depois verificar quantas tinha acertado.
Nesse processo eu notei que era bem recorrente eu confundir a ordem das respostas na hora de corrigir e ter de recomeçar a correção por estar anotando
tudo no bloco de notas do Windows. Então, para facilitar minha vida, eu criei um projetinho em django que me permitisse registrar as respostas enquanto
eu estava fazendo as questões para depois corrigir de forma organizada. Acabou ficando bem bagunçado porque eu fiz nas pressas e era algo só para quebrar
um galho, então esse mês eu resolvi refazer essa minha ideia do zero para deixar o "produto final" melhor lapidado.
