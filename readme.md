Pré-requisitos
Certifique-se de ter o Python 3 instalado em seu sistema. Além disso, é recomendado o uso de um ambiente virtual para isolar as dependências do projeto.

Configuração do ambiente
Crie e ative um ambiente virtual:
```
python3 -m venv myenv
source myenv/bin/activate

```
Instale as dependências:
```
pip install -r requirements.txt
```


Executando a aplicação
Para executar a aplicação junto com o banco de dados PostgreSQL e o RabbitMQ, siga as etapas abaixo:

Abra um terminal na pasta raiz do projeto, onde o arquivo docker-compose.yml está localizado.

Execute o seguinte comando para criar e iniciar os contêineres:

``` docker-compose up --build -d```

Consumidor
Parar executar o consumidor asyc executer o seguinte comando:

```
 python main.py
 
```
Aguarde o processamento assíncrono pelo serviço 
