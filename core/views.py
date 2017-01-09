from django.shortcuts import render
from .forms import CadastroNewsletter
from .models import News

def index(request):
    template_name = 'core/index.html'
    context = {}
    if request.method == 'POST':
        form = CadastroNewsletter(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            data = form.cleaned_data
            email = News.objects.get_or_create(email=data["email"])
            context['email'] = data['email']
            print(email)
        else:
            form = CadastroNewsletter()
        context['form'] = form


    return render(request, template_name, context)
