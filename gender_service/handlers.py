from fastapi import HTTPException, APIRouter
from .schema import PersonContactRequest, PersonContactResponse
from .services import set_gender


router = APIRouter()


@router.patch("/", response_model=PersonContactResponse)
def set_person_gender(item: PersonContactRequest):

    try:
        person = set_gender(contacts=item)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"database error: {ex}")
    return person
