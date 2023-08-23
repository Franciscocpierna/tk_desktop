from datetime import datetime #, timedelta 
#import datetime
data1="30/03/2023"
#datahoje=datetime.now()
#datahoje=datahoje.date()
#print(datahoje)
#datahoje= datetime.date.today() 
data = datetime.now()
datahoje=data 
ano = data.year
mes = data.month
dia = data.day
print(str(dia)+"/"+str(mes)+"/"+str(ano))
#print(datahoje.date())
#data3=datetime.strptime(data1,"%d/%m/%Y")
data3= data.strftime("%Y-%m-%d")
print(data3)
data4= datahoje.strftime("%d/%m/%Y")
#data4= datahoje.strftime("%Y-%m-%d")
if str(data3)>data4:
#if str(data3)>str(datahoje):
    print("dat1 é maior que data hoje")
else:
    print("dat1 é menor que data hoje")

if str(datahoje)>str(data3):
    print("datahoje é maior que data1")
else:
    print("datahoje é menor que data1")
data2=data1.split("/")
print(data2[0])
print (data2)
print(data2[0]+"/"+data2[1]+"/"+data2[2])    
print(data)
print(datahoje)

print(data3)
print(datahoje.strftime("%d/%m/%Y"))
#AND strftime('%Y', delivery_date) IN ('2016')
#dia=data2[0]
#mes=data2[1]
#ano=data2[2]
#print(dia)
#print(mes)
#print(ano)
#data3=data1.strftime("%y-%m-%d",data1)
#print(data3)
#data_em_texto = data_atual.strftime(‘%d/%m/%Y’)                