from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required
def course_chat_room(request, course_slug):
    try:
        course = request.user.courses_joined.get(id=course_slug)
    except:
        return HttpResponseForbidden()
    return render(request,
                  'chat/room.html',
                  {'course': course})
