from django.shortcuts import render, redirect, HttpResponse
import pymysql
import mysql.connector as pymysql
from tkinter import messagebox
_from=''
_to=''
_cabin=''
firstname=''
lastname=''
age=''
gender=''
dod=''
dor=''
mobile=''
mobile1=''
email=''
email1=''
def home1(request):
    global _from,_to,_cabin,firstname,lastname,age,gender,dod,dor,mobile,email
    if(request.method=="POST"):
        m=pymysql.connect(host="localhost",user="root",password="Muthamizh@5609",database="flight")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="from_1":
                _from=value
            if key=="to":
                _to=value
            if key=="value1":
                _cabin=value
            if key=="fname":
                firstname=value
            if key=="lname":
                lastname=value
            if key=="age":
                age=value
            if key=="gender":
                gender=value
            if key=="depart":
                dod=value
            if key=="return1":
                dor=value
            if key=="mobile":
                mobile=value
            if key=="mobile1":
                mobile1=value
            if key=="mail":
                email=value
            if key =="mail1":
                email1=value
        c="insert into booking values('"+_from+"','"+_to+"','"+_cabin+"','"+firstname+"','"+lastname+"','"+age+"','"+gender+"','"+dod+"','"+dor+"','"+mobile+"','"+email+"');"
        cursor.execute(c)
        m.commit()
        m.close()
        return render(request,"ticketbooking/thankyou.html")
    return render(request,"ticketbooking/fbook.html")
def sum(request):
    return render(request,"ticketbooking/sum.html")
def about(request):
    return render(request,"ticketbooking/Ap.html")
