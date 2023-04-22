from django.urls import path
from .views import MainPageView, DictionaryListView, DictionaryDetailView


app_name = "personal_area"

urlpatterns = [
    path("", MainPageView.as_view(), name="main-page"),
    path("dictionaries/", DictionaryListView.as_view(), name="dictionary-list"),
    path("dictionary/<int:pk>/", DictionaryDetailView.as_view(), name="dictionary-detail"),
]
