from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from tablib import Dataset
from .models import Red_Wine_data, Boston_Data_1, Black_Friday_data_1, Black_Friday_data_2, Black_Friday_data_3, Walmart_data_1, Walmart_data_2, Walmart_data_3, Walmart_data_4
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
import re
# Create your views here.

def index(request):
	if 'user_login' in request.session:
		return render(request, 'index.html')
	else:
		return redirect('/login')

def login(request):
	if 'user_login' in request.session:
		return redirect('/index')
	else:
		return render(request, 'login.html')
def registration(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		username = request.POST['username']
		password = make_password(request.POST['password'])
		regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

		if len(fname) > 3 and len(lname) and len(username) and len(password):

			if fname.isnumeric() and lname.isnumeric():

				return render(request, 'registration.html', {'name_error':'Please Check Your name'})
			else:
				if re.match(regex, email):
					all_user = User.objects.filter(username=username)
					if all_user:
						return render(request, 'registration.html',{'username_error':'Please Check Your Username'})
					else:
						#data_store_user=User(first_name=fname, last_name=lname, email=email, username=username, password=password)
						#data_store_user.save()

						#auth.login(request, data_store_user)
						#request.session['user_login'] = 'user'
						return redirect('/index')
				else:
					return render(request, 'registration.html',{'email_error':'PLease Check Your Email'})
				
		else:
			return render(request, 'registration.html', {'len_error':'Please Keep your name and Username more than 3 characters'})
	else:
		return render(request, 'registration.html')
def about(request):
	if 'user_login' in request.session:
		return render(request, 'about.html')
	else:
		return redirect('/login')

def upload(request):
	if 'user_login' in request.session:
		if request.method == 'POST':
			upload_file = request.FILES['upload_data']
			upload_file_name = request.FILES['upload_data'].name
			file_name = upload_file_name.split('.')[0]
			if file_name == 'winequality-red':
				dataset = Dataset()
				import_data = dataset.load(upload_file.read(), format="xlsx")
				for x in import_data:
					data_stored = Red_Wine_data(Fixed_Acidity=x[0], volatile_Acidity=x[1], Citric_Acid=x[2], Residual_Sugar=x[3], Chlorides=x[4], Free_Sulfur_Dioxide=x[5], Total_Sulfur_Dioxide=x[6], Density=x[7], Ph=x[8], Sulphates=x[9], Alcohol=x[10], Quality=x[11])
					data_stored.save()
			elif file_name == 'catb_1':
				dataset = Dataset()
				import_data = dataset.load(upload_file.read(), format="xlsx")
				for x in import_data:
					data_stored = Black_Friday_data_1(User_ID=x[0], Product_ID=x[1], Purchase=x[2])
					data_stored.save()
			elif file_name == 'train':
				dataset = Dataset()
				import_data = dataset.load(upload_file.read(), format="xlsx")
				for x in import_data:
					data_stored = Black_Friday_data_2(User_ID=x[0], Product_ID=x[1], Gender=x[2], Age=x[3], Occupation=x[4], City_Category=x[5], Stay_In_Current_City_Year=x[6], Marital_Status=x[7], Product_Category_1=x[8], Product_Category_2=x[9], Product_Category_3=x[10], Purchase=x[11])
					data_stored.save()
			elif file_name == 'test':
				dataset = Dataset()
				import_data = dataset.load(upload_file.read(), format="xlsx")
				for x in import_data:
					data_stored = Black_Friday_data_3(User_ID=x[0], Product_ID=x[1], Gender=x[2], Age=x[3], Occupation=x[4], City_Category=x[5], Stay_In_Current_City_Year=x[6], Marital_Status=x[7], Product_Category_1=x[8], Product_Category_2=x[9], Product_Category_3=x[10])
					data_stored.save()
			elif file_name == 'features':
				dataset = Dataset()
				import_data = dataset.load(upload_file.read(), format="xlsx")
				for x in import_data:
					data_stored = Walmart_data_1(Store=x[0], Date=x[1], Temperature=x[2], Fuel_Price=x[3], MarkDown1=x[4], MarkDown2=x[5], MarkDown3=x[6], MarkDown4=x[7], MarkDown5=x[8], CPI=x[9], Unemployment=x[10], IsHoliday=x[11])
					data_stored.save()
			elif file_name == 'Store':
				dataset = Dataset()
				import_data = dataset.load(upload_file.read(), format="xlsx")
				for x in import_data:
					data_stored = Walmart_data_2(Store=x[0], Type=x[1], Size=x[2])
					data_stored.save()
			elif file_name == 'Train':
				dataset = Dataset()
				import_data = dataset.load(upload_file.read(), format="xlsx")
				for x in import_data:
					data_stored = Walmart_data_3(Store=x[0], Dept=x[1], Date=x[2], Weekly_Sales=x[3], IsHoliday=x[4])
					data_stored.save()
			elif file_name == 'Test':
				dataset = Dataset()
				import_data = dataset.load(upload_file.read(), format="xlsx")
				for x in import_data:
					data_stored = Walmart_data_4(Store=x[0], Dept=x[1], Date=x[2], IsHoliday=x[3])
					data_stored.save()
			else:
				file_name = 'Boston' 
				dataset = Dataset()
				import_data = dataset.load(upload_file.read(), format="xlsx")
				for x in import_data:
					data_stored = Boston_Data_1(CRIM=x[0], ZN=x[1], INDUS=x[2], CHAS=x[3], NOX=x[4], RM=x[5], AGE=x[6], DIS=x[7], RAD=x[8], TAX=x[9], PTRATIO=x[10], B=x[11], LSTAT=x[12], PRICE=x[13])
					data_stored.save()
			return redirect('/upload')
		else:
			return render(request, 'upload.html')
		return render(request, 'upload.html')
	else:
		return redirect('/login')

def show(request):
	if 'user_login' in request.session:
		show_redwine = Red_Wine_data.objects.all().order_by('-id')
		paginator = Paginator(show_redwine, 50)
		page = request.GET.get('page')
		print(page)
		try:
			show_redwine = paginator.page(page)
		except PageNotAnInteger:
			show_redwine = paginator.page(1)
		except EmptyPage:
			show_redwine = paginator.page(paginator.num_pages)
			return render(request, 'show.html', {'show_redwine': show_redwine})
		else:
			return redirect('/login')

def login_check(request):
	 	if request.method == 'POST':
	 		username = request.POST['username']
	 		password = request.POST['password']
	 		user = auth.authenticate(request,username=username, password=password)
 			if user is not None:
 				auth.login(request, user)
 				request.session['user_login'] = 'user'
 				return redirect('/index')
 			else:
 				return render(request, 'login.html', {'error': "Please Chekch Your Credentials"})
 		else:
 			return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	request.session.flush()
	return redirect('/login')


def boston_housing(request):
	boston_housing_data = Boston_Data_1.objects.all()
	paginator = Paginator(boston_housing_data, 50)
	page = request.GET.get('page')
	print(page)
	try:
		boston_housing_data = paginator.page(page)
	except PageNotAnInteger:
		boston_housing_data = paginator.page(1)
	except EmptyPage:
		boston_housing_data = paginator.page(paginator.num_pages)
	return render(request, 'show.html',{'boston_housing_data':boston_housing_data})

def black_friday_catb1(request):
	black_friday_catb = Black_Friday_data_1.objects.all()
	paginator = Paginator(black_friday_catb, 50)
	page = request.GET.get('page')
	print(page)
	try:
		black_friday_catb = paginator.page(page)
	except PageNotAnInteger:
		black_friday_catb = paginator.page(1)
	except EmptyPage:
		black_friday_catb = paginator.page(paginator.num_pages)
	return render(request, 'show.html',{'black_friday_catb':black_friday_catb})

def black_friday_train(request):
	black_friday_train = Black_Friday_data_2.objects.all()
	paginator = Paginator(black_friday_train, 50)
	page = request.GET.get('page')
	print(page)
	try:
		black_friday_train = paginator.page(page)
	except PageNotAnInteger:
		black_friday_train = paginator.page(1)
	except EmptyPage:
		black_friday_train = paginator.page(paginator.num_pages)
	return render(request, 'show.html',{'black_friday_train':black_friday_train})

def black_friday_test(request):
	black_friday_test = Black_Friday_data_3.objects.all()
	paginator = Paginator(black_friday_test, 50)
	page = request.GET.get('page')
	print(page)
	try:
		black_friday_test = paginator.page(page)
	except PageNotAnInteger:
		black_friday_test = paginator.page(1)
	except EmptyPage:
		black_friday_test = paginator.page(paginator.num_pages)
	return render(request, 'show.html',{'black_friday_test':black_friday_test})

def walmart_sales_features(request):
	walmart_sales_feature = Walmart_data_1.objects.all()
	paginator = Paginator(walmart_sales_feature, 50)
	page = request.GET.get('page')
	print(page)
	try:
		walmart_sales_feature = paginator.page(page)
	except PageNotAnInteger:
		walmart_sales_feature = paginator.page(1)
	except EmptyPage:
		walmart_sales_feature = paginator.page(paginator.num_pages)
	return render(request, 'show.html',{'walmart_sales_feature':walmart_sales_feature})

def walmart_sales_store(request):
	walmart_sales_store = Walmart_data_2.objects.all()
	paginator = Paginator(walmart_sales_store, 50)
	page = request.GET.get('page')
	print(page)
	try:
		walmart_sales_store = paginator.page(page)
	except PageNotAnInteger:
		walmart_sales_store = paginator.page(1)
	except EmptyPage:
		walmart_sales_store = paginator.page(paginator.num_pages)
	return render(request, 'show.html',{'walmart_sales_store':walmart_sales_store})

def walmart_sales_train(request):
	walmart_sales_train = Walmart_data_3.objects.all()
	paginator = Paginator(walmart_sales_train, 50)
	page = request.GET.get('page')
	print(page)
	try:
		walmart_sales_train = paginator.page(page)
	except PageNotAnInteger:
		walmart_sales_train = paginator.page(1)
	except EmptyPage:
		walmart_sales_train = paginator.page(paginator.num_pages)
	return render(request, 'show.html',{'walmart_sales_train':walmart_sales_train})

def walmart_sales_test(request):
	walmart_sales_test = Walmart_data_4.objects.all()
	paginator = Paginator(walmart_sales_test, 50)
	page = request.GET.get('page')
	print(page)
	try:
		walmart_sales_test = paginator.page(page)
	except PageNotAnInteger:
		walmart_sales_test = paginator.page(1)
	except EmptyPage:
		walmart_sales_test = paginator.page(paginator.num_pages)
	return render(request, 'show.html',{'walmart_sales_test':walmart_sales_test})

def Walmart_sales_analysis(request):
	return render(request, 'walmart_analysis.html')

def redwine_analysis(request):
	return render(request, 'redwine_analysis.html')

def black_friday_analysis(request):
	return render(request, 'black_friday_analysis.html')

def boston_housing_data_analysis(request):
	return render(request, 'boston_housing.html')