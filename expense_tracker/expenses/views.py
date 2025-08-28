from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum


from django.db.models import Q

def expense_list(request):
    # Start with non-deleted expenses
    expenses = Expense.objects.filter(is_deleted=False).order_by('date', 'id')

    # Get filter parameters
    category = request.GET.get('category')
    exp_type = request.GET.get('type')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Apply filters if present
    if category:
        expenses = expenses.filter(category=category)
    if exp_type:
        expenses = expenses.filter(type__iexact=exp_type.lower())
    if start_date:
        expenses = expenses.filter(date__gte=start_date)
    if end_date:
        expenses = expenses.filter(date__lte=end_date)

    # Calculate cumulative expense, balance, etc.
    cumulative_expense = 0
    total_income = 0
    expense_data = []

    for exp in expenses:
        if exp.type.lower() == 'income':
            total_income += exp.amount
        else:
            cumulative_expense += exp.amount

        balance = total_income - cumulative_expense

        expense_data.append({
            'id': exp.id,
            'description': exp.description,
            'amount': exp.amount,
            'category': exp.category,
            'payment_method': exp.payment_method,
            'type': exp.type,
            'date': exp.date,
            'cumulative_expense': cumulative_expense,
            'balance': balance,
        })

    # Get list of unique categories for the filter dropdown
    categories = Expense.objects.filter(is_deleted=False).values_list('category', flat=True).distinct()

    context = {
        'expenses': expense_data,
        'categories': categories,
    }

    return render(request, 'expenses/expense_list.html', context)



# Add new expense
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

# Edit existing expense
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/edit_expense.html', {'form': form})

# Soft Delete
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.is_deleted = True
    expense.save()
    return redirect('expense_list')


from django.shortcuts import render
from .models import Expense
from django.db.models import Sum

def dashboard(request):
    # Get all non-deleted expenses
    expenses = Expense.objects.filter(is_deleted=False)

    # Total income
    total_income = expenses.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0

    # Total expenses
    total_expense = expenses.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0

    # Balance
    balance = total_income - total_expense

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, 'expenses/dashboard.html', context)

def deleted_expenses(request):
    deleted_expenses = Expense.objects.filter(is_deleted=True)
    context = {
        'deleted_expenses': deleted_expenses
    }
    return render(request, 'expenses/deleted_expenses.html', context)

def delete_all_deleted_expenses(request):
    Expense.objects.filter(is_deleted=True).delete()
    return redirect('recently_deleted')

def reports(request):
    return render(request, 'expenses/reports.html')

def restore_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, is_deleted=True)
    expense.is_deleted = False
    expense.save()
    return redirect('recently_deleted')