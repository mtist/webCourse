from django.shortcuts import render


def response(request):
    person_list = Person.object.all()
    return render(request, 'main/persons.html', {'person_list': person_list})