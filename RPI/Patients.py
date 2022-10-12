import datetime
import json
class Patient:
   def  __init__(self,name='',oxygen=100,is_mortal=False):
       self.name=name
       self.entry_date=datetime.date.today()
       self._oxygen=oxygen
       self._is_mortal=is_mortal
   
      

class Patient_Setter_Operations:
   def __init__(self,patient_object):
      self.patient=patient_object

   def set_name(self,patient_name=''): 
      self.patient.name=patient_name

   def set_mortality(self):
      self.patient._is_mortal=True


class Patient_Getter_Operations:
   def __init__(self,patient_object):
      self.patient=patient_object

   def get_name(self): 
      return self.patient.name

   def get_mortality(self):
      return self.patient._is_mortal

class json_class_converter:
   def __init__(self,patient_object):
      self.patient=patient_object

   def convert(self):
      pass