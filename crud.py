# crud.py is for communication with your extensions database

# add your dependencies here
# from .models import createExample, Example
from lnbits.db import Database

db = Database("ext_paylistmod")

# add your fnctions here

# async def create_a_record(data: Example) -> createExample:
#     paylistmod_id = urlsafe_short_hash()
#     paylistmod = Example(id=paylistmod_id, **data.dict())
#     await db.insert("paylistmod.paylistmod", paylistmod)
#     return paylistmod


# async def get_a_record(paylistmod_id: str) -> Optional[Example]:
#     return await db.fetchone(
#         "SELECT * FROM paylistmod.paylistmod WHERE id = :id", {"id": paylistmod_id}, Example
#     )
