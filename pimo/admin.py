from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from pimo.models import User

from .models import Order
from .models import Post
from .models import Offer
from .models import Grade
from .models import User

admin.site.register(Order)
admin.site.register(Post)
admin.site.register(Offer)
admin.site.register(User)
admin.site.register(Grade)
admin.site.register(User, UserAdmin)
