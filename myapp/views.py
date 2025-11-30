from django.shortcuts import render


def index(request):
    """Home / portfolio landing page."""
    context = {
        'name': 'Kyle and Davene',
        'title': 'Kylee and  Davane — Portfolio',
        'summary': 'Welcome to are simple portfolio. Work on Game Dev and Web Dev projects.'
    }
    return render(request, 'index.html', context)


def projects(request):
    """Projects listing page."""
    # Prefer database-backed projects when available
    from .models import Project

    projects_qs = Project.objects.all()
    if projects_qs.exists():
        projects = projects_qs
    else:
        # fallback sample projects when DB empty
        projects = [
            {'title': 'Game Dev', 'description': 'Personal and collaborative game development projects (Unity, Godot, prototypes).'},
            {'title': 'Web Dev', 'description': 'Web applications and sites built with Django, JavaScript, and modern front-end tooling.'},
        ]
    return render(request, 'projects.html', {'projects': projects})


def project_detail(request, pk):
    """Show a single project detail page."""
    from .models import Project
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        from django.http import Http404
        raise Http404('Project not found')
    return render(request, 'project_detail.html', {'project': project})


def about(request):
    """About page."""
    about_text = 'This is a small portfolio site created from an existing Django project.'
    return render(request, 'about.html', {'about': about_text})

