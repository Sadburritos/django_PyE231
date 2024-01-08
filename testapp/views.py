import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import StreamingHttpResponse, FileResponse, JsonResponse
from django.urls import resolve
from django.views.decorators.http import require_GET

from bboard.models import Rubric, Bb


# def index(requaste):
#     resp_content = ("Тута будет ", "главная ", 'страница ', 'саййта ')
#     resp = StreamingHttpResponse(resp_content, content_type='text/plain; charset=utf-8')
#     return resp
# def index(requast):
#     file_name = r"static/bg.jpg"
#     return FileResponse(open(file_name, 'rb'))
# def index(rureuast):
#     data = {"file": "Боброцикл", "conent": "Гоночный", "price": 100000000000}
#     return JsonResponse(data, encoder=DjangoJSONEncoder)
# def index(request):
#     context = {"title": "тест"}
#     return render(request, 'test.html', context)

# def index(request):
#     r = get_object_or_404(Rubric, name="Движимость")
#     return redirect('bboard:by_rubric',rubric_id=r.id)wcrfcxxxs

@require_GET
def index(request):
    r = get_object_or_404(Rubric, name="Движимость")
    bbs = get_list_or_404(Bb, rubric=r)

    res = resolve('/test/')

    context = {"title": "TEST", "bbs": bbs, "res": res}

    return render(request, 'test.html', context)
