from django.shortcuts import render, get_object_or_404
from .models import FchatWebsite


def fchat_website_view(request, name, environment):
    print('come')
    # Fetch the instance based on name and environment
    website = get_object_or_404(FchatWebsite, name=name, environment=environment)

    print(website.scripts)
    # Render the instance to an HTML template
    return render(request, 'fchat_website.html', {'website': website})
