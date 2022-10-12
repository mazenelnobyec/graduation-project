import sqops
class Device:
    device_counter = 0
    def __init__(self,database_collection,data_template,device_id=device_counter+1):
        self.device_id=device_id
        self.database_collection = database_collection
        self.is_connected = False
       # self.connected_pins=connected_pins
        self.data_template=data_template
        pass

    def set_patient(self,bed_number):
        self.patient_connected=sqops.search_patient(self.database_collection,'bed_number',self.device_id)
    # def connection_testing(self):
    #     hardware_controller=Button(self.connected_pins['test'])
    #     hardware_controller.wait_for_active()
    #     #function to test connection
    #     pass


    # def connection_setting(self):
    #     hardware_controller=Button(self.connected_pins['set'])
    #     hardware_controller.wait_for_active()
    #     #function to implement patient
    #     pass
    def send_data(self,oxygen_rate):
        sqops.patient_update(self.database_collection,self.data_template,oxygen_rate)

    def set_device(self,stats_collection):
        sqops.add_patient(stats_collection)
        self.data_template['device_id']=self.device_id
        self.data_template['bed_number']=self.device_id
        sqops.patient_setup(self.database_collection,self.data_template)