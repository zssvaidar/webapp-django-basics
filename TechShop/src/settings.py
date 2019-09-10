import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'h9ke%p0mgoo5d_vh2tfkgm*24f@2&!!f-q5n**k$5_or!k&2g^'
DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = 'src.urls'
WSGI_APPLICATION = 'src.wsgi.application'

INSTALLED_APPS = [
    'src.bone',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['src/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
import pymysql  # noqa: 402
pymysql.install_as_MySQLdb()
if os.getenv('GAE_APPLICATION', None):
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/arctic-signer-220812:asia-northeast1:gcloudtest27-10-19',#/cloudsql/[YOUR-CONNECTION-NAME]tensile-cogency-220620:asia-northeast1:gcloudtest27-10-18
            'USER': 'root',
            'PASSWORD': 'aa18aa01',
            'NAME': 'invoice_db',
		}
	}
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': 'invoice_db',
			'USER': 'root',
			'PASSWORD': 'aa18aa01',
			'HOST': '127.0.0.1',
			'PORT': ''
		}
	}

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa: 501
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa: 501
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa: 501
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa: 501
#     },
# ]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "src/static")]
STATIC_ROOT = os.path.join(BASE_DIR,"src/static/static_cdn")
LOGIN_REDIRECT_URL = '/'
