import re
import pdfkit
from django.http import HttpResponse
from .models import Customer, SaleDeed
from .models import SettlementDeed
# Create your views here.
br = "<br>"

def index(request):
    return HttpResponse("You are in listing documents.")

def get_salesdeed_message(customer_name):
    AllSaleDeed = SaleDeed.objects.filter(Customer=customer_name)
    msg: str = f"Sale deed:{br}"
    for i in AllSaleDeed:
        msg = msg + f"Later on {i.LaterDate}the said {i.SaidName} had sold the schedule of property/{i.Property} to one {i.To} for a valid sale consideration and possession was delivered as recited therein. The said document is duly stamped and registered as Doc.No.{i.DocNo} before {i.BeforeSRO} SRO. The said document is produced as document No.{i.DocNo} in the above list."
        msg = msg + f"{br}{br}"
    AllSettlementDeed =SettlementDeed.objects.filter(Customer=customer_name)
    msg: str = msg + f"Settlement Deed:{br}"
    for i in AllSettlementDeed:
        msg = msg + f"Later on {i.LaterDate} the said {i.SaidName} executed settlement deed to his/her {i.ExecutedBy}(Relationship){i.Relation} out of love and affection in respect to the schedule of property/{i.Property} and possession was delivered as recited therein and the said deed was duly stamped and registered as Doc.No.{i.DocNo} before {i.BeforeSRO} SRO. The said Document is produced as document no.{i.DocNo}in the above list."
        msg = msg + f"{br}{br}"
    return msg

def detail(request, customer_name):
    # Pick all saledeed for selected customer and return
    msg = get_salesdeed_message(customer_name)
    return HttpResponse(msg)
    
def getpdf(request,customer_name):
    msg = get_salesdeed_message(customer_name)
    pdf = pdfkit.from_string(msg, False)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="doc.pdf"'
    return response
