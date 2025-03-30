from fastapi import APIRouter, Depends
from lnbits.decorators import check_user_exists
from . import paylistmod_ext

@paylistmod_ext.get("/")
async def paylistmod_page(user=Depends(check_user_exists)):
    return paylistmod_ext.send_template(
        "paylistmod/index.html",
        user=user,
        title="Payment List"
    )
