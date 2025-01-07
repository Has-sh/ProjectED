from django.shortcuts import render

# Create your views here.
def tutor_matcher(request):
    return render(request, 'tutor-matcher/tutor_matcher.html')

def find_tutors(request):
    return  render(request, 'find-tutors/find_tutors.html')
