from django.contrib import admin
from .models import User
from .models import Item
from .models import Tag
from .models import Item_Tag
from .models import Chat
from .models import Matching
from .models import review
# Register your models here.
admin.site.register(User)
admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Item_Tag)
admin.site.register(Chat)
admin.site.register(Matching)
admin.site.register(review)

