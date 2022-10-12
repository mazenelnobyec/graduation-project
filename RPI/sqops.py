#Smart Quarntine Operationsjg
#patients data gathering
def reset_stats(stats_collection):
   # values = stats_collection.find()
    stats_collection.update_one({},{'$set':{'activepatient':0,'totalpatients':0,'recovered':0,'deathcount':0}})
    
def add_patient(patient_data_collection):
    x = patient_data_collection.find_one()['activepatient']
    patient_data_collection.update_one({'activepatient': x}, {'$inc': {'activepatient': 1}})
    patient_data_collection.update_one({'totalpatients': x}, {'$inc': {'totalpatients': 1}})
    pass

def recoverd_patient(patient_stats_collection):
    x = patient_stats_collection.find_one()['recovered']
    y = patient_stats_collection.find_one()['activepatient']

    patient_stats_collection.update_one({'recovered': x}, {'$inc': {'recovered': 1}})
    patient_stats_collection.update_one({'activepatient': y}, {'$inc': {'activepatient': -1}})

    pass    


def terminate_patient(patient_data_collection):
    x = patient_data_collection.find_one()['deathcount']
    y = patient_data_collection.find_one()['activepatient']
    patient_data_collection.update_one({'deathcount': x}, {'$inc': {'deathcount': 1}})
    patient_data_collection.update_one({'activepatient': y}, {'$inc': {'activepatient': -1}})

    pass

#patients tracking operations
def search_patient(collection,key='',data=''):
    result = collection.find_one({key:data})
    return result
#databases collection migrations

def archive_patient(archive_collection,patient_tracking,patient_data):
    patient = search_patient(patient_tracking,key="is_alive",data = patient_data)
    archive_collection.insert_one(patient)
    patient_tracking.delete_one(patient)

#device and senors opertaions

def set_death(archive_collection,stats_collection,patient_tracking,patient_data):
    inversion = {"$set":{"is_alive":False}}
   #patient=search_patient(patient_tracking,key="device_id",data=patient_data)
    patient_tracking.update_one({"is_alive":True},inversion)
    terminate_patient(stats_collection)
    archive_patient(archive_collection,patient_tracking,patient_data)
    pass
def set_recovery(archive_collection,stats_collection,patient_tracking,patient_data):
    recoverd_patient(stats_collection)
   #patient=search_patient(patient_tracking,key="device_id",data=patient_data)
    archive_patient(archive_collection,patient_tracking,patient_data)
    pass
def patient_setup(patient_tracking,data_template):
    patient_tracking.insert_one(data_template)

def patient_update(patient_tracking,data_template,oxygen_rate):
    value = {"$set":{"oxygen_rate":oxygen_rate}}
    patient_tracking.update_one(data_template,value)