from planetpost.models import Planet_Comments, Planet_Post
from django.contrib import admin
from planetpost.models import Planet_Post

# Register your models here.
admin.site.register(Planet_Post)
admin.site.register(Planet_Comments)