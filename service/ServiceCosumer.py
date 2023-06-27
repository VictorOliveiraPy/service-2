import asyncio
import json

import aio_pika
import httpx

from config import configs
from repository.database import insert_db


async def get_vehicle_models(code):
    async with httpx.AsyncClient() as client:
        url = f'{configs.API_URL}/{code}/modelos'
        response = await client.get(url)
        return response.json()


async def process_message(
        message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    async with message.process():
        data = json.loads(message.body)
        vehicle_models = await get_vehicle_models(data['codigo'])
        await insert_db(vehicle_models)


async def run_consumer() -> None:
    connection = await aio_pika.connect_robust(
       configs.BROKER_URL
    )

    # Creating channel
    channel = await connection.channel()

    # Maximum message count which will be processing at the same time.
    await channel.set_qos(prefetch_count=100)

    # Declaring queue
    queue = await channel.declare_queue(configs.QUEUE_NAME, auto_delete=True)

    await queue.consume(process_message)

    try:
        # Wait until terminate
        await asyncio.Future()
    finally:
        await connection.close()
