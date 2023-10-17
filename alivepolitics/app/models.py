from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    STATUS = (
        ('0','Draft'),
        ('1','Publish'),
    )
    SECTION = (
        #('Main', 'Main'),
        ('Popular','Popular'),
        ('Recent','Recent'),
        ('Editors_pick','Editors_pick'),
        ('Trending','Trending'),
        ('Inspiration','Inspiration'),
        ('Latest_Posts','Latest_Posts'),
    )
    featured_image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = RichTextField()
    slug = models.SlugField(max_length=200, null=True, blank=True,unique=True)
    status = models.CharField(choices=STATUS,max_length=100)
    section = models.CharField(choices=SECTION,max_length=100)
    main_post = models.BooleanField(default=False)
    
    # def get_absolute_url(self):
    #     kwargs = {
    #         'pk': self.id,
    #         'slug': self.slug
    #     }
    #     return reverse('post-detail', kwargs=kwargs)
    
    # def save(self, *args, **kwargs):
    #     value = self.title
    #     self.slug = slugify(value, allow_unicode=True)
    #     super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_details", kwargs={'slug': self.slug})

    
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Post)

    
    
    

       
# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#     pre_save.connect(pre_save_post_receiver, Post)



class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)   