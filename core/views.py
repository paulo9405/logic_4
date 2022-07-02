from django.shortcuts import render, redirect
from .models import Double
from .forms import DoubleForm
import re



def double_list(request):
    double_list = Double.objects.all()
    return render(request, 'double_list.html', {'double_list': double_list})


def double_create(request):
    form = DoubleForm(request.POST or None)
    name_user = form.data.get('name')
    val_user = request.POST.get('value')
    value_user = int(val_user or 0)
    data_obj = None
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


    obj = Double.objects.filter(name=name_user, value=val_user)
    if obj.count() > 0:
        data_obj = obj[0]

    if data_obj is not None:
        return render(request, 'double_exist.html', {'name_user_obj': data_obj.name,
                                             'value_user_obj': data_obj.value,
                                             'date_user_obj': data_obj.date})

    elif value_user > 1000 or value_user < -1000:
        erro_value = 'Plaese dont use value biggest than 1000 or -1000'
        return render(request, 'double_create.html', {'form': form, 'erro_value': erro_value})

    elif form.is_valid() and (regex.search(name_user) != None):
        erro_char = "Please Don't use especial character!"
        return render(request, 'double_create.html', {'form': form, 'erro_char': erro_char})

    elif form.is_valid() and (regex.search(name_user) == None):
        form.save()
        return redirect('double_list')
    return render(request, 'double_create.html', {'form': form})




