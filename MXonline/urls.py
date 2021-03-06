"""MXonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.views.static import serve
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetPwdView, \
    ModifyPwdView
from organization.views import CourseOrgView, Comments_Upload, CustomAddView, CustomAjaxView

import xadmin
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='my_index'),
    url(r'^login/$', LoginView.as_view(), name='my_login'),
    url(r'^register/$', RegisterView.as_view(), name='my_register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>\w*)/$', ActiveUserView.as_view(), name='my_active_user'),
    url(r'^forget_pwd/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<reset_code>\w*)/$', ResetPwdView.as_view(), name='reset_pwd'),
    url(r'modify_pwd/$', ModifyPwdView.as_view(), name='my_modify_pwd'),
    url(r'^org_list/$', CourseOrgView.as_view(), name='org-list'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # 这个项目里面的测试，尝试用ajax动态的提交内容到后台
    url(r'^comments_upload/$', Comments_Upload.as_view(), name='comments_upload'),
    url(r'^ajax/add/$', CustomAddView.as_view(), name='comments_add'),
    url(r'^ajax/$', CustomAjaxView.as_view(), name='ajax_add'),
]
