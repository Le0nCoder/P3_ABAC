#Solicitudes python


#Prueba de la primera solicitud

solicitud_1 ={
    "subject":{
        "id" : "P001",
        "role": "Profesor",
        "status": "Active",
        "assigned_groups": ["5A","5B"]
    },
    
    "resource":{
        "type":"Calificaciones",
        "group":"5A",
        "owner_id":"None",
    },
    
    "action":"Read",
    "environment":{
        "academic_period":"Active",
        "device_registered":True,
    }
}

#Prueba de la segunda solicitud

solicitud_2 ={
    "subject":{
        "id" : "P002",
        "role": "Profesor",
        "status": "Inactive",
        "assigned_groups": ["5A"]
    },
    
    "resource":{
        "type":"Calificaciones",
        "group":"5A",
        "owner_id":"None",
    },
    
    "action":"Read",
    "environment":{
        "academic_period":"Active",
        "device_registered":True,
    }
}


solicitud_3 ={
    "subject":{
        "id" : "P003",
        "role": "Alumno",
        "status": "Inactive",
        "assigned_groups": [""]
    },
    
    "resource":{
        "type":"Calificaciones",
        "group":"5A",
        "owner_id":"None",
    },
    
    "action":"Read",
    "environment":{
        "academic_period":"Inactive",
        "device_registered":False,
    }
}
    
solicitud_4 ={
    "subject":{
        "id" : "P004",
        "role": "Alumno",
        "status": "Active",
        "assigned_groups": [""]
    },
    
    "resource":{
        "type":"Calificaciones",
        "group":"5A",
        "owner_id":"None",
    },
    
    "action":"Read",
    "environment":{
        "academic_period":"Active",
        "device_registered":True,
    }
}