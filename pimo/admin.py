from django.contrib import admin

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