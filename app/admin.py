from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

# Register your models here.


User = get_user_model()
admin.site.register(User)  # Userモデルを登録
admin.site.unregister(Group)  # Groupモデルは不要のため非表示にします
