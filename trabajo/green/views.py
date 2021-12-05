from django.shortcuts import render
from .models import Post
from green.form import PostForm
from .models import Post

def home(request):
    data = Post.objects.all()
    return render(request, "home.html", {"posts": data})
#primero basico
def m1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/Matematicas.html", {"posts": data})
def l1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/Lenguaje.html", {"posts": data})
def c1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/ciencias.html", {"posts": data})
def h1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/Historia.html", {"posts": data})
def i1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/ingles.html", {"posts": data})
def o1(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/primero_basico/otros.html", {"posts": data})


#segundo basico


def m2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/Matematicas.html", {"posts": data})
def l2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/Lenguaje.html", {"posts": data})
def c2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/ciencias.html", {"posts": data})
def h2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/Historia.html", {"posts": data})
def i2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/ingles.html", {"posts": data})
def o2(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/segundo basico/otros.html", {"posts": data})
#tercero basico


def m3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/Matematicas.html", {"posts": data})
def l3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/Lenguaje.html", {"posts": data})
def c3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/ciencias.html", {"posts": data})
def h3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/Historia.html", {"posts": data})
def i3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/ingles.html", {"posts": data})
def o3(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/tercero basico/otros.html", {"posts": data})

#cuarto basico

def m4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/Matematicas.html", {"posts": data})
def l4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/Lenguaje.html", {"posts": data})
def c4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/ciencias.html", {"posts": data})
def h4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/Historia.html", {"posts": data})
def i4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/ingles.html", {"posts": data})
def o4(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/cuarto basico/otros.html", {"posts": data})

#cuarto basico

def m5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/Matematicas.html", {"posts": data})
def l5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/Lenguaje.html", {"posts": data})
def c5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/ciencias.html", {"posts": data})
def h5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/Historia.html", {"posts": data})
def i5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/ingles.html", {"posts": data})
def o5(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/quinto basico/otros.html", {"posts": data})

#sexto basico

def m6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/Matematicas.html", {"posts": data})
def l6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/Lenguaje.html", {"posts": data})
def c6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/ciencias.html", {"posts": data})
def h6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/Historia.html", {"posts": data})
def i6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/ingles.html", {"posts": data})
def o6(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/sexto basico/otros.html", {"posts": data})

#septimo basico

def m7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/Matematicas.html", {"posts": data})
def l7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/Lenguaje.html", {"posts": data})
def c7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/ciencias.html", {"posts": data})
def h7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/Historia.html", {"posts": data})
def i7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/ingles.html", {"posts": data})
def o7(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/septimo basico/otros.html", {"posts": data})

#octavo basico

def m8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/Matematicas.html", {"posts": data})
def l8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/Lenguaje.html", {"posts": data})
def c8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/ciencias.html", {"posts": data})
def h8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/Historia.html", {"posts": data})
def i8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/ingles.html", {"posts": data})
def o8(request):
    data = Post.objects.all()
    return render(request, "grados/Basica/octavo basico/otros.html", {"posts": data})


def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        print(request.POST)
    
    return render(request, 'post/posteos.html', {"form": form})