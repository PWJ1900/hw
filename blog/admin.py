from django.contrib import admin

# Register your models here.

from .models import Article
admin.site.register(Article)
from .models import index_slider
admin.site.register(index_slider)
from .models import index_introduction
admin.site.register(index_introduction)
from .models import index_people
admin.site.register(index_people)
from .models import Achievementss
admin.site.register(Achievementss)
from .models import people
admin.site.register(people)
from .models import people_detail_simple
admin.site.register(people_detail_simple)
from .models import people_education
admin.site.register(people_education)
from .models import Peradminuse
admin.site.register(Peradminuse)
from .models import Achievementss_project
admin.site.register(Achievementss_project)
