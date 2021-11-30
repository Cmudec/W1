from django.shortcuts import render
import operator as op


# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)


def first(request):
    context = {
        'n1': request.GET['number_1'],
        'op': request.GET['operator'],
        'n2': request.GET['number_2']
    }
    ops = {
        '+': op.add,
        '*': op.mul,
        '-': op.sub,
        '/': op.truediv
    }

    context['res'] = ops[context['op']](float(context['n1']), float(context['n2']))

    return render(request, "first.html", context)


def second(request, id):
    context = {
        'number': id
    }
    return render(request, "second.html", context)
