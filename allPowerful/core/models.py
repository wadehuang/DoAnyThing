# coding: utf-8

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#   Use south migration tool to generate the migration script.
#   manage.py schemamigration core --auto

class BaseModel(models.Model):
    """
        这是基类模型, 包含创建时间和更新时间
    """
    updated_at = models.DateTimeField(_(u'更新时间'), auto_now=True)
    created_at = models.DateTimeField(_(u'创建时间'), auto_now_add=True)

    class Meta:
        abstract = True


class UserInfoManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        """
        通过Email, 创建并且保存一个用户
        """
        if not email:
            raise ValueError(u'用户必须输入一个邮箱地址') # Users must have an email address
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """
        通过Email, 创建并且保存一个超级用户
        """
        user = self.create_user(email, username=username, password=password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user

class UserInfo(AbstractBaseUser):
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
#    password = models.CharField(_(u'密码'), max_length=128)
    email = models.EmailField(_(u'邮箱'), unique=True)
    nickname = models.CharField(_(u'昵称'), max_length=100, default="")
    date_joined = models.DateTimeField(_(u'加入时间'), default=timezone.now)
    #我在考虑是存储在数据库里,还是放到类似S3的地方,来存储图片。
    avatar = models.TextField(_(u'头像'), default="")
    #这里为什么用integer类型,减少数据库存储量。本来是需要存储字符串的, 现在只需要存储int类型。
    marital_status = models.IntegerField(_(u'婚姻状况'), choices=MARITAL_STATUS, default=0)
    is_admin = models.BooleanField(_(u'是否是管理员'), default=False)
    is_active = models.BooleanField(_(u'是否是激活状态'), default=False)
    is_online = models.BooleanField(_(u'是否在线'), default=False)


    objects = UserInfoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
    # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
