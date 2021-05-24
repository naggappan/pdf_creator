from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer, SaleDeed
from .models import SettlementDeed

# Create your views here.
br = "<br>"


def index(request):
    return HttpResponse("You are in listing documents.")


def detail(request, customer_name):
    # Pick all saledeed for selected customer and return
    AllSaleDeed = SaleDeed.objects.filter(Customer=customer_name)
    msg: str = f"Sale deed:{br}{br}"
    for i in AllSaleDeed:
        msg = msg + f"Later on {i.LaterDate}the said {i.SaidName} had sold the schedule of property/{i.Property} to one {i.To} for a valid sale consideration and possession was delivered as recited therein. The said document is duly stamped and registered as Doc.No.{i.DocNo} before {i.BeforeSRO} SRO. The said document is produced as document No.{i.DocNo} in the above list."
        msg = msg + f"{br}{br}"
    AllSettlementDeed =SettlementDeed.objects.filter(Customer=customer_name)
    msg: str = msg + f"Settlement Deed:{br}{br}"
    for i in AllSettlementDeed:
        msg = msg + f"Later on {i.LaterDate} the said {i.SaidName} executed settlement deed to his/her {i.ExecutedBy}(Relationship){i.Relation} out of love and affection in respect to the schedule of property/{i.Property} and possession was delivered as recited therein and the said deed was duly stamped and registered as Doc.No.{i.DocNo} before {i.BeforeSRO} SRO. The said Document is produced as document no.{i.DocNo}in the above list."
        msg = msg + f"{br}{br}"
    return HttpResponse(msg)

