import re
import pdfkit
from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, SaleDeed
from .models import SettlementDeed
from django.http import JsonResponse
# Create your views here.
def index(request):
    return HttpResponse("You are in listing documents.")

def get_salesdeed_message(customer_name):
    AllSaleDeed = SaleDeed.objects.filter(Customer=customer_name)
    for i in AllSaleDeed:
        Doc_Data = {"sales_data":{"laterdate":i.LaterDate,"saidname":i.SaidName,"property":i.Property,"to":i.To,"docno":i.DocNo,"beforesro":i.BeforeSRO}}
    AllSettlementDeed =SettlementDeed.objects.filter(Customer=customer_name)
    for i in AllSettlementDeed:
        Settlementdeed_data = {"settlement_data":{"laterdate":i.LaterDate,"saidname":i.SaidName,"relation":i.Relation,"to":i.ExecutedBy,"property":i.Property,"docno":i.DocNo,"beforesro":i.BeforeSRO}}
    Doc_Data.update(Settlementdeed_data)
    saldeed="Later "+str(Doc_Data["sales_data"]["laterdate"])+" on  the said " +Doc_Data["sales_data"]["saidname"] +" had sold the schedule of property "+Doc_Data["sales_data"]["property"]+" to one "+Doc_Data["sales_data"]["to"]+" for a valid sale consideration and possession was delivered as recited therein. The said document is duly stamped and registered as Doc.No. "+Doc_Data["sales_data"]["docno"]+" before "+Doc_Data["sales_data"]["beforesro"] +" SRO. The said document is produced as document No."+Doc_Data["sales_data"]["docno"]+" in the above list."
    setdeed="Later on "+ str(Doc_Data["settlement_data"]["laterdate"]) +"the said "+Doc_Data["settlement_data"]["saidname"]+" executed settlement deed to his/her "+ Doc_Data["settlement_data"]["to"]+" (Relationship)"+Doc_Data["settlement_data"]["relation"]+" out of love and affection in respect to the schedule of property/"+Doc_Data["settlement_data"]["property"]+" and possession was delivered as recited therein and the said deed was duly stamped and registered as Doc.No."+Doc_Data["settlement_data"]["docno"]+" before "+Doc_Data["settlement_data"]["beforesro"] +" SRO. The said Document is produced as document no."+Doc_Data["settlement_data"]["docno"]+" in the above list."
    message={"salesdeed":saldeed,"settlementdeed":setdeed}
    return message,Doc_Data

def data(request, customer_name):
    message,Doc_Data = get_salesdeed_message(customer_name)
    return JsonResponse(Doc_Data)

def detail(request, customer_name):
    message ,Doc_Data= get_salesdeed_message(customer_name)
    return JsonResponse(message)
    
def getpdf(request,customer_name):
    message = get_salesdeed_message(customer_name)
    pdf = pdfkit.from_string(message, False)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="doc.pdf"'
    return response
