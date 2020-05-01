from django.shortcuts import render,redirect

# Create your views here.
from .models import Image
# from .forms import ImageForm

def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'album/showall.html', context)
    
# def upload(request):
#     if request.method == "POST":
#         # ここでrequest.POSTだけでなくrequest.FILESとしていることに注意
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('album:showall')
#     else:
#         form = ImageForm()

#     context = {'form':form}
#     return render(request, 'album/upload.html', context)