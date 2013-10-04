# coding: utf-8

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from allPowerful import settings

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


#class UserInfoManager(BaseUserManager):
#    def create_user(self, email, username=None, password=None, **extra_fields):
#        """
#        通过Email, 创建并且保存一个用户
#        """
#        if not email:
#            raise ValueError(u'用户必须输入一个邮箱地址') # Users must have an email address
#        user = self.model(
#            email=self.normalize_email(email),
#            username=username,
#            **extra_fields
#        )
#        user.set_password(password)
#        user.save(using=self._db)
#        return user
#
#    def create_superuser(self, username, email, password, **extra_fields):
#        """
#        通过Email, 创建并且保存一个超级用户
#        """
#        user = self.create_user(email, username=username, password=password, **extra_fields)
#        user.is_admin = True
#        user.save(using=self._db)
#        return user
#
#class UserInfo(AbstractBaseUser):
#    """
#        这是用户模型表
#    """
#    MARITAL_STATUS = (
#        (0, u"未婚"),
#        (1, u"已婚"),
#        (2, u"离异")
#    )
#
#    GENDER = (
#        (0, u'男'),
#        (1, u'女'),
#    )
#
#    username = models.CharField(_(u'用户名'), max_length=30, unique=True,
#        help_text=_('Required. 30 characters or fewer. Letters, numbers and '
#                    '@/./+/-/_ characters'))
##    password = models.CharField(_(u'密码'), max_length=128)
#    email = models.EmailField(_(u'邮箱'), unique=True)
#    nickname = models.CharField(_(u'昵称'), max_length=100, default="")
#    date_joined = models.DateTimeField(_(u'加入时间'), default=timezone.now)
#    #我在考虑是存储在数据库里,还是放到类似S3的地方,来存储图片。
#    avatar = models.TextField(_(u'头像'), default="")
#    #这里为什么用integer类型,减少数据库存储量。本来是需要存储字符串的, 现在只需要存储int类型。
#    marital_status = models.IntegerField(_(u'婚姻状况'), choices=MARITAL_STATUS, default=0)
#    company = models.CharField(_(u'公司'), blank=True, null=True, max_length=255)
#    city    = models.CharField(_(u'现工作地'), blank=True, null=True, max_length=255)
#    is_admin  = models.BooleanField(_(u'是否是管理员'), default=False)
#    is_active = models.BooleanField(_(u'是否是激活状态'), default=False)
#    is_online = models.BooleanField(_(u'是否在线'), default=False)
#    expert_in = models.CharField(_(u'擅长领域'), max_length=255, default='')
#    gender    = models.IntegerField(_(u'性别'), max_length=2, choices=GENDER, default=0)
#    birthday  = models.CharField(_(u'生日'), max_length=16, null=True, blank=True)
#    industry  = models.CharField(_(u'行业'), max_length=50, null=True, blank=True)
#
#    objects = UserInfoManager()
#
#    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = ['username']
#
#    def get_full_name(self):
#    # The user is identified by their email address
#        return self.email
#
#    def get_short_name(self):
#        # The user is identified by their email address
#        return self.email
#
#    # On Python 3: def __str__(self):
#    def __unicode__(self):
#        return self.email
#
#    def has_perm(self, perm, obj=None):
#        return True
#
#    def has_module_perms(self, app_label):
#        return True
#
#    @property
#    def is_staff(self):
#        return self.is_admin

class UserProfile(BaseModel):
    """
        这是用户模型表
    """
    MARITAL_STATUS = (
        (0, u"未婚"),
        (1, u"已婚"),
        (2, u"离异")
    )

    GENDER = (
        (0, u'男'),
        (1, u'女'),
    )

    user = models.OneToOneField(User)
    nickname = models.CharField(_(u'昵称'), max_length=100, default="")
    date_joined = models.DateTimeField(_(u'加入时间'), default=timezone.now)
    #我在考虑是存储在数据库里,还是放到类似S3的地方,来存储图片。
    avatar = models.TextField(_(u'头像'), default="")
    #这里为什么用integer类型,减少数据库存储量。本来是需要存储字符串的, 现在只需要存储int类型。
    marital_status = models.IntegerField(_(u'婚姻状况'), choices=MARITAL_STATUS, default=0)
    company = models.CharField(_(u'公司'), blank=True, null=True, max_length=255)
    city    = models.CharField(_(u'现工作地'), blank=True, null=True, max_length=255)
    is_admin  = models.BooleanField(_(u'是否是管理员'), default=False)
    is_active = models.BooleanField(_(u'是否是激活状态'), default=False)
    is_online = models.BooleanField(_(u'是否在线'), default=False)
    expert_in = models.CharField(_(u'擅长领域'), max_length=255, default='')
    gender    = models.IntegerField(_(u'性别'), max_length=2, choices=GENDER, default=0)
    birthday  = models.CharField(_(u'生日'), max_length=16, null=True, blank=True)
    industry  = models.CharField(_(u'行业'), max_length=50, null=True, blank=True)
    tel_number = models.IntegerField(_(u'电话号码'))

class Friends(BaseModel):
    """
    用户和用户之间的朋友关系 我想了很久,想了3个解决方案。
    1.加一个字段friends在UserInfo表里, 里面是一个UserInfo id 的列表集合.类似这个样子:[1,2,3,4,5,6], 好处可以速度的取出好友的列表集合
    2.创建一个多对多的关系表. 里面我又分成了2个想法:
        1).查询的方便,但是会有数据冗余, 互相成为好友的时候,需要加入2条数据。
           用户-1 -- 用户-2 -- 备注
           用户-1 -- 用户-3 -- 备注
           用户-1 -- 用户-4 -- 备注
           用户-2 -- 用户-1 -- 备注
           用户-3 -- 用户-1 -- 备注
           用户-4 -- 用户-1 -- 备注
        2).减少数据冗余,查询相对麻烦一点
           用户-1 -- 用户-2 -- 用户备注-1 -- 用户备注-2
           用户-2 -- 用户-3 -- 用户备注-2 -- 用户备注-3
           用户-4 -- 用户-3 -- 用户备注-4 -- 用户备注-3
    3.使用no-sql.
    根据现有需求的话.我最终决定使用稍微清晰点的设计方案, 第2个想法的第一个解决方案。
    """
#    user   = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_set')
#    friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friends_set')
#    remark = models.CharField(_(u'备注'), blank=True, null=True, max_length=255)

    pass

###############################################
#From this, I will use these model to create breakfast project.
class Item(BaseModel):
    """
        items table.
    """
    TYPE = (
        (0, u"水果"),
        (1, u"早餐")
        )
    name        = models.CharField(_(u'物品名字'), max_length=255)
    type        = models.IntegerField(_(u'物品类型'), choices=TYPE, default=0)
    price       = models.FloatField(_(u'物品价格'), default=0.0)
    description = models.TextField(_(u'物品描述'), null=True, blank=True, default="")
    image       = models.TextField(_(u'物品图片'))

class UserAddress(BaseModel):
    """
        这个模型是用来记录 用户的常用配送地址
    """
    user           = models.ForeignKey(User, null=True, blank=True)
    user_address   = models.TextField()
    recipient_name = models.CharField(max_length=256)
    tel_number     = models.IntegerField()
    comment        = models.TextField(default="")


class Order(BaseModel):
    """
        用户的订单表
    """
    order_id         = models.IntegerField(_(u'订单号'))
    item_quantity    = models.IntegerField(_(u'物品数量'), default=1)
    item             = models.ForeignKey(Item)
    user             = models.ForeignKey(User)
    is_send          = models.BooleanField(_(u'是否已送到'), default=False)
    comment          = models.TextField(default="")
    price            = models.FloatField(_(u'当次配送物品金额'), default=0.0)
    dispatching_cost = models.FloatField(_(u"配送费用"), default=0.0)
    user_address     = models.ForeignKey(UserAddress)


