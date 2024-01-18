from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse 
from django.http import HttpResponse
from groceries.models import cart
from .models import *
import json
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.http import FileResponse
# import sys
# sys.setrecursionlimit(10000)

# id = request.session.get('session_id')
 
def register(request):
   if request.method=='POST': 
    db=json.loads(request.body)
    username=db['Username']
    password=db['Password']
    confirmpassword=db['Confirmpassword']
    email=db['Email']
    first_name=db['Firstname']
    last_name=db['Lastname']
    if username==""or email==""or password==""or first_name==""or last_name==""or confirmpassword=="":
         return JsonResponse(status=400) 
    elif User.objects.filter(username=username).exists():
       return JsonResponse({'message':'Username already registered'}) 
    elif User.objects.filter(email=email).exists():
       return JsonResponse({'message':'Email already registered'}) 
    else:  
         user = User.objects.create_user(username,email,confirmpassword) 
         user.first_name = first_name
         user.last_name = last_name 
         user.save()
         return JsonResponse({'message':'Successfully registered'})   
def login1(request):
   if request.method=='POST': 
    db=json.loads(request.body)
    username=db['Username']
    password1=db['Password']
    user = authenticate(request,username=username,password=password1)
    if user is not None:
      superuser=user.is_superuser    
      login(request,user,backend='django.contrib.auth.backends.ModelBackend')  
      if superuser==True:    
       return JsonResponse({'message':'Manager'})
      else :
       return JsonResponse({'message':'I am a user'})
    else:
      return JsonResponse({'message':'Invalid login'}) 
   elif request.method=='GET':
    db=json.loads(request.body)
    username=db['Username']
    password1=db['Password']
    user = authenticate(request,username=username,password=password1)
    if user is not None:
      superuser=user.is_superuser    
      login(request,user,backend='django.contrib.auth.backends.ModelBackend')  
      if superuser==True:    
       return JsonResponse({'message':'Manager'},superuser)
      else :
       return JsonResponse({'message':'I am a user'},superuser)
    else:
      return JsonResponse({'message':'Invalid login'})
# def logout(request):
#       logout(request)      
#       return JsonResponse({'message':'Logged out successfully'})
def section(request):
  if request.method=='GET':
     sections1=sections.objects.filter(removed=False)
   #  section1=list((sections.objects.filter(removed=False).values('id','SectionName','Img')))
     sectionsdata = [{'id': section.id,'name': section.SectionName, 'image': section.Img.url} for section in sections1]
     return JsonResponse(sectionsdata,safe=False) 
  if request.method=='POST':
    if request.user.is_authenticated: 
   #  if request.FILES.has_key('data'):
       file = request.FILES.get('sectionImage')
    #  data = file.read() 
       name=request.POST.get('sectionName')
       sections.objects.create(SectionName=name,Img=file)
       id=sections.id
       return JsonResponse({'message':'Successfully added'}) 
def product(request):
  if request.method=='GET':
     products1=products.objects.filter(removed=False)
   #  section1=list((products.objects.filter(removed=False).values('id','SectionName','Img')))
     productsdata = [{'id': product.id,'name': product.ProductName,'image': product.Img.url,'price': product. Priceperun} for product in products1]
     return JsonResponse(productsdata,safe=False) 
  if request.method=='POST': 
   if request.user.is_authenticated:
    id=request.POST.get('id')
    name=request.POST.get('product')
    qt=request.POST.get('qt')
    mfdate=request.POST.get('mfdate')
    expdate=request.POST.get('expdate') 
    priceperun=request.POST.get('price')
    Img= request.FILES.get('productImage')
    products.objects.create(section_id=id,qt=qt,ProductName=name,Mf_Date=mfdate,Ep_Date=expdate,Priceperun=priceperun,Img=Img)
    return JsonResponse({'message':'Product successfully added'}) 
def deletesection(request):
   if request.method=='POST': 
      db=json.loads(request.body)
      id1=db['name']
      delt=sections.objects.filter(id=id1)
      for object in delt:
       object.removed = True
       object.save()
      # delt.removed="True"
      # delt.save() 
      # delt=sections.objects.get(SectionName=id1)
      # delt.removed=True
      # delt.save() 
      return JsonResponse({'message':'Section deleted successfully'})
      # delt1=products.objects.filter(id=id1)
      # return HttpResponse(status=204)
def deleteproduct(request):
   if request.method=='POST':  
      db=json.loads(request.body)
      id1=db['id']
      delt=products.objects.filter(id=id1)
      for object in delt:
       object.removed = True
       object.save()
      return JsonResponse({'message':'Product deleted successfully'})   
def editsection(request):
   if request.user.is_authenticated: 
    if request.method=='POST': 
      # db=json.loads(request.body)
      # id3=db['id'] 
      # name=db['name']
      id3=request.POST.get('id')
      name=request.POST.get('name')
      file = request.FILES.get('image')
      # file = db['image']
      # file= request.FILES.get('image')
      edits=sections.objects.get(id=id3,removed=False)
      if file is not None:
       edits.Img=file
      if name is not None:
       edits.SectionName=name
      edits.save()
      return JsonResponse({'message':'Section edited successfully'})
   else:
      return JsonResponse({'message':'bye'})
def editproduct(request):
  if request.user.is_authenticated:
   if request.method=='POST': 
      # db=json.loads(request.body)
      id4=request.POST.get('id')
      editp=products.objects.get(id=id4,removed=False)
      name=request.POST.get('name')
      qt=request.POST.get('qt1')
      mf_Date = request.POST.get('date1')
      ep_Date = request.POST.get('date2')
      priceperun =request.POST.get('price')
      Img= request.FILES.get('image')
      if name is not None:
       editp.ProductName=name
      if qt is not None:
       editp.qt=qt
      if mf_Date is not None:
       editp.Mf_Date=mf_Date
      if ep_Date is not None:  
       editp.Ep_Date=ep_Date
      if priceperun is not None: 
       editp.Priceperun=priceperun
      if Img is not None: 
        editp.Img=Img
      editp.save() 
      return JsonResponse({'message':'Product edited successfully'})
# def addtocart(request):
#    if request.user.is_authenticated:
#     if request.method=='POST':
#      user=request.user.id
#      db=json.loads(request.body)
#      id5=db['productid']
#      lt2=products.objects.get(id=id5,removed = False)
#      price=lt2.Priceperun
#    #   author,created = cart.objects.get_or_create(product_id=id5,customer_id=user,Priceperun=price)
#    # #   y= author.Quantity
#    # #   print(y)
#    #   if created==False:         
#    #     z=author.Quantity
#    #     z=z+1
#    #     print(z)
#    #     w=author.Priceperun
#    #     author.Netprice=z*w
#    #     author.Netprice=z
#    #     author.save()
#      cart.objects.create(product_id=id5,customer_id=user,Priceperun=price,Netprice=price)
#      return JsonResponse({'message':'Product added successfully'})
def addtocart(request):
   if request.user.is_authenticated:
    if request.method=='POST':
     user=request.user.id
     db=json.loads(request.body)
     id5=db['productid']
     lt2=products.objects.get(id=id5,removed = False)
     price=lt2.Priceperun
   #   qt=lt2.Quantity
   #   a=price*qt
     author= cart.objects.filter(product_id=id5,customer_id=user,removed = False).first()
     if author is None:
      cart.objects.create(product_id=id5,customer_id=user,Priceperun=price,Netprice=price)
      return JsonResponse({'message':'Product added successfully'})
     else:
      return JsonResponse({'message':'Product already exists'})
   #   try:
   #    author= cart.objects.get(product_id=id5,customer_id=user,removed = False)
   #    return JsonResponse({'message':'Product already exists'})
   #   except cart.DoesNotExist:
   #    cart.objects.create(product_id=id5,customer_id=user,Priceperun=price)
   #    return JsonResponse({'message':'Product added successfully'})
     
      
def qtyinc(request):
      if request.method=='POST':
       db=json.loads(request.body)
       id9=db['productid']
       qty=db['quantity']
      #  price=lt1.Priceperun
       lt2=products.objects.get(id=id9,removed = False)
       price=lt2.Priceperun
       net=price*qty
       lt3=cart.objects.filter(product_id=id9,removed = False)
       for lt1 in lt3:
        lt1.Quantity=qty
        lt1.Netprice=net
        lt1.save()
       return JsonResponse({'message':'Product added successfully'})
def removefromcart(request):
    if request.method=='POST':
     db=json.loads(request.body)
     id6=db['id']
     lt0=cart.objects.filter(product_id=id6,removed = False)
     for object in lt0:
          object.removed = True
          object.save()
     return JsonResponse({'message':'Product removed successfully'}) 
def cartview(request):
   if request.user.is_authenticated:
    if request.method=='GET': 
         user=request.user.id
         viewcart=cart.objects.filter(customer_id=user,removed=False,ordered=False)
      # productid=viewcart.product.id
      # productname=viewcart.product.ProductName 
      # productimage=viewcart.product.Img.url
         net=0
         for y in viewcart:
           w=y.Netprice
           net=w+net
         # net1=[{ 'NETAMOUNT':net, }]
         net1=str(net)
         productsdata = [{'name': x.product.ProductName, 'productid': x.product.id,'image': x.product.Img.url,'quantity': x.Quantity,'Netprice': x.Netprice,'Id': x.customer.id} for x in viewcart]
         net2=({ 'productsdata':productsdata,'NETAMOUNT':net1 })
         # print(net2)
         return JsonResponse(net2,safe=False)
      # else:
      #   return JsonResponse({'message':'Product deleted successfully'})        
def buynow(request):
   if request.user.is_authenticated:   
     if request.method=='POST':
       user=request.user.id
       db=json.loads(request.body)
       id=db['id']
      #  print(id)
      #  print(user)
       b1=products.objects.filter(id=id,removed=False)
       for y in b1:
        y.qt-=1
        y.save()
       buy=cart.objects.filter(product_id=id,removed=False,customer_id=user)
       for x in buy:
        x.ordered=True
        x.save()
       return JsonResponse({'message':'Ordered successfully'}) 
def buycart(request):
    if request.user.is_authenticated:
     if request.method=='GET':
        user=request.user.id
        buy=cart.objects.filter(removed=False,customer_id=user)  
        for x in buy:
          x.ordered=True
          x.save() 
        return JsonResponse({'message':'Ordered successfully'}) 
#       if request.method=='GET':
#        user=request.user.id
# def searchpro(request):
#      if request.method=='POST':
#       db=json.loads(request.body)
#       name=db['name']
#       search=products.objects.get(ProductName=name)
#       search.removed=True
#       search.save()
       
# category=list(Category.objects.filter(deleted_status=False).values('id','category_name','category_image'))
#             return JsonResponse(category,safe=False)
#         else:
#             return JsonResponse({'message': 'You Are not authenticated'},status=401)
      # SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
      # s = SessionStore()
      # backend='django.contrib.auth.backends.ModelBackend
      # request.session['team'] = '20'
      # id = request.session.get('session_id')  
      # response = "User Id".format(user_id)
      # return HttpResponse(response)
      # request.session['user']=[user.id]
      # current_user = request.session['user']
      # param = {'current_user': current_user}
      # return param
      # request.session['customer'] = user.id
      # s = SessionStore()
      # s.create()
      # pk=s.session_key 
      # s = Session.objects.get(pk=pk)
      # id=s.get_decoded()
      # request.session.modified = True
      # s = SessionStore()
      # s.create()
      # key=s.session_key
      # request.session['customer']=user.id
      # request.session['username']=user.username
      # response=HttpResponse("Manager")
      # response.set_cookie('name','ananya')
      # return response
      # request.session['fav_color'] = 'blue'
      # my_car = request.session['my_car']
      # request.session['my_car'] = 'mini'
      # request.session.set_test_cookie()
# def send_file(response):

#     img = open('Pictures/photo-1519996529931-28324d5a630e.avif', 'rb')

#     response = FileResponse(img)

#     return response
            # else:
            # return JsonResponse({'message': 'Access Denied'},status=401)