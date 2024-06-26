from django.http.response import HttpResponse


def index(request):
    if 'name' in request.session:
        return HttpResponse(f'Hello {request.session.get("name")}')

    name = request.GET.get('name', '')
    if name:
        request.session['name'] = name
        return HttpResponse(f'Hello {name}')

    return HttpResponse('Hello Guest')



def index(request):
    name = request.session.get('name')
    print('[DEBUG] name :', name)

    if name:
        return HttpResponse(f'Hello {name}')

    request.session['name'] = 'Guest'
    return HttpResponse('Hello Guest')
