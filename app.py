from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from config import DB_PASS, DB_PORT, DB_USER, BOT_TOKEN, DB_NAME, DB_HOST
import asyncio
import asyncpg
import logging

bot = Bot(BOT_TOKEN)
dp = Dispatcher(MemoryStorage())


async def on_startup(bot: Bot) -> None:
    # Установка команд бота
    await bot.set_my_commands([
        BotCommand(command="start", description="Перезапустить бота")
    ])

    # Создание пула базы данных
    dp["db"] = await asyncpg.create_pool(
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        host=DB_HOST,
        max_size=100
    )


async def on_shutdown() -> None:
    if "db" in dp.workflow_data:
        await dp["db"].close()

async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    logging.basicConfig(filename='log.log', level=logging.DEBUG)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
        
        
if __name__ == '__main__':
    asyncio.run(main=main())