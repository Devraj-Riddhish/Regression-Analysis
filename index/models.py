from django.db import models

from django.db import models

class Boston_Data_1(models.Model):
	id = models.AutoField
	CRIM = models.FloatField(default=0)
	ZN = models.FloatField(default=0)
	INDUS = models.FloatField(default=0)
	CHAS= models.FloatField(default=0)
	NOX = models.FloatField(default=0)
	RM = models.FloatField(default=0)
	AGE = models.FloatField(default=0)
	DIS = models.FloatField(default=0)
	RAD = models.IntegerField(default=0)
	TAX = models.IntegerField(default=0)
	PTRATIO = models.FloatField(default=0)
	B = models.FloatField(default=0)
	LSTAT = models.FloatField(default=0)
	PRICE = models.FloatField(default=0)

class Red_Wine_data(models.Model):
	id = models.AutoField
	Fixed_Acidity = models.FloatField(default=0)
	volatile_Acidity = models.FloatField(default=0)
	Citric_Acid = models.FloatField(default=0)
	Residual_Sugar = models.FloatField(default=0)
	Chlorides = models.FloatField(default=0)
	Free_Sulfur_Dioxide = models.IntegerField(default=0)
	Total_Sulfur_Dioxide = models.IntegerField(default=0)
	Density = models.FloatField(default=0)
	Ph = models.FloatField(default=0)
	Sulphates = models.FloatField(default=0)
	Alcohol = models.FloatField(default=0)
	Quality = models.IntegerField(default=0)


class Black_Friday_data_1(models.Model):
	id = models.AutoField
	User_ID = models.IntegerField(default=0)
	Product_ID = models.CharField(default="" , max_length=10)
	Purchase = models.FloatField(default=0)

class Black_Friday_data_2(models.Model):
	id = models.AutoField
	User_ID = models.IntegerField(default=0)
	Product_ID = models.CharField(default="" , max_length=10)
	Gender = models.CharField(default="", max_length=10)
	Age = models.CharField(default=0, max_length=10)
	Occupation = models.IntegerField(default=0)
	City_Category = models.TextField(default="" , max_length=10)
	Stay_In_Current_City_Year = models.IntegerField(default=0)
	Marital_Status = models.IntegerField(default=0)
	Product_Category_1 = models.IntegerField(default=0)
	Product_Category_2 = models.IntegerField(default=0)
	Product_Category_3 = models.IntegerField(default=0)
	Purchase = models.CharField(default=0, max_length=10)

class Black_Friday_data_3(models.Model):
	id = models.AutoField
	User_ID = models.IntegerField(default=0)
	Product_ID = models.CharField(default="", max_length=10)
	Gender = models.CharField(default="" , max_length=10)
	Age = models.CharField(default=0, max_length=10)
	Occupation = models.IntegerField(default=0)
	City_Category = models.TextField(default="", max_length=10)
	Stay_In_Current_City_Year = models.CharField(default=0, max_length=10)
	Marital_Status = models.CharField(default=0, max_length=10)
	Product_Category_1 = models.IntegerField(default=0)
	Product_Category_2 = models.IntegerField(default=0)
	Product_Category_3 = models.IntegerField(default=0)

class Walmart_data_1(models.Model):
	id = models.AutoField
	Store = models.IntegerField(default=0)
	Date = models.DateField(default="")	
	Temperature = models.FloatField(default=0)	
	Fuel_Price = models.FloatField(default="")
	MarkDown1 = models.FloatField(default=0)	
	MarkDown2 = models.FloatField(default=0)
	MarkDown3 = models.FloatField(default=0)	
	MarkDown4 = models.FloatField(default=0)	
	MarkDown5 = models.FloatField(default=0)	
	CPI = models.FloatField(default=0)	
	Unemployment = models.FloatField(default=0, max_length=10)	
	IsHoliday = models.BooleanField(default="")

class Walmart_data_2(models.Model):
	id = models.AutoField
	Store = models.IntegerField(default=0)
	Type = models.CharField(default="" , max_length=10)	
	Size = models.IntegerField(default=0)

class Walmart_data_3(models.Model):
	id = models.AutoField
	Store = models.IntegerField(default=0)	
	Dept = models.IntegerField(default=0)
	Date = models.DateField(default="" )
	Weekly_Sales = models.FloatField()
	IsHoliday = models.BooleanField(default="")

class Walmart_data_4(models.Model):
	id = models.AutoField
	Store = models.IntegerField(default=0)	
	Dept = models.IntegerField(default=0)
	Date = models.DateField(default="" )
	IsHoliday = models.BooleanField(default="")