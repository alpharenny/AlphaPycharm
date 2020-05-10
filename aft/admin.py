from django.contrib import admin

from .models import Employees,Customers, Tasks, Jobs, JobTime, Suppliers, JobMaterial
admin.site.site_header = 'Anna Future Technology'
admin.site.site_title  = 'Anna Future Technology - CRM'
#admin.site.register(JobsCost)
##admin.site.register(Tasks)

class InLineJobTime(admin.TabularInline):
    ordering = ("-Date",) ## minus for descending
    model=JobTime
    extra = 0

class InLineCustomerTask(admin.TabularInline):
    model=Tasks
    ordering = ("-DueDate",) ## minus for descending
    extra = 0


class InLineJobMaterial(admin.TabularInline):
    model=JobMaterial
    ordering = ("-Date",) ## minus for descending
    extra = 0

# Admin Action Functions
def Change_TasksStatus(modeladmin, request, queryset):
    queryset.update(Status = 'Completed')

Change_TasksStatus.short_description = "Mark selected Tasks as Completed"



class JobTimeAdmin(admin.ModelAdmin):
    list_display = ('InvNumber','EmployeeName','Date','WorkHrs', 'LabourCost','Remarks')
    list_filter = ('EmployeeName','InvNumber')
    search_fields = ('InvNumber','EmployeeName')
    ordering = ('Date','EmployeeName','InvNumber')


class JobMaterialAdmin(admin.ModelAdmin):
    list_display = ('InvNumber','Suppliers','Date','Material', 'Quantity', 'UnitCostwithGST')
    list_filter = ('Suppliers','InvNumber')
    search_fields = ('InvNumber','Suppliers')
    ordering = ('Date','Suppliers','InvNumber')


class JobsAdmin(admin.ModelAdmin):
    list_display = ('InvNumber','CustomerName','Date','JobType','Status')
    ordering = ('Date','InvNumber')
    list_filter = ('JobType','Status')
    search_fields = ('InvNumber','CustomerName')
    inlines = [InLineJobTime,InLineJobMaterial]


class TasksAdmin(admin.ModelAdmin):
    list_display = ('Subject','DueDate','CustomerName','EmployeeName','Priority','Status')
    list_filter = ('EmployeeName','Status','DueDate')
    search_fields = ('Subject','EmployeeName')
    ordering = ('DueDate','CustomerName')
    actions = [Change_TasksStatus]


class CustomersAdmin(admin.ModelAdmin):
    list_display = ('Name','ContactPerson','Mobile','City','Status')
    search_fields = ('Name','Mobile','City')
    list_filter = ('City','Status')
    ordering = ('Name','Status')
    inlines = [InLineCustomerTask]

    ''' FOR MAKING SECTION IN FORM
    fieldsets = (
        ('Section 1', {
            'fields': ('Name', 'Mobile')
        }),
        ('Section 2', {
            'fields': ('City', 'Status')
        }),
    )'''


class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('Name','ContactPerson','Mobile','City')
    search_fields = ('Name','Mobile','City','Remarks')
    list_filter = ('City',)
    ordering = ('Name',)

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('Name','Phone','Email','Status')
    search_fields = ('Name','Phone','Status')
    ordering = ('Name','Status')


admin.site.register(Customers,CustomersAdmin)
admin.site.register(Suppliers,SuppliersAdmin)
admin.site.register(Employees,EmployeesAdmin)
admin.site.register(Tasks,TasksAdmin)
admin.site.register(Jobs,JobsAdmin)
admin.site.register(JobTime,JobTimeAdmin)
admin.site.register(JobMaterial,JobMaterialAdmin)