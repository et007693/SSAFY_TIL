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