from django.shortcuts import render, redirect
from .models import Diary, Comment
from .forms import DiaryForm, CommentForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    comment_form = CommentForm()
    context = {
        'diaries': diaries,
        'comment_form': comment_form,
    }

    for diary in diaries:
        diary.comments = Comment.objects.filter(diary=diary)
    return render(request, 'diaries/index.html', context)


def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

def comments_create(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.diary = diary
            comment.save()
            return redirect('diaries:index')
        
def comments_delete(request, comment_pk):
    # 뷰 코드 내용은 그대로 유지됩니다.
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('diaries:index')