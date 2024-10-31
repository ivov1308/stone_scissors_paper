import asyncio

from aiogram import Bot, Dispatcher
from config_data import Config, load_config
import handlers


async def main():

    config: Config = load_config()

    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
