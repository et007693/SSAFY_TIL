# 가상환경
python -m venv venv
source venv/Scripts/activate
pip freeze > requirements.txt

# Django 프로젝트 생성
django-admin startproject name .

# Django app 생성
python manage.py startapp name -> 앱 등록(settings.py)

# 서버 실행
python manage.py runserver

# Migrations 핵심 명령어
1. python manage.py makemigrations
2. python manage.py migrate

# admin
1. python manage.py createsuperuser

2. admin.py -> admin.site.register(class)

# ORM
pip install ipython
pip install django-extensions

python manage.py shell_plus

## 전체 데이터 조회
model.objects.all()
## 특정 조건 데이터 조회
model.object.filter(attribute = 'name')

# 수정, 삭제는 데이터를 할당(todo = Todo()) 후 삭제

# satic 추가 경로 설정(setting.py)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# MEDIA_ROOT 설정
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

### urls.py
from django.conf import settings
from django.conf.ursl.static import static

urlspatterns = [
    
] + static(setting.MEDIA_URL, document_root = settigs.MEDIA_ROOT)


query 예시
https://wayhome25.github.io/django/2017/04/01/django-ep9-crud/

# serializer views.py
```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
```

# serializer serializers.py
```python
from rest_framework import serializers
```