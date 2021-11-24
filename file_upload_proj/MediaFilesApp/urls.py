from django.urls import path
from .views import *

urlpatterns =[
    path('upload/',file_upload_view,name='upload'),
    path('displaydocs/',display_documents_view,name='display')
]