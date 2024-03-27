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




