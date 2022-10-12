import json
from pymongo import MongoClient 
from gpiozero import Button
import sqops
import device
import serial
#import data from patients class and import data attribute
patient_standard = { "name": "","device_id":None, "bed_number": "","oxygen_rate":"0","is_alive":True }





client = MongoClient("mongodb+srv://admin:mazenelnoby1412@cluster0.095vb.mongodb.net/patients?retryWrites=true&w=majority")
#define patients database
db = client.test
db = client['patients']
stats_collection = db['patientsdata']
patients_collection = db['patientstracking']

#define archive database
arch_db=client['archives']
patients_archives = db['patients_archive']




core_device = device.Device(patients_collection,data_template=patient_standard)
#sqops.reset_stats(stats_collection) 
core_device.set_device(stats_collection)
timer=10
ser = serial.Serial()
ser.baudrate=115200
ser.port = 'COM6'
ser.open()
while True:
    data = int(ser.readline())
    #core_device.send_data(data)
    patients_collection.update_one({"is_alive":True},update={"$set":{'oxygen_rate':data}})
    print(data)
    if data == 0 and timer==0:
        sqops.set_death(patients_archives,stats_collection,patients_collection,False)
        break
    elif timer ==0:
        sqops.set_recovery(patients_archives,stats_collection,patients_collection,True)
        break
    timer -=1
    print(timer)
ser.close()

#print(x)


#TODO after weekend
#1-check the spelling of entries
#2-check the mongo atlas problem
#3-test the function
#4-start CODING the  RPI GPIO
#5-refactor if you can

#device initialization
#boolen of python maybe will make some issues in the backend

#patients_collection.insert_one(patient_standard)
#sqops.search_patient(patients_collection,'name','test')
#print(patient_standard.items())
#sqops.archive_patient(patients_archives,patients_collection,patient_standard['bed_number'])
# patientSetter = Button(17)
# patientTerminator = Button(4)
# patientRecoverd = Button(27)
#sqops.set_death(stats_collection,patients_collection,patient_standard['oxygen_rate'])
# while True:
#     pass

#x = collection.find_one()['activepatient']
