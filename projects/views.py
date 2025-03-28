from django.shortcuts import render
from projects.models import Project

# Create your views here.

def project_index(request):
    """
    This Python function retrieves all projects from the database and passes them to a template for
    rendering.

    :param request: The `request` parameter in the `project_index` function is typically an HttpRequest
    object that represents the current web request. It contains information about the request made by
    the client, such as the request method, headers, user session, and more. This parameter is commonly
    used in Django views to interact with
    :return: The `project_index` function is returning a rendered HTML template named
    "project_index.html" along with a context containing all projects retrieved from the database.
    """
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    """
    This function retrieves a specific Project object based on its primary key and renders a template
    with the project details.

    :param request: The `request` parameter in the `project_detail` function is an HttpRequest object
    that Django passes to the view function when it's called. It contains information about the current
    web request, such as the user making the request, any data sent with the request, and other metadata
    related to the request
    :param pk: The `pk` parameter in the `project_detail` function stands for Primary Key. It is used to
    uniquely identify a specific record in the database. In this case, the function is retrieving a
    Project object from the database based on its primary key value
    :return: The `project_detail` function is returning a rendered HTML template called
    "project_detail.html" with the context containing the project object retrieved from the database
    with the primary key `pk`.
    """
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)
