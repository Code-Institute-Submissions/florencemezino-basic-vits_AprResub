from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Question
from .forms import QuestionForm


def view_quiz(request):
    """  A view to show all questions """



    questions = Question.objects.all()
    healthgoals = None

    if request.GET:
        if 'question_id' in request.GET:
            healthgoals = request.GET['question_id'].split(',')
            questions = questions.filter(question__name__in=healthgoals)
            return render(request,'quiz/quiz_result.html', context)
        else:
            context = {
                'form': form,
            }
    return render(request,'quiz/view_quiz.html', context)

# def view_quiz_id(request, question_id):
#     """ A view to show an answered question """

# def view_quiz_result_id(request, quiz_result_id):
#     """ A view to show quiz health goal result ""



# use a form ?

@login_required
def add_question(request):
    """ Add a question to quiz """    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('quiz'))

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save()
            messages.success(request, 'Successfully added question!')
            return redirect(reverse('quiz_home', args=[question.id]))
        else:
            messages.error(request, 'Failed to add question. Please ensure the form is valid.')
    else:
        form = QuestionForm()
        
    template = 'quiz/add_question.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_question(request, question_id):
    """ Edit a question to quiz """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('quiz'))

    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated question!')
            return redirect(reverse('quiz', args=[question.id]))
        else:
            messages.error(request, 'Failed to update question. Please ensure the form is valid.')
    else:
        form = QuestionForm(instance=question)
        messages.info(request, f'You are editing {question.name}')

    template = 'quiz/edit_question.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_question(request, question_id):
    """ Delete a question to quiz """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('quiz'))

    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    messages.success(request, 'Question deleted!')
    return redirect(reverse('quiz'))

