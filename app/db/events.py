import asyncpg
from fastapi import FastAPI
from loguru import logger

from app.core.config import DATABASE_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from time import sleep


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to {0}", repr(DATABASE_URL))
    count = 0

    while count < 2:
        try:
            logger.info("try connecting... {0}", count)
            app.state.pool = await asyncpg.create_pool(
                str(DATABASE_URL),
                min_size=MIN_CONNECTIONS_COUNT,
                max_size=MAX_CONNECTIONS_COUNT,
            )

            logger.info("Connection established")
            break
        except:
            count += 1
            sleep(2)



async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    await app.state.pool.close()

    logger.info("Connection closed")