from django.urls import path
from place.views import ListPlaceApiView, PlaceByIdApiView, CreatePlaceApiView, PlaceUpdate

app_name = 'place'

urlpatterns = [
    path('all-place/', ListPlaceApiView.as_view()),
    path('place/<int:pk>/', PlaceByIdApiView.as_view()),
    path('create-place/', CreatePlaceApiView.as_view()),
    path('update-place/<int:pk>/', PlaceUpdate.as_view()),

]