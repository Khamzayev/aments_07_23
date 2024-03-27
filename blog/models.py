from django.db import models
from blog.abstract import ActiveModel, OrderModel, BaseModel
from django.utils.translation import gettext_lazy as _




class Author(BaseModel):
    full_name = models.CharField(max_length=100, verbose_name=_("full_name"))
    image = models.ImageField(upload_to='media/blog/author/%Y/%m/%d')

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")




class BlogFullWidth(BaseModel):
    title = models.CharField(max_length=100, help_text=_("write title"), verbose_name=_("title"))
    author = models.CharField(max_length=30, help_text=_("write author name"), verbose_name=_("author"))
    image = models.ImageField(upload_to='media/blog/post/%Y/%m/%d', verbose_name=_("image"))

    def __str__(self) -> str:
        return f"{self.title}, {self.author}"
    
    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

        
