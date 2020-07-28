"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import diaryapp.views
import profileapp.views
import albumapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profileapp.views.main, name='main'),
    path('community/', profileapp.views.community, name='community'),
    path('diary/', diaryapp.views.diary, name='diary'),
    path('write/', diaryapp.views.write, name='write'),
    path('album/', albumapp.views.album, name='album'),
    path('detail/<int:diary_id>', diaryapp.views.detail, name="detail"),
    path('prev/<int:diary_id>', diaryapp.views.prev, name="prev"),
    path('next/<int:diary_id>', diaryapp.views.next, name="next"),
    path('rewrite/<int:diary_id>', diaryapp.views.rewrite, name='rewrite'),
    path('remove/<int:diary_id>', diaryapp.views.remove, name='remove'),
    path('delete/<int:album_id>', albumapp.views.delete, name='delete'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)