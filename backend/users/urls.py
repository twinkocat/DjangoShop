from django.urls import path

from users.api.views import SelfView
from users.api.views import RegisterView

urlpatterns = [
    path('me/', SelfView.as_view()),
    path('register/', RegisterView.as_view())
]
