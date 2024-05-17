from django.urls import path
from event.views import ListEventApiView, CreateEventApiView, EventUpdate, EventDelete, \
    EventByIdApiView, AddMember

app_name = 'event'

urlpatterns = [
    path('all-events/', ListEventApiView.as_view()),
    path('event/<int:pk>/', EventByIdApiView.as_view()),
    path('create-event/', CreateEventApiView.as_view()),
    path('update-event/<int:pk>/', EventUpdate.as_view()),
    path('delete-event/<int:pk>/', EventDelete.as_view()),
    path('add-member/<int:pk>/', AddMember.as_view())

]