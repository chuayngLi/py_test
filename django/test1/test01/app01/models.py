# 数据库模型
from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=18, null=True, blank=True)  # 第一个为默认值 23个为允许为空
