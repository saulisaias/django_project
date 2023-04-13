from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # REDIRECCION EN CASO QUE ESTE BIEN Y SE ENVIA EL CORREO
            email = EmailMessage(
                "Veterinaria: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no-reply@inbox.mailtrap.io",
                ["saulisaias1501@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                # SI jalo se redireccion a pagina de OK
                return redirect(reverse('contact') + "?ok")
            except:
                # NO jalo se redireccion a pagina de fallo
                return redirect(reverse('contact')+ "?fail")


    return render(request, "contact/contact.html", {'form': contact_form})
