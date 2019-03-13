from django.shortcuts import render, redirect
from .forms import ImageForm, ProfileForm
from .models import Image, Profile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your instagram account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('index')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account <a href="/accounts/login">here </a>.')
    else:
        return HttpResponse('Activation link is invalid!')


@login_required(login_url='/accounts/login')
def index(request):
    form = ImageForm()
    image = Image.objects.all()

    return render(request, 'index.html', {"image": image})


def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')

    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})


def profile(request):
    images = Image.objects.all()
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    posts = Image.objects.filter(user=current_user)
    image_form = ProfileForm()
    if request.method == 'POST':
        image_form = ProfileForm(
            request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
        else:
            image_form = ProfileForm()

    return render(request, 'profile.html', {"image_form": image_form, "posts": posts, "profile": profile, "images": images})


def update_profile(request):
    # current_user = request.user
    if request.method == 'POST':
        me = User.objects.get(username=request.user)
        user = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"form": form})
