import io, csv, datetime, re, os, mimetypes
from django.shortcuts import render
from .models import Users
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, StreamingHttpResponse
from wsgiref.util import FileWrapper
from fpdf import FPDF

def index(request):
    users = Users.objects.values()
    data = users
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for row in data:
        txt = row['name'] + '   ' + row['secondName'] + '   ' + row['date'].strftime("%H:%M:%S - %b %d %Y")
        pdf.cell(200, 10, txt=txt, ln=1,)
    pdf.output("media/queue.pdf")
    return render(request, 'main/person.html', {'users': users})

def users(request):
    name = request.GET.get("name")
    secondName = request.GET.get("secondName")
    reg = "^([A-Z]{1}[a-z]{1,23})$"
    if re.fullmatch(reg, name) == None:
        return HttpResponse('Error! Invalid value for field: "Name"')
    if re.fullmatch(reg, secondName) == None:
        return HttpResponse('Error! Invalid value for field: "Second Name"')
    print(re.fullmatch(reg, name))
    _, created = Users.objects.get_or_create(
                    name = name,
                    secondName = secondName,
                    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    )
    return HttpResponse('Registration complete')
    
def list(request):

    the_file = 'media/queue.pdf'
    filename = os.path.basename(the_file)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(the_file, 'rb'), chunk_size),
                            content_type=mimetypes.guess_type(the_file)[0])
    response['Content-Length'] = os.path.getsize(the_file)    
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
