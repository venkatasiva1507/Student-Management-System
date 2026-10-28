from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student
from .forms import StudentForm


def student_list(request):
    query = request.GET.get("q", "").strip()

    students = Student.objects.all().order_by("-id")

    if query:
        students = students.filter(
            Q(name__icontains=query)
            | Q(email__icontains=query)
            | Q(course__icontains=query)
        )

    return render(request, "students/student_list.html", {
        "students": students,
        "query": query,
    })


def student_add(request):
    form = StudentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("student_list")

    return render(request, "students/student_form.html", {
        "form": form,
        "title": "Add Student",
    })


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("student_list")

    return render(request, "students/student_form.html", {
        "form": form,
        "title": "Update Student",
    })


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "students/student_confirm_delete.html", {
        "student": student,
    })

