from django.urls import path
from comment.views import ListEventCommentApiView, EventCommentByIdApiView, \
    CreateEventCommentApiView, EventCommentUpdate, EventCommentDelete

app_name = 'comment'

urlpatterns = [
    path('all-comments/', ListEventCommentApiView.as_view()),
    path('comment/<int:pk>/', EventCommentByIdApiView.as_view()),
    path('create-comment/', CreateEventCommentApiView.as_view()),
    path('update-comment/<int:pk>/', EventCommentUpdate.as_view()),
    path('delete-comment/<int:pk>/', EventCommentDelete.as_view())

]