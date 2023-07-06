from typing import Any
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')
    exclude = ['_autor']

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'
    
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any):
        obj.autor = request.user
        super().save_model(request, obj, form, change)
