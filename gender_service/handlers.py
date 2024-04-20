from fastapi import FastAPI, HTTPException, APIRouter
from .schema import MenNames, WomenNames, ContactRequest, ContactResponse
from .services import set_gender


router = APIRouter()


#олучать данные контакта (ID, Имя) из Битрикс24 по Webhook проверять имя контакта на наличие его в БД (PostgreSQL)

@router.post("/", response_model=ContactResponse)
def get_person_contact(item: ContactRequest):

    print(item)

    #contacts = item.dict()

    # if "id" not in contacts:
    #     raise HTTPException(status_code=404, detail="id was not provided")
    #
    # if "name" not in contacts:
    #     raise HTTPException(status_code=404, detail="name was not provided")
    try:
        res = set_gender(contacts=item)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"database error: {ex}")
    return res
