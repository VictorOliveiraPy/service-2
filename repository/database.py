import motor.motor_asyncio


async def insert_db(dados):
    conn_str = "mongodb://root:password@127.0.0.1"
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)
    db = client["test"]
    marcas_collection = db["marcas"]

    await marcas_collection.insert_one(dados)
    print("Saved Data")

    client.close()
