# #     """
"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
import django
from fastapi.middleware.cors import CORSMiddleware


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anverali.settings")
django.setup()
application = get_asgi_application()

from gender_service.handlers import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
fastapp = app

origins = ["*"]

fastapp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
