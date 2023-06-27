from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    BROKER_URL: str = "amqp://admin:pass@127.0.0.1/"
    API_URL = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
    QUEUE_NAME = "test_queue"


configs = Config()
