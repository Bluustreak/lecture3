from django.urls import path
from . import views

urlpatterns=[
    # format is probably (URL ending, the actual file, ID)
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("kevin", views.kevin, name="kevin"),
    path("<str:name>", views.greet, name="greet"),
]