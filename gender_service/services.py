from .schema import PersonContactRequest
from .models import MenNames, WomenNames
from django.db.models import Q


def set_gender(contacts: PersonContactRequest) -> dict:

    man = MenNames.objects.filter(
        Q(bitrix_id=contacts.bitrix_id) &
        Q(names_man=contacts.name)
    ).first()

    if man is not None:
        man.gender = "Мужской"
        man.save()
        return {"bitrix_id": man.bitrix_id, "name": man.names_man, "gender": "Мужской"}

    woman = WomenNames.objects.filter(
        Q(bitrix_id=contacts.bitrix_id) &
        Q(names_woman=contacts.name)
    ).first()

    if woman is not None:
        woman.gender = "Женский"
        woman.save()
        return {"bitrix_id": woman.bitrix_id, "name": woman.names_woman, "gender": "Женский"}



