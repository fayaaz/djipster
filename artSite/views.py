from django.shortcuts import render_to_response
from django.template import RequestContext, Template
from artSite.models import Gallery, Art, Project, About


class ListsDef():
    
    def allGalleries(self):
        """ Get all the galleries for the main page """
        sortedGalleryList=[] 
        for gallery in Gallery.objects.all().order_by('id'): 
            sortedGalleryList.append((gallery.title, gallery.id, gallery.image)) 
        return sortedGalleryList
    
    def artsInGallery(self, id):
        
        sortedArtsList=[]
        for art in Art.objects.filter(gallery__id__exact = id).order_by('id'):
            sortedArtsList.append((art.title, art.id, art.image))
            
        return sortedArtsList
    
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
            artList.append((art.title, art.id, art.image))
        return artList
    
    def artsInProject(self, projectid):
        """ Get page of art in the project """        
        artInProject = Art.objects.filter(project__id__exact = projectid)
        artList = []
        for art in artInProject:
            artList.append((art.title, art.id, art.image))
        return artList
    
    def allProjects(self):
        """ Get all Projects - this is the main view """
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
        
def ProjectsPage(request):
    context = RequestContext(request)
    artClass = ListsDef()
    projectsList = artClass.allProjects()
    
    if request.method == 'GET':
        return render_to_response('index.html', {'items':projectsList}, context )

def GalleriesPage(request):
    context = RequestContext(request)
    artClass = ListsDef()
    projectsList = artClass.allGalleries()
    
    if request.method == 'GET':
        return render_to_response('gallery.html', {'items':projectsList}, context)
    
def ArtsInProject(request, id):
    context = RequestContext(request)
    artClass = ListsDef()
    artsList = artClass.artsInProject(id)
    
    if request.method == 'GET':
        return render_to_response('project.html',{'items':artsList}, context)
    
def ArtInGallery(request, id):
    context = RequestContext(request)
    artClass = ListsDef()
    projectsList = artClass.artsInGallery(id)
    
    if request.method == 'GET':
        return render_to_response('project.html', {'items':projectsList}, context)
    
def AllArt(request):
    context = RequestContext(request)
    artClass = ListsDef()
    artsList = artClass.allArts()
    
    if request.method == 'GET':
        return render_to_response('project.html', {'items':artsList}, context)
    
def AboutView(request):
    context = RequestContext(request)
    artClass = ListsDef()
    aboutList = artClass.aboutSections()
    
    if request.method == 'GET':
        return render_to_response('about.html', {'items':aboutList}, context)
    