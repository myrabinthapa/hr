from django.http import HttpResponse
def zk_health(_request):
    return HttpResponse("zkpush alive")
