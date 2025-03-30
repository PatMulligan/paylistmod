import asyncio

from fastapi import APIRouter
from loguru import logger

from .crud import db
from .tasks import wait_for_paid_invoices
from .views import paylistmod_ext_generic
from .views_api import paylistmod_ext_api

paylistmod_ext: APIRouter = APIRouter(prefix="/paylistmod", tags=["paylistmod"])
paylistmod_ext.include_router(paylistmod_ext_generic)
paylistmod_ext.include_router(paylistmod_ext_api)

paylistmod_static_files = [
    {
        "path": "/paylistmod/static",
        "name": "paylistmod_static",
    }
]

scheduled_tasks: list[asyncio.Task] = []


def paylistmod_stop():
    for task in scheduled_tasks:
        try:
            task.cancel()
        except Exception as ex:
            logger.warning(ex)


def paylistmod_start():
    from lnbits.tasks import create_permanent_unique_task

    task = create_permanent_unique_task("ext_testing", wait_for_paid_invoices)
    scheduled_tasks.append(task)


__all__ = [
    "db",
    "paylistmod_ext",
    "paylistmod_static_files",
    "paylistmod_start",
    "paylistmod_stop",
]
