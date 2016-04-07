# simple-route
App para calcular a rota mais curta entre pontos distintos, com estimativa de gastos, usando malha logística.


Usei as seguintes tecnologias para desenvolvimento dessa aplicação:

postgresql para banco de dados em produção
sqlite3 para banco de dados de desenvolvimento.

Nginx para servidor web em produção
supervisord para gerenciar os serviços
gunicorn com wsgi

Virtualenv para serparar os ambientes

Python Versão 2.7

O sistema operacional utilizado foi o ubuntu 32 bits, entretanto gostaria de usar o centos 64 bits, não foi possivel por limitações no ambiente que foi utilizado para desenvolvimento.

observações: Com o aumento da utilização do servidor, se faz necessário utilizar outras ferramentas, como mongoDB para banco de dados,
             juntamente com uma ferramente de cache, podendo ser o memcached, e sem dúvidas restruturar a arquitetura do app, tirando 
             banco de dados do mesmo servidor entre outras melhorias.


#Instalação
1 - Rode o script install.sh com permissão de super usuario.
    
    Considerando que o ubuntu esta atualizado corretamente, o script ira instalar o nginx 
    e configura-lo, também criar uma virtualenv dentro do projeto.

    Lembrando que não considerei usar um dns, usei o endereço local para simular, o wsgi 
    esta apontando para o settings_production que esta usando postgresql. Então será preciso
    baixar o postgresql e configurar um usuário, para faciltar crie o usuario com nome de 
    postgres e sem senha, o database com nome de route, caso crie as credencias diferentes,
    alterar o arquivo settings_production.py, dento de app/conf/.

2 - entrar na virtualenv

	source /simple-route/walmart/bin/activate

3 - instalar as dependencias do projeto

	make install


Até aqui no passo 4, ja podemos testar o projeto, com as ferramentas sitadas de desenvolvimento.

4 - Rodar localmente para desenvolvimento 

	make database
	
	make migrate
	
	make run

Para continuar o deploy e usar o nginx para produção.

5 - Dentro de extras/supervisord/supervisord.conf, coloque
    este arquivo dentro de /etc/supervisor/supervisord.conf
    *lembre de salvar o original.

6 - Vamos iniciar o supervisord 
	
	sudo supervisord -c /mypath/supervisord.conf

	sudo supervisorctl -c /mypath/supervisord.conf 

Pronto, podemos rodar tanto para produção, ou desenvolvimento com esses passos.


#Sobre a API.


| URI            			           | MÉTODO | DESCRICÃO        		                                                                                                                     |
|--------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `/delivery/maps/list`          		           | GET    | Retorna todos os mapas e pontos.                                                                                           |
| `/delivery/maps/list`            | POST    | Cria um novo mapa.                                                                           |
| `/delivery/maps/nome`          		           | GET   | Detalha um mapa.                                                                                                                     |
| `/delivery/maps/nome`            | PUT | Altera um map.                                                                |
| `/delivery/maps/nome`                 | DELETE   | Apaga o mapa indicado.                                                                                    |
| `/delivery/routes/list`           | GET | Lista as rotas.                                                                    |
| `delivery/routes/list` 				           | POST    | Cria uma nova rota                                                                                        |
| `/delivery/routes/id`                   | GET    | Detalha uma rota                                                                         |
| `/delivery/routes/id`        | PUT   | Altera uma rota |
| `/delivery/routes/id`                      | DELETE | Remove a rota.                                                                                                      |
| `/delivery/routes/price_route` | POST    | Calular a distancia entre as rotas e o preço que sera gasto de combustivel.           |


### Utilização

    para cadastrar um mapa ex: POST
        {
            "name_map": "SP",
            "description_map": "teste",
            "route_map": []
        }

    para alterar um mapa ex: PUT
        {
            "name_map": "SP",
            "description_map": "teste2",
            "route_map": []
        }

    para deletar um mapa ex: DELETE
        {
            "name_map": "SP",
            "description_map": "teste2",
            "route_map": []
        }

    listar os mapas ex: GET
        http://localhost:7000/delivery/maps/list/

    listar mapa especifico: GET
        http://localhost:7000/delivery/maps/SP/


    para cadastrar uma rota ex: POST
        {
            "origin_route": "A",
            "destination_route": "C",
            "distance_route": "10",
            "description_route": "teste",
            "id_map": 2
        }

    para alterar uma rota ex: PUT
        {
            "origin_route": "A",
            "destination_route": "C",
            "distance_route": "10",
            "description_route": "test2",
            "id_map": 2
        }

    para deletar uma rota ex: DELETE
        {
            "origin_route": "A",
            "destination_route": "C",
            "distance_route": "10",
            "description_route": "test2",
            "id_map": 2
        }

    listar as rotas ex: GET
        http://localhost:7000/delivery/routes/list/

    listar rota especifica: GET
        http://localhost:7000/delivery/routes/1/

    calcular a rota ex: POST
    	curl -X POST -d '{"fuel": "2.50", "origin": "A", "destination": "D","autonomy": "10", "map": "SP"}'  -H "Content-Type: application/json" http://localhost:7000/delivery/routes/price_route/

Todos os metodos tem uma interface com as instruções e caracteristicas.

Ex: abrir diretamente no navegador http://localhost:7000/delivery/maps/list

    É possivel cadastrar via insterface de admin.
    http://localhost:7000/admin
    credenciais foram criadas durante o deploy.


### TESTES

make test

Lembre de dar permissão ao script runtests
