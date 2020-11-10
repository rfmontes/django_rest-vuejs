# django_rest-vuejs
Site simples com Django Rest Framework e VueJs

- BACKEND (DJANGO REST FRAMEWORK)

- Instalar djangorestframework
pip install djangorestframework

- Instalar ipython
pip install ipython

- Criar projeto django-admin
django-admin.py startproject loja .

- Criar app
manage.py startapp produtos

- Criar Models
models.py (class Camisa e class Chuteira)

- Fazer migrações
manage.py makemigrations
manage.py migrate

- Cadastrar itens pelo ipython
manage.py shell
from produtos.models import Chuteira
from produtos.models import Camisa
camisa = Camisa() em seguida cadastrar os fields e save()
chuteira = Chuteira() em seguida cadastrar os fields e save()
Por fim exit

- Criar os serializers.py

- Ver itens cadastrados Serializados pelo ipython
manage.py shell
from produtos.models import Chuteira
from produtos.models import Camisa
from produtos.serializers import ChuteiraSerializer
from produtos.serializers import CamisaSerializer
camisa = Camisa.objects.first()
chuteira = Chuteira.objects.first()
ser = CamisaSerializer(camisa)
serC = ChuteiraSerializer(chuteira)
ser.data
serC.data

- Criar funções GET em views.py

- Criar endpoint em urls.py e produtos/urls.py

- Criar funções PUT, DELETE, POST em views.py

- Criar endpoint em produtos/urls.py

- Refatorar função camisa_list() e camisa_detail() para Classe baseada em view

- Refatorar Classes CamisaListCreate e CamisaDetail

- Refatorar novamente usando viewsets do djagorestframework, que implementa todas as funções criadas antes



- FRONTEND (VUE.JS)

- create vue frontend

- cd frontend

- npm run serve

- npm install axios / npm install bootstrap-vue

- Apagar HellWorld.vue

- criar pasta views, para colocar as telas criadas

- npm install vue-router (para trabalhar com rotas no vue)

- criar arquivo router.js

- criar Home.vue na pasta views

- criar Camisas.vue e Chuteiras.vue na pasta views importar axios em cada um e fazer get no api rest criado no backend

- criar rotas para Home, Camisas e Chuteiras no router.js

- importar o router no main.js

- criar Navbar.vue com bootstrap-vue

- importar bootstrap-vue no main.js

- importar bootstrap css no main.js

- criar as rotas no Navbar.vue para Home, Camisas e Chuteiras 
(o b-nav-item ja esta integrado com o router-link to, ou seja basta colocar o url no to=)

- criar um data no Camisas.vue para carregar os valores vindos da api rest

- fazer um v-for para exibir os valores carregados no data no Camisas.vue

- criar EditCamisa.vue

- criar rotas pra EditCamisa.vue em router.js (/add e /:id/edit)

- criar botão adicionar para direcionar a rota de EditCamisa

- criar formulario para adicionar nova camisa em EditCamisa.vue

- criar data no EditCamisa.vue com os atributos da Camisa para cadastrados

- criar um v-model para atribuir um valor a cada data criado

- criar b-button com @click e um metodo para enviar dados via post pelo axios

- criar função para desabilitar quando o mesmo ja foi clicado

- criar botões editar e excluir no Camisas.vue

- criar função excluir no Camisas.vue

- no button editar criar to para /camisas/id/edit

- criar condição para editar no EditCamisas.vue, para editar e criar novas camisas
