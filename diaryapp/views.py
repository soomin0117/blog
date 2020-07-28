from django.shortcuts import render, get_object_or_404, redirect
from .models import Diary
from django.utils import timezone

# Create your views here.

def diary(request):
    diary=Diary.objects.all().order_by('-id')
    return render(request, 'diary.html', {'diary': diary})

def detail(request, diary_id):
    diary=get_object_or_404 (Diary, pk=diary_id)
    if Diary.objects.first().id==diary.id:
        diary_order=0
    elif Diary.objects.last().id==diary.id:
        diary_order=2
    else:
        diary_order=1
    return render(request, 'detail.html', {'diary_detail':diary, "diary_order":diary_order})

def write(request):
    if request.method=='POST':
        diary=Diary()
        diary.title=request.POST['title']
        diary.body=request.POST['body']
        diary.pub_date= timezone.datetime.now()
        diary.save()
        return redirect('/diary/')
    else:
        return render(request, 'write.html')    

def prev(request, diary_id):
    prev_diary=diary_id-1
    previous=Diary.objects.get(pk=diary_id)
    while 1:
        try:
            previous=Diary.objects.get(pk=prev_diary)
        except:
            prev_diary=prev_diary-1
        if previous.id != diary_id:
            break
    return redirect('/detail/'+str(prev_diary))

def next(request, diary_id):
    next_diary=diary_id+1
    next=Diary.objects.get(pk=diary_id)
    while 1:
        try:
            next=Diary.objects.get(pk=next_diary)
        except:
            next_diary=next_diary+1
        if next.id != diary_id:
            break
    return redirect('/detail/'+str(next_diary))    

def rewrite(request, diary_id):
    if request.method=='POST':
        diary=get_object_or_404 (Diary, pk=diary_id)
        diary.title=request.POST['title']
        diary.body=request.POST['body']
        diary.pub_date= timezone.datetime.now()
        diary.save()
        return redirect('/detail/'+str(diary.id))
    else:
        diary=get_object_or_404 (Diary, pk=diary_id)
        return render(request, 'rewrite.html', {'diary':diary})

def remove(request, diary_id):
    diary=get_object_or_404 (Diary, pk=diary_id)
    diary.delete()
    return redirect('/diary/')