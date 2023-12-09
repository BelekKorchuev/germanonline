from django.shortcuts import render


def view_profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'user_profile/profile.html', context)