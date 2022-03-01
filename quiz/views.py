from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

# Create your views here.
def quiz_home(request):
    if request.method == 'POST':
        print(request.POST)
        questions = Question.objects.all()
        healthgoalscore = 0
        for q in questions:
            healthgoalscore += 1
            print(request.POST.get(q.question))
            print()
        context = {
            'healthgoalscore': healthgoalscore,
        }
        return render(request,'quiz/quiz_result.html', context)
    else:
        questions = Question.objects.all()
        context = {
            'question_id': question_id,
            'question_name': question,
            'question_description': question_description,
            'option1': option1,
            'option2': option2,
            'option3': option3,
            'option4': option4,
            'option5': option5,
            'option6': option6,
            'option7': option7,
            'option8': option8,
            'option9': option9,
            'option10': option10,
            'option11': option11,
            'option12': option12,
            'option13': option13,
            'option14': option14,
            'option15': option15,
            'option_text': option_text,

        }
        return render(request, 'quiz/quiz_home.html', context)


@login_required
def add_question(request):
    """ Add a question to quiz"""    
    if request.user.is_superuser:
        form = addQuestionform()
        if(request.method == 'POST'):
            form = addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context = {
            'form': form
            }
        return render(request, 'quiz/add_question.html', context)
    else: 
        return redirect('quiz') 


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

