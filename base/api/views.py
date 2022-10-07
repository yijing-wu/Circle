from django.http import JsonResponse


def getRoutes(request):
    routes = [
        "GET /api",
        "GET /api/rooms",
        "GET /api/rooms/:id",
    ]
    return JsonResponse(routes, safe=False)
    # JsonResponse: convert it into Json data
