#music-api setup

### Dev environment setup:
```bash
#in project directory:
virtualenv --python python3 envgrocer
source envgrocer/bin/activate
deactivate
```

### Django install:
```bash
#in virtualenv:
pip install Django==2.0.5
```

### Django validate and verify:
```bash
#in python3 shell
import django
django.get_version()
```

### Dependency management:
```bash
#pin depedencies in current project:
pip freeze > requirements.txt

#download dependencies when working in different environment:
pip install -r requirements.txt
```

### install drf
```bash
pip install djangorestframework
```

### create django project
```bash
django-admin.py startproject api .
```

### create django app
```bash
django-admin.py startapp music
```

### sync db
```bash
python manage.py migrate
```

### create user
```bash
python manage.py createsuperuser --email admin@example.com --username admin
```
