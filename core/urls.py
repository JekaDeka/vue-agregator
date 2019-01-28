from django.urls import path
from core.views import IndexView, IndexTownView, ManufactureView, MasterView, LoginView, NewLoginView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<country>/<town>/', IndexTownView.as_view()),
    path('<country>/register/login/', LoginView.as_view()),
    path('<country>/register/new_login/', NewLoginView.as_view()),
    path('<country>/register/manufacture/<int:id>/', ManufactureView.as_view()),
    path('<country>/register/master/<int:id>/', MasterView.as_view()),
]
