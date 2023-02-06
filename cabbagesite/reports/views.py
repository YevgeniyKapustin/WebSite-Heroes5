from django.contrib import messages
from django.shortcuts import render, redirect

from reports.forms import ReportForm
from stats.stat import Stats


def send_reports(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Отчёт отправлен')
            Stats().save()
            return redirect('home')
        else:
            messages.error(request, 'Ошибка отправки отчёта')
    else:
        form = ReportForm()
    return render(request, 'reports/reports_form.html', {'form': form})
