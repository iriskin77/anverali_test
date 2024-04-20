from .schema import MenNames, WomenNames, ContactRequest
from .models import MenNames, WomenNames, Gender
from django.db.models import Q


def set_gender(contacts: ContactRequest) -> dict:

    man = MenNames.objects.filter(Q(id=contacts.id) & Q(names_man=contacts.name)).first()
    if man is not None:
        gender = Gender.objects.get(gender="M")
        man.gender = gender
        man.save()
        return {"id": man.id, "name": man.names_man, "gender": "M"}

    woman = WomenNames.objects.filter(Q(id=contacts.id) & Q(names_woman=contacts.name)).first()
    if woman is not None:
        gender = Gender.objects.get(gender="F")
        woman.gender = gender
        woman.save()
        return {"id": woman.id, "name": woman.names_woman, "gender": "F"}



