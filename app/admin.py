from django.contrib import admin
from app.models import Account,Transaction
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','acc_type','balance']

class TransactionManage(admin.ModelAdmin):
    list_display = ['id','From','to','status','amount']    

admin.site.register(Account,UserAdmin)
admin.site.register(Transaction,TransactionManage)


