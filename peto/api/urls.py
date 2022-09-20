from .views import PetoGetCreate , PetoUpdateDelete
from django.urls import path ,include
urlpatterns = [
path('',PetoGetCreate.as_view()),
path('<int:pk>',PetoUpdateDelete.as_view()),
#  path('api-auth/', include('rest_framework.urls')),
 
]