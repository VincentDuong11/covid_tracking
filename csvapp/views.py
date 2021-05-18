"""[Author: Chanh Duong. Student number: 040-681-356]
    """
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from csvapp.models import Record
from .forms import RecordForm
from django.db.models.functions import Lower

import pandas as pd
import csv
import io
import operator


def record_list(request):
    records = Record.objects.all()
    context = {'records': records}
    # return render(request, 'csvapp/record_list.html', context)
    prompt = {'order': 'Order of the CSV should be pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal'}
    if request.method == "GET":
        return render(request, 'csvapp/record_list.html', context)
    try:  # Handle the error when click the upload button
        csv_file = request.FILES['file']
    except Exception:
        messages.error(request, 'THERE IS NO FILE TO UPLOAD')
        return redirect('/csvapp/list')
    # check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
        return redirect('/csvapp/list')

    try:  # Handle the col_list error if not .csv file uploaded
        col_list = ['pruid', 'prname', 'prnameFR', 'date', 'numconf',
                    'numprob', 'numdeaths', 'numtotal', 'numtoday', 'ratetotal']
        data_set = pd.read_csv(csv_file, encoding='utf-8',
                               nrows=100, parse_dates=['date'], usecols=col_list).dropna()
    except IOError as e:  # handle IO error
        print(e.message)
    except Exception as e:  # handle col_list error
        return redirect('/csvapp/list')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    # convert dataframe to new csv in order to be read by StringIO
    io_string = io.StringIO(data_set.to_csv())
    next(io_string)
    readData = csv.reader(io_string, delimiter=',', quotechar="|")
    for column in readData:
        _, created = Record.objects.update_or_create(  # Write new data to database
            pruid=column[1],
            prname=column[2],
            prnameFR=column[3],
            date=column[4],
            numconf=column[5],
            numprob=column[6],
            numdeaths=column[7],
            numtotal=column[8],
            numtoday=column[9],
            ratetotal=column[10]
        )
    # context = {}
    # return render(request, 'csvapp/record_upload.html', context)
    messages.success(request, 'UPLOAD SUCCESSFUL')
    return redirect('/csvapp/list')

# CSV export function


def record_download(request):
    records = Record.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Chanh-Covid19-Record.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['pruid', 'prname', 'prnameFR', 'date', 'numconf',
                     'numprob', 'numdeaths', 'numtotal', 'numtoday', 'ratetotal'])

    for record in records:
        writer.writerow([
            record.pruid,
            record.prname,
            record.prnameFR,
            record.date,
            record.numconf,
            record.numprob,
            record.numdeaths,
            record.numtotal,
            record.numtoday,
            record.ratetotal])
    return response

# Form for users to input new Data


def record_form(request, id=0):
    # if request.method == 'GET':
    #     if id == 0:
    #         form = RecordForm()
    #     else:
    #         record = Record.objects.get(pk=id)
    #         form = RecordForm(instance=record)
    #     return render(request, 'csvapp/record_form.html', {'form': form})
    # else:
    #     if id == 0:
    #         form = RecordForm(request.POST)
    #     else:
    #         record = Record.objects.get(pk=id)
    #         form = RecordForm(request.POST, instance=record)

    #     if form.is_valid():
    #         form.save()
    #         return redirect('/csvapp/list')


    if request.method == 'GET':
        if id == 0:
            form = RecordForm()
        else:
            record = Record.objects.get(pk=id)
            form = RecordForm(instance=record)
        return render(request, 'csvapp/record_form.html', {'form': form})
    else:
        if id == 0:
            form = RecordForm(request.POST)
        else:
            record = Record.objects.get(pk=id)
            form = RecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
        return redirect('/csvapp/list')

# Delete a specific data function


def record_delete(request, id):
    record = Record.objects.get(pk=id)
    if request.method == "POST":
        record.delete()
        return redirect('/csvapp/list')
    return render(request, 'csvapp/record_delete.html')

# Delete all data function


def record_delete_all(request):
    record = Record.objects.all()
    if request.method == "POST":
        record.delete()
        return redirect('/csvapp/list')
    return render(request, 'csvapp/record_delete_all.html')




# Sort Records by ID ascendingly
def sort_recordId_Ascending(request):
    recordList = Record.objects.all().order_by('pruid')
    context = {'records': recordList}
    return render(request, 'csvapp/record_list.html', context)

# Sort Records by ID desscendingly
def sort_recordId_Descending(request):
    recordList = Record.objects.all().order_by('-pruid')
    context = {'records': recordList}
    return render(request, 'csvapp/record_list.html', context)

# Sort Records by name asscendingly
def sort_recordName_Ascending(request):
    recordList = Record.objects.order_by(Lower('prname'))
    context = {'records': recordList}
    return render(request, 'csvapp/record_list.html', context)

# Sort Records by name desscendingly
def sort_recordName_Descending(request):
    recordList = Record.objects.order_by(Lower('prname').desc())
    context = {'records': recordList}
    return render(request, 'csvapp/record_list.html', context)


# bar chart view
def bar_chart(request):
    records = Record.objects.filter(prname = 'Canada')
    print(records)
    context = {'records': records}
 
    return render(request, 'csvapp/bar_chart.html', context)

# horizontal bar chart view
def horizontal_bar_chart(request):
    records = Record.objects.filter(prname = 'Canada')
    print(records)
    context = {'records': records}
 
    return render(request, 'csvapp/horizontal_bar_chart.html', context)