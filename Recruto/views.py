from django.shortcuts import render, redirect


def getMessage(request):
    if request.method == 'GET':
        name = request.GET['name']
        message = request.GET['message']
        return render(request, 'Recruto/answer.html', {"name": name, "message": message})


def main(request):
    return render(request, 'Recruto/index.html')


def page_not_found_view(request, exception):
    return redirect(to='main')
