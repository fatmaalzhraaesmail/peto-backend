from .views import AccountGetCreate , AccountUpdateDelete
from django.urls import path ,include
urlpatterns = [
path('',AccountGetCreate.as_view()),
path('<int:pk>',AccountUpdateDelete.as_view()),
#  path('api-auth/', include('rest_framework.urls')),
 
]