from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, Template
from artSite.models import Gallery, Art, Project, About

def ArtListItems(object):
    if not object.description:
        object.description = "No words to be said"
    items = (object.title, object.id, object.image_res, object.image, object.description)
    return items

class ArtLists():
    
    def allGalleries(self):
        """ Get all the galleries for the main page """
        sortedGalleryList=[] 
        for gallery in Gallery.objects.all().order_by('id').reverse(): 
            sortedGalleryList.append((gallery.title, gallery.id, gallery.image_res, gallery.image)) 
        return sortedGalleryList
    
    def artsInGallery(self, id):
        """ Get all the pieces of art in the Gallery """
        artList=[]
        for art in Art.objects.filter(gallery__id__exact = id).order_by('id'):
            artList.append(ArtListItems(art))
            
        return artList
    
    def projectsInGallery(self, galleryid):
        """" Get page of projects in the gallery """
        projectsInGallery = Project.objects.filter(gallery__id__exact = galleryid)
        projectList = []
        for projects in projectsInGallery:
            projectList.append((projects.title, projects.id, projects.image))
        return projectList
            
    def allArts(self):
        """ Get all art for gallery"""        
        artList = []
        for art in Art.objects.all().order_by('id'):
            artList.append(ArtListItems(art))
        return artList
    
    def artsInProject(self, projectid):
        """ Get page of art in the project """        
        artInProject = Art.objects.filter(project__id__exact = projectid)
        artList = []
        for art in artInProject:
            artList.append(ArtListItems(art))
        return artList
    
    def allProjects(self):
        """ Get all Projects """
        allProjectsList = []
        for projects in Project.objects.all().order_by('id'):
            allProjectsList.append((projects.title, projects.id, projects.image))
        return allProjectsList
    
    def aboutSections(self):
        """ Get all About pages """
        allAboutList = []
        for about in About.objects.all().order_by('id'):
            allAboutList.append((about.title, about.id, about.image, about.body))
        return allAboutList
    
    def artMoreInfo(self, artId):
        try:
            art = Art.objects.get(id=artId)   
        except (ValueError, Art.DoesNotExist):
            return 'No matching description found!'
        return art.more_info_html
        
        
def ProjectsPage(request):
    """ Page to show all projects """
    context = RequestContext(request)
    artClass = ArtLists()
    projectsList = artClass.allProjects()
    
    if request.method == 'GET':
        return render_to_response('index.html', {'items':projectsList}, context )

def GalleriesPage(request):
    """ This is the main page (set in urls.py) - page shows all galleries"""
    context = RequestContext(request)
    artClass = ArtLists()
    projectsList = artClass.allGalleries()
    
    if request.method == 'GET':
        return render_to_response('gallery.html', {'items':projectsList}, context)
    
def ArtsInProject(request, id):
    context = RequestContext(request)
    artClass = ArtLists()
    artsList = artClass.artsInProject(id)
    
    if request.method == 'GET':
        return render_to_response('project.html',{'items':artsList}, context)
    
def ArtInGallery(request, id):
    context = RequestContext(request)
    artClass = ArtLists()
    projectsList = artClass.artsInGallery(id)
    
    if request.method == 'GET':
        return render_to_response('project.html', {'items':projectsList}, context)
    
def AllArt(request):
    context = RequestContext(request)
    artClass = ArtLists()
    artsList = artClass.allArts()
    
    if request.method == 'GET':
        return render_to_response('project.html', {'items':artsList}, context)
    
def AboutView(request):
    context = RequestContext(request)
    artClass = ArtLists()
    aboutList = artClass.aboutSections()
    
    if request.method == 'GET':
        return render_to_response('about.html', {'items':aboutList}, context)
    
def ArtModalView(request, id):
    context = RequestContext(request)
    artClass = ArtLists()
    Modal = artClass.artMoreInfo(id)
    
    if request.method == 'GET':
        return HttpResponse(Modal, content_type='text/html')
    