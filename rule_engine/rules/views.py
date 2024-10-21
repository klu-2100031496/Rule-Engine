
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Rule
from .forms import RuleForm,UserDataForm
from .utils import create_ast_from_rule,evaluate_ast, dict_to_node
import json


# views.py
def home(request):
    return render(request, 'home.html')


def node_to_dict(node):
    if node is None:
        return None
    return {
        'node_type': node.node_type,
        'left': node_to_dict(node.left),
        'right': node_to_dict(node.right),
        'value': node.value
    }


def create_rule(request):
    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            rule_string = form.cleaned_data['rule_string']
            ast = create_ast_from_rule(rule_string)
            ast_dict = node_to_dict(ast)
            Rule.objects.create(rule_string=rule_string, ast=ast_dict)
            return redirect('rule_list')  # Redirect to rule list page after saving
    else:
        form = RuleForm()

    return render(request, 'create_rule.html', {'form': form})
    

def evaluate_rule(request, rule_id):
    rule = get_object_or_404(Rule, id=rule_id)
    # Convert the stored JSON back into a Node object
    ast = dict_to_node(rule.ast)
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            result = evaluate_ast(ast, user_data)
            return render(request, 'evaluate_result.html', {'result': result})
    else:
        form = UserDataForm()

    return render(request, 'evaluate_rule.html', {'form': form, 'rule': rule})
    

def rule_list(request):
    rules = Rule.objects.all()
    return render(request, 'rule_list.html', {'rules': rules})
