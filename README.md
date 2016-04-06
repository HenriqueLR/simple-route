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
    esta apontando para o settings_production que esta usando postgresql, então sera preciso
    baixa-lo e configurar um usuário, caso crie um diferente de postgresql e sem senha, altere 
    somente em settings_production as novas credencias.

2 - entra na virtualenv

	source /simple-route/walmart/bin/activate

3 - make install

	ira instalar as dependencias do projeto.


Até aqui no passo 4, ja podemos testar o projeto, com as ferramentas sitadas de desenvolvimento.

4 - Rodar localmente para desenvolvimento 
	
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
| `/delivery/maps/SP`          		           | GET   | Detalha um mapa. mapa                                                                                                                      |
| `/delivery/maps/SP`            | PUT | Altera um mpap.                                                                |
| `/delivery/maps/SP`                 | DELETE   | Apaga o mapa indicado.                                                                                    |
| `/delivery/routes/list`           | GET | Lista as rotas.                                                                    |
| `delivery/routes/list` 				           | POST    | Cria uma nova rota                                                                                        |
| `/delivery/routes/4`                   | GET    | Detalha uma rota                                                                         |
| `/delivery/routes/4`        | PUT   | Alera uma rota |
| `/delivery/routes/4`                      | DELETE | Remove a rota.                                                                                                      |
| `/delivery/routes/price_route` | POST    | Calular a distancia entre as rotas e o preço que sera gasto de combustivel.           |



### Utilização

Todos os metodos tem uma interface com as instruções e caracteristicas, com exeção do calcular a rota.

Ex: abrir diretamente no navegador http://localhost/delivery/maps/list 

O metodo para calcular a rota pode ser testado da seguinte forma.

Ex: curl -X POST -d '{"fuel": "2.50", "origin": "A", "destination": "D","autonomy": "10", "map": "SP"}'  -H "Content-Type: application/json" http://localhost:7000/delivery/routes/price_route/

Ou com outro client para fazer requisições via post, baste que o load data seja como este.


### TESTES

make test
