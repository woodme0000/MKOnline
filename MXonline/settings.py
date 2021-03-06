# -*- encoding:utf-8 -*-
"""
Django settings for MXonline project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 因为我们自己建立了apps，所以我们需要使用sys.path.insert将我们的app目录插入到系统目录
# 第一个参数是搜索位置，第二个参数是使用Base_DIR和app拼成一个路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(1, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&=*@e5b$(fs96-nm&ri0m2nmky69!awlxiq$j&-i(q2_e&lsx8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'courses',
    'operation',
    'organization',
    'xadmin',
    'crispy_forms',
    'captcha',
    'pure_pagination',
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

ROOT_URLCONF = 'MXonline.urls'
# 重写用户模型
AUTH_USER_MODEL = 'users.UserProfile'
# 重写自定义用户认证后台
AUTHENTICATION_BACKENDS = (
    ('users.views.CustomBackend'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 添加这个用于处理在html里面处理 {{MEDIA_URL}}
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'MXonline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mxonline',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'
#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 配置文件上传的默认根路径，需要在setting里面加入如下配置文件
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Media Root 如果使用FileField 和ImageField
#在你的settings文件中, 你必须要定义 MEDIA_ROOT 作为Django存储上传文件的路径
# (从性能上考虑，这些文件不能存在数据库中。) 定义一个 MEDIA_URL 作为基础的URL或者目录。
# 确保这个目录可以被web server使用的账户写入。
#在模型中添加FileField 或 ImageField 字段, 定义 upload_to参数，内容是 MEDIA_ROOT 的子目录，
# 用来存放上传的文件。
#数据库中存放的仅是这个文件的路径 （相对于MEDIA_ROOT). 你很可能会想用由Django提供的便利的url
# 属性。比如说, 如果你的ImageField 命名为 mug_shot, 你可以在template中用 {{ object.mug_shot.url }}
# 获得你照片的绝对路径。
#例如，如果你的 MEDIA_ROOT设定为 '/home/media'，并且 upload_to设定为 'photos/%Y/%m/%d'。
#  upload_to的'%Y/%m/%d'被strftime()所格式化；'%Y' 将会被格式化为一个四位数的年份, '%m'
# 被格式化为一个两位数的月份'%d'是两位数日份。如果你在Jan.15.2007上传了一个文件，它将被保存
# 在/home/media/photos/2007/01/15目录下.


# 配置邮件附送服务器
EMAIL_HOST = 'smtp.aliyun.com'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'luojingen@aliyun.com'
EMAIL_HOST_PASSWORD = 'luo1380126'
EMAIL_USE_TLS = False
EMAIL_FROM = 'luojingen@aliyun.com'
