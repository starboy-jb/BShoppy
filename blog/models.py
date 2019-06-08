from django.db import models

# Create your models here.

class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 100)
    head0 = models.CharField(max_length = 300, default='')
    chead0 = models.CharField(max_length = 3000, default='')
    head1 = models.CharField(max_length = 300, default='')
    chead1 = models.CharField(max_length = 3000, default='')
    head2 = models.CharField(max_length = 300, default='')
    chead2 = models.CharField(max_length = 3000, default='')
    pub_date = models.DateField(default='')
    thumbnail = models.ImageField(upload_to = 'blog/images', default = '')

    def __str__(self):
        return self.title