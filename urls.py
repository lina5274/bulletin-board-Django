from django.urls import path
from.views import edit_advertisement

urlpatterns = [
    path('edit-ad/<int:advertisement_id>/', edit_advertisement, name='edit_advertisement'),
]
