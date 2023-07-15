from django.contrib import admin
from .models import ContactModel, ContactLink, About, Social, ImageAbout



class ImageAboutInline(admin.StackedInline):
    model = ImageAbout
    extra = 1



@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'create_at']#оочередность вывода в админке
    list_display_links = ('name',)#переход на более подробную запись нажимая на 'name'



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ImageAboutInline]#одключить с админки фотки






admin.site.register(ContactLink)
admin.site.register(Social)






