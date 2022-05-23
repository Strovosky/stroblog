from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Posts(Model):
    title = CharField(max_length=150)
    content = TextField(max_length=500)
    date_created = DateTimeField(auto_now_add=True) # This won't ever be modified.
    last_modified = DateTimeField(auto_now=True) # This can be updated.
    author = ForeignKey(to=User, on_delete=CASCADE)

    def __str__(self) -> str:
        return f"Post: {self.title}"
    
    # This method will return the url of any instance of this class.
    def get_absolute_url(self):
        # Here we return (through reverse) the full path of where we wanna redirect.
        return reverse(viewname="detail-post", kwargs={"pk": self.pk})
