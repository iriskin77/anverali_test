from fastapi import HTTPException, APIRouter
from .schema import ContactRequest, ContactResponse
from .services import set_gender


router = APIRouter()


@router.post("/", response_model=ContactResponse)
def get_person_contact(item: ContactRequest):

    try:
        person = set_gender(contacts=item)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"database error: {ex}")
    return person
