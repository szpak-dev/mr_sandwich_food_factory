import os

import django.http.request
from django.utils.regex_helper import _lazy_re_compile
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.http.request.host_validation_re = _lazy_re_compile(r"[a-zA-z0-9.:]*")

app = get_wsgi_application()
