# coding: utf-8
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

__author__ = 'wadehuang'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100)

class UserForm(forms.Form):
    username = forms.CharField(max_length=100, error_messages={'required':u'用户名不能为空'}, label=u"用户名")
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100, error_messages={'required':u'密码不能为空'}, label=u"密码")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        #验证是否为空
        if username.strip() == "":
            raise ValidationError(u"用户名不能为空")
        #验证是否有同名
        user = User.objects.filter(username=username)
        if user:
            raise ValidationError(u'用户名已存在, 请重新输入')
        return self.cleaned_data['username']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        #验证是否为空
        if not password:
            raise ValidationError(u"密码不能为空")
        return self.cleaned_data['password']

    def save(self, *args, **kwargs):
        user = User()
        user.username = self.cleaned_data.get("username")
        user.set_password(self.cleaned_data.get("password"))
        user.save()

