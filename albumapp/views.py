from django.shortcuts import render, get_object_or_404, redirect
from .models import Album

# Create your views here.

def album(request):
    if request.method=="POST":
        form=Album()
        form.title=request.POST['title']
        try:
            form.image=request.FILES['image']
        except:
            pass
        form.save()
    album=Album.objects.all().order_by('-id')
    return render(request, 'album.html', {'album':album})

def delete(request, album_id):
    album=get_object_or_404 (Album, pk=album_id)
    album.delete()
    return redirect('/album/')