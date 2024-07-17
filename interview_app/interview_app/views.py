import logging
import sys
from app.tasks import add
from app.models import TaskResult
from django.http import HttpResponse

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def add_result(request):
    response_text = "Result added."
    a = request.GET.get("a", 0)
    b = request.GET.get("b", 0)
    logging.info("adding result")
    logging.info(f"Parameters: a: {a}, b: {b}")
    result = add.delay(a, b)
    if result.successful():
        TaskResult.objects.create(task_name="add", result=result.get())
        logging.info("result added")
    else:
        response_text = result.get()
    return HttpResponse(response_text)
