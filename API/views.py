from django.http import HttpResponse , JsonResponse
def home_url(request):
    print("function based response worked")
    friends = [
        'Ankit' ,
        'Ram',
        'shaym'
    ]
    return JsonResponse(friends, safe=False)