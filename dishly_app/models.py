from django.db import models




CATEGORY = (
   ('A', 'Arabi'),
   ('S', 'Shawerma'),
   ('B', 'Burgers'),
   ('D', 'Deserts'),
   ('I', 'Ice Cream')
)


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    ingeredients = models.TextField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add=True)
    
    cate = models.CharField(max_length=1, 
                            choices = CATEGORY,
                            default=CATEGORY[0][0]
                            )
    
    
    def __str__(self):
        return self.name
    
    



