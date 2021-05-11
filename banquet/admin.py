from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Customer, Music, Food, Banquet, Comment, FoodCategory
from django.utils.translation import ugettext_lazy

admin.site.register(Banquet)
admin.site.register(Customer)
admin.site.register(Music)
admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(Comment)
AdminSite.site_title = ugettext_lazy('My Admin')