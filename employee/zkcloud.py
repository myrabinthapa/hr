import json
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def biometric_push_view(request: HttpRequest):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    ct = (request.META.get("CONTENT_TYPE") or "")
    if ct.startswith("application/json"):
        try:
            data = json.loads(request.body.decode("utf-8") or "{}")
        except Exception as e:
            return JsonResponse({"status":"error","message":f"Bad JSON: {e}"}, status=400)
    else:
        data = request.POST.dict()

    emp = data.get("emp_id") or data.get("emp") or data.get("user_id")
    ts  = data.get("timestamp") or data.get("ts") or data.get("punch_time")
    ev  = data.get("event") or data.get("status")
    return JsonResponse({"status":"ok","received":{"emp":emp,"timestamp":ts,"event":ev}})
