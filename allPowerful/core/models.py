# coding: utf-8

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail

class BaseModel(models.Model):
    """
        这是基类模型, 包含创建时间和更新时间
    """
    updated_at = models.DateTimeField(_(u'更新时间'), auto_now=True)
    created_at = models.DateTimeField(_(u'创建时间'), auto_now_add=True)

    class Meta:
        abstract = True

class UserInfo(BaseModel):
    """
        这是用户模型表
    """
    MARITAL_STATUS = (
        (0, u"未婚"),
        (1, u"已婚"),
        (2, u"离异")
    )

    username = models.CharField(_(u'用户名'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters'))
    password = models.CharField(_(u'密码'), max_length=128)
    email = models.EmailField(_(u'邮箱'), unique=True)
    nickname = models.CharField(_(u'昵称'))
    last_login = models.DateTimeField(_(u'最后登陆时间'), default=timezone.now)
    date_joined = models.DateTimeField(_(u'加入时间'), default=timezone.now)
    #我在考虑是存储在数据库里,还是放到类似S3的地方,来存储图片。
    avatar = models.TextField(_(u"头像"), default="")
    #这里为什么用integer类型,减少数据库存储量。本来是需要存储字符串的, 现在只需要存储int类型。
    marital_status = models.IntegerField(_(u"婚姻状况"), choices=MARITAL_STATUS, default=0)
