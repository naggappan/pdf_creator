from django.db import models

# Create your models here.
from django.db import models


class Document(models.Model):
    doc_name = models.CharField(max_length=200)

    def __str__(self):
        return self.doc_name

class DocType(models.Model):
    doc_type = models.CharField(max_length=200)

    def __str__(self):
        return self.doc_type


class DocValue(models.Model):
    doc_name = models.ForeignKey(Document, on_delete=models.CASCADE)
    doc_type = models.ForeignKey(DocType, on_delete=models.CASCADE)
    dc_date = models.DateField()
    part_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    seat_no = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    ar_no = models.IntegerField()
    print_text = models.CharField(max_length=2000, blank=True)

    def save(self, *args, **kwargs):
        # save the print text by combaining the values as per doc type,
        self.print_text = self.get_text(self.doc_type.doc_type)
        super(DocValue, self).save(*args, **kwargs)

    def get_text(self, doc_type):
        if doc_type == 'Car':
            msg = f'On {self.dc_date} one {self.part_name} came by {self.doc_type} form {self.place} and for transport he had spent {self.amount}. He/she arrived as self.ar_no.'
        elif doc_type == 'Bus':
            msg = f'On {self.dc_date} one {self.part_name} came by tamil nadu Govrment bus form {self.place} and for transport he had spent{self.amount}. His seat No. {self.seat_no}. He/she arrived as {self.ar_no}.'
        else:
            msg = "string not generated"
        return msg
