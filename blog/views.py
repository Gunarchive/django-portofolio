from multiprocessing import context
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def index(request):
    db = Post.objects.all()
    context = {
        'Judul' : 'data guna',
        'about' : 'About Me',
        'Nama' : 'Guna Dharma',
        'NPM' : '1204071',
        'Asal' : 'sumatra Barat',
        'Email' : 'gunadharma201@gmail.com',
        'HP' : '089516370731',
        'Umur' : '21',
        'Desc' : 'Mahasiswa',
        'title' : 'Blog',
        'heading' : 'Blog',
        'subheading' : 'Postingan',
        'post' : db,

        'detail' : 'Hai guyus kenalin nama saya guna dharma saya berasal dari sumatra barat, pak punten banget saya ngk liat deadline kirain saya sampai minggu depan ternyata kemaren, sorry banget pak, mudah"an punya saya diterima ya pak kwkwkkw, sehat selalu pak trus kapan kita valo nih pak wkkwkwk'
    }
    return render(request, 'blog/index.html', context)

def recent(request):
    return HttpResponse("RECENT BLOG")
    #context = {
    #    'Judul' : 'blog2',
    #    'h1' : 'Python'
    #}
    #return render(request, 'blog/index.html', context)
# Create your views here
