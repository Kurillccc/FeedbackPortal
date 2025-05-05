from django.shortcuts import render

from .forms import FeedbackForm


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'feedback/success.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/form.html', {'form': form})


def home(request):
    return render(request, 'home.html')
