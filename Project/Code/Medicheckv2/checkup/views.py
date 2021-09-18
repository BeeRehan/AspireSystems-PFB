from django.http import response, HttpResponse
from django.shortcuts import redirect, render
from appointment.models import AppoinmentDetails
from .models import CheckupDetails
from .form import checklistForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkup.serializers import CheckupSerializer
from rest_framework.response import Response
from rest_framework.decorators import MethodMapper, api_view


# Create your views here.
@login_required(login_url="/")
def create_checklist(request):
    apps = AppoinmentDetails.objects.filter(status="approved", doctor=request.user)
    return render(request, "checklist.html", {"apps": apps})


@login_required(login_url="/")
def view_checklist(request, pk):
    title = "Add Report"
    form = checklistForm()
    return render(
        request, "to_add_checklist.html", {"title": title, "form": form, "pk": pk}
    )


@login_required(login_url="/")
def add_checklist(request, pk):
    title = "Add Report"
    form = checklistForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save(pk)
            return redirect("/checkup/create_checklist")
        else:
            messages.info(request, "Not valid")
            return render(
                request,
                "to_add_checklist.html",
                {"title": title, "form": form, "pk": pk},
            )
    else:
        messages.info(request, "Not a post request")
        return render(
            request, "to_add_checklist.html", {"title": title, "form": form, "pk": pk}
        )


@login_required(login_url="/")
def doc_get_checklis(request, pk):
    header = "Previous Checkup Details!!!"
    apps = AppoinmentDetails.objects.filter(user_id=pk, status="approved")
    return render(
        request,
        "detail_appoinment.html",
        {"apps": apps, "title": "Previuous", "header": header},
    )


@login_required(login_url="/")
def pat_get_checklis(request, pk):
    try:
        title = "Checkup"
        header = "Checkup Details"
        checks = CheckupDetails.objects.get(appointment_id=pk)
        return render(
            request,
            "show_checklist.html",
            {"header": header, "title": title, "checks": checks},
        )
    except Exception:
        messages.info(request, "No checkup details found")
        return render(request, "show_checklist.html")


@api_view(["GET"])
def api_patient_get_checklist(request, pk):
    checks = CheckupDetails.objects.get(appointment_id=pk)
    serializer = CheckupSerializer(checks)
    return Response(serializer.data)


@api_view(["POST"])
def api_patient_post_checklist(request):
    if request.method == "POST":
        serializers = CheckupSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return HttpResponse("Inserted Successfully!!!")
    else:
        return HttpResponse("Not a Post request!!!")
