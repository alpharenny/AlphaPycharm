from django.db import models

TypeOfEmplyment_CHOICES = (
    ('Permanent', 'Permanent',),
    ('Temporary', 'Temporary',),
    ('Contractor', 'Contractor',),
)

TypeOfCustomer_CHOICES = (

    ('Lead', 'Lead',),
    ('Deal', 'Deal',),
    ('CLient', 'Client',),
)
Priority_CHOICES = (
    ('Highest', 'Highest',),
    ('High', 'High',),
    ('Normal', 'Normal',),
    ('Low', 'Low',),
    ('Lowest', 'Lowest',),
)

TaskStatus_CHOICES = (
    ('Cancelled', 'Cancelled',),
    ('Completed', 'Completed',),
    ('Differed', 'Differed',),
    ('In Progress', 'In Progress',),
)


JobType_CHOICES = (
    ('Installation', 'Installation',),
    ('AfterSales', 'AfterSales',),
)



# Create your models here.

class Customers(models.Model):
    class Meta:
        verbose_name_plural = 'Customers'

    Name=models.CharField(max_length=100, unique=True)
    ContactPerson=models.CharField(max_length=100, help_text='First Contact' )
    Status=models.CharField(max_length=10,choices=TypeOfCustomer_CHOICES,default='Lead', help_text='Current Status')
    Phone=models.CharField(max_length=30,null=True, blank=True)
    Mobile=models.CharField(max_length=30, unique=True)
    Email=models.EmailField(max_length=100,null=True, blank=True)
    Address=models.TextField()
    City=models.CharField(max_length=100)
    GPSLocation=models.CharField(max_length=100,null=True, blank=True)
   # LeadSource=models.CharField(max_length=100,null=True, blank=True)
    Remarks=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Name

class Suppliers(models.Model):
    class Meta:
        verbose_name_plural = 'Suppliers'

    Name=models.CharField(max_length=100, unique=True)
    ContactPerson=models.CharField(max_length=100)
    Phone=models.CharField(max_length=30,null=True, blank=True)
    Mobile=models.CharField(max_length=30, unique=True)
    Email=models.EmailField(max_length=100,null=True, blank=True)
    WebAddress=models.CharField(max_length=100,null=True, blank=True)
    Address=models.TextField()
    City=models.CharField(max_length=100)
    GPSLocation=models.CharField(max_length=100,null=True, blank=True)
    Remarks=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Name


class Employees(models.Model):
    class Meta:
        verbose_name_plural = 'Employees'

    Name=models.CharField(max_length=100, unique=True )
    Designation=models.CharField(max_length=100)
    Status=models.CharField(max_length=10,choices=TypeOfEmplyment_CHOICES,default='Permanent')
    Email=models.EmailField(max_length=100,null=True, blank=True)
    Phone=models.CharField(max_length=30)
    Address=models.TextField()
    CostPerHour=models.FloatField()
    Remarks=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Name



class Jobs(models.Model):

    InvNumber=models.CharField(max_length=20, help_text='Enter SO Number if Invoice not created and change later')
    JobType = models.CharField(max_length=15, choices=JobType_CHOICES, default='Installation')
    Status = models.CharField(max_length=15, choices=TaskStatus_CHOICES, default='In Progress')
    CustomerName = models.ForeignKey(Customers, on_delete=models.PROTECT)
    Date = models.DateField()
    Remarks=models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Job'
        unique_together = ('InvNumber', 'JobType',)

    def __str__(self):
        return str(self.InvNumber)+' '+self.JobType


class JobTime(models.Model):
    class Meta:
        verbose_name_plural = 'JobTime'

    InvNumber = models.ForeignKey(Jobs, on_delete=models.PROTECT)
    EmployeeName = models.ForeignKey(Employees, on_delete=models.PROTECT,default=1)
    Date = models.DateField()
    WorkHrs = models.FloatField()
    LabourCost = models.FloatField()
    Remarks = models.CharField(max_length=100)
    def __str__(self):
         return str(self.InvNumber)


class JobMaterial(models.Model):
    class Meta:
        verbose_name_plural = 'JobMaterial'

    InvNumber = models.ForeignKey(Jobs, on_delete=models.PROTECT)
    Suppliers = models.ForeignKey(Suppliers, on_delete=models.PROTECT,default=1)
    Date = models.DateField()
    Material = models.CharField(max_length=100)
    Quantity = models.FloatField()
    UnitCostwithGST = models.FloatField()
    #TotalCost=Quantity*UnitCostwithGST
    Remarks = models.CharField(max_length=100)
    def __str__(self):
         return str(self.InvNumber)


class Tasks(models.Model):
    class Meta:
        verbose_name_plural = 'Tasks'

    Subject = models.CharField(max_length=200)
    EmployeeName = models.ForeignKey(Employees, on_delete=models.PROTECT)
    CustomerName = models.ForeignKey(Customers, on_delete=models.PROTECT)
    CreateDate=models.DateTimeField(auto_now_add=True)
    DueDate = models.DateTimeField()
    Priority=models.CharField(max_length=10,choices=Priority_CHOICES,default='High')
    Status=models.CharField(max_length=15,choices=TaskStatus_CHOICES,default='In Progress')
    Remarks=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.Subject+'  '+str(self.CustomerName)
               #+' '+self.CustomerName
