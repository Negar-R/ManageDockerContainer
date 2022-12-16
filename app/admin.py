from django.contrib import admin

from .models import App, AppContainerHistory

# Register your models here.

admin.site.register(App)
admin.site.register(AppContainerHistory)
