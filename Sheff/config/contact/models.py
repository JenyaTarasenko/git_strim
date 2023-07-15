from django.db import models
from ckeditor.fields import RichTextField


class ContactModel(models.Model):
    """"Класс модели обратной связи"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField()
    massage = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} - {self.email}'#выводит имя и эмеил


class ContactLink(models.Model):
    """"Класс модели контактов"""
    icon = models.FileField(upload_to="icons/")#для формата иконок
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name




class About(models.Model):
    text = RichTextField()
    mini_text = RichTextField()


    def get_first_images(self):
        item = self.about_images.first()#забираем картинку первую с адмирнки болшую
        return item.image.url

    def get_images(self):
        return self.about_images.order_by("id")[1:]#перебираем картинки маленькие через цикл


class ImageAbout(models.Model):
    image = models.ImageField(upload_to='about/')
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_images')
    alt = models.CharField(max_length=100)#для SEO



class Social(models.Model):
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)
    link = models.URLField()




