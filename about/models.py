from django.db import models

# Model for Mission
class Mission(models.Model): 
    title = models.TextField(max_length=1000)

    def __str__(self):
        return self.title




