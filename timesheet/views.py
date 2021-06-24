import os
from django.http import HttpResponse
from django.shortcuts import render
from .models import IMIT
from .models import Physicists
from .models import LAU
from .models import PI
from .models import MIEL
from .models import INYAZ
from .models import ISN
from .models import BMB
from .models import BIO
from .models import GEOG
from .models import HIST
from .models import SAF
from .models import SR
from .models import PSY
from .models import CHEM
from django.shortcuts import get_object_or_404
from rating.models import Users

def index(request):
    data = IMIT.objects.all()
    data2 = Physicists.objects.all()
    data3 = LAU.objects.all()
    data4 = PI.objects.all()
    data5 = MIEL.objects.all()
    data6 = INYAZ.objects.all()
    data7 = ISN.objects.all()
    data8 = BMB.objects.all()
    data9 = BIO.objects.all()
    data10 = GEOG.objects.all()
    data11 = HIST.objects.all()
    data12 = SAF.objects.all()
    data13 = SR.objects.all()
    data14 = PSY.objects.all()
    data15 = CHEM.objects.all()
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request, 'timesheet/timesheet.html', {'data': data, 'type_user': type_user,'data2':data2,'data3':data3,'data4':data4,'data5':data5,'data6':data6,'data7':data7,'data8':data8,'data9':data9,'data10':data10,'data11':data11,'data12':data12,'data13':data13,'data14':data14,'data15':data15})

# Create your views here.
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_pat)
            return response
    raise Http404