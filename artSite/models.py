from django.db import models
from time import sleep
from markdown import markdown
from django.core.exceptions import ValidationError
from django.dispatch import Signal
from imagefuncs import imgResize, imgRename

def validate_only_one_instance(obj):
    ''' Used for making sure only one entry exists on a model. For example the title of the site '''
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)

# Create your models here.

class MainPicture(models.Model):

    image = models.FileField(upload_to = 'upload/main')
    
    def clean(self):
        validate_only_one_instance(self)

    def __unicode__(self):
        return str(self.image)
    
class Title(models.Model):
    '''Title of the site: only allows one entry'''    
    title = models.CharField(max_length=255)
    
    def clean(self):
        validate_only_one_instance(self)

    def __unicode__(self):
        return self.title
    
class Gallery(models.Model):
    '''A gallery for projects and art pieces'''
    upload_folder = 'upload/gallery'
    
    title = models.CharField(max_length=20)
    image = models.FileField(upload_to = upload_folder)
    image_res = models.FileField(default = 'notResized', upload_to = upload_folder, blank = True, null = True, editable = False)

    def save(self):
        self.image_res = self.upload_folder+'/'+str(imgRename(str(self.image)))
        super(Gallery, self).save()
        
        resizeTry('media/'+str(self.image))
    
    def __unicode__(self):
        return self.title
    
class Project(models.Model):
    '''A project is a group of art pieces linked somehow'''
    
    upload_folder = 'upload/project'
    
    title = models.CharField(max_length=20)
    gallery = models.ForeignKey('Gallery', null = True, blank = True)
    image = models.FileField(upload_to = upload_folder)
    image_res = models.FileField(default = 'notResized', upload_to = upload_folder, blank = True, null = True, editable = False)
    
    
    def save(self):
        self.image_res = self.upload_folder+'/'+str(imgRename(str(self.image)))
        super(Project, self).save()
        
        resizeTry('media/'+str(self.image))
            
    
    def __unicode__(self):
        return self.title
    
class Art(models.Model):
    '''Each art piece. Has to be in a gallery and project'''

    upload_folder = 'upload/art'
    
    title = models.CharField(max_length=50)
    project = models.ForeignKey('Project',  null = True, blank = True)
    gallery = models.ForeignKey('Gallery',  null = True, blank = True)
    image = models.FileField(upload_to = upload_folder)
    image_res = models.FileField(default = 'notResized', upload_to = upload_folder, blank = True, null = True, editable = False)
    
    def save(self):
        self.image_res = self.upload_folder+'/'+str(imgRename(str(self.image)))
        super(Art, self).save()
        
        resizeTry('media/'+str(self.image))

    def __unicode__(self):
        return self.title
    
class About(models.Model):
    '''Each section in About. To be written in Markdown (body_markdown field) to allow editing in CMS.'''
    title = models.CharField(max_length=50)
    body_markdown = models.TextField('Entry Body', help_text='Write in Markdown! <a href=\'https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet/\'  target=\'_blank\'>Help</a>', blank=True)
    body = models.TextField('Entry HTML', help_text='HTML from markdown', blank=True)
    image = models.FileField(upload_to = 'upload/about', blank=True)
    
    def __unicode__(self):
        return self.title
    
    def save(self):
        '''Save the markdown to HTML'''
        self.body = markdown(self.body_markdown)
        super(About, self).save() # Call the "real" save() method.
        
def resizeTry(image):
    
    try:
        imgResize(image, 1024)
    except IOError:
        sleep(0.1)
        resizeTry(image)