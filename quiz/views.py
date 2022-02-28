from django.shortcuts import redirect,render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.http import HttpResponse
 
# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        healthgoalscore=0
        for q in questions:
            healthgoalscore+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
        context = {
            'healthgoalscore':healthgoalscore,
        }
        return render(request,'quiz/quiz_result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz/quiz_home.html',context)
 
 # admin : add question
@login_required
def addQuestion(request):
     """ Add a question to quiz"""    
    if request.user.is_superuser:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'quiz/add_question.html',context)
    else: 
        return redirect('quiz') 

# admin : edit question
@login_required
def editQuestion(request, quiz_id):
    """ Edit a question to quiz """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('quiz'))

    quiz = get_object_or_404(Product, pk=quiz_id)
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES, instance=quiz)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated question!')
            return redirect(reverse('quiz_home', args=[quiz.id]))
        else:
            messages.error(request, 'Failed to update question. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=quiz)
        messages.info(request, f'You are editing {quiz.number}')

    template = 'quiz/edit_question.html'
    context = {
        'form': form,
        'question': question,
        'options': options,
    }

    return render(request, template, context)

# admin : delete question
@login_required
def delete_product(request, product_id):
    """ Delete a question to quiz """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('quiz'))
        
    question = get_object_or_404(Product, pk=product_id)
    question.delete()
    messages.success(request, 'Question deleted!')
    return redirect(reverse('quiz'))
