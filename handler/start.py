from core import dp
from asyncio import gather, create_task
from loguru import logger

from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart

from db import AsyncSession
from db.sql import select
from db.base import UserTable

import template.start as start


@dp.message_handler(CommandStart())
async def start_handler(
    ctx : Message,
    db : AsyncSession
) -> None:
    """
    Start handler
    """
    chat_id = ctx.chat.id

    print(chat_id)

    await ctx.answer(
        text=start.hello.format(data=ctx),
        reply_markup=start.kb()
    )
    
    user = await db.execute(
        select(UserTable).where(
            UserTable.chat_id == chat_id
        )
    )

    if (usr:=user.fetchone()) is not None:
        return await db.close()

    print(usr)

    db.add(UserTable(
        chat_id=chat_id
    ))

    logger.info("New user")
    return await db.commit()