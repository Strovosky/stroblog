from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Posts(Model):
    title = CharField(max_length=150)
    content = TextField(max_length=500)
    date_created = DateTimeField(auto_now_add=True) # This won't ever be modified.
    last_modified = DateTimeField(auto_now=True) # This can be updated.
    author = ForeignKey(to=User, on_delete=CASCADE)

    def __str__(self) -> str:
        return f"Post: {self.title}"