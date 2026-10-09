#Politicas.py


#Funcion principal
def evaluar_acceso(solicitud):


    """
    PDP: evalua las politicasde autorización
    
    Retorna:
    
    ("PERMIT", motivo)
    ("DENY", motivo)
    """
    
    #Se verifica que sea un diccionario
    if not isinstance(solicitud, dict):
        return "DENY","Solicitud invalida"


    #las 4 acciones principales de ABAC
    subject = solicitud.get("subject")
    resource = solicitud.get("resource")
    action = solicitud.get("action")
    environment = solicitud.get("environment")

    if not all([
        isinstance(subject, dict),
        isinstance(resource, dict),
        isinstance(environment, dict),
        isinstance(action, str),
    ]):
        return "DENY","Atributos insuficientes"
    
    
    
    #P01: Comprobar que la cuenta este activa
    if subject.get("status")!="Active":
        return "DENY","Cuenta inactiva"
    else:
        return "PERMIT", "Cuenta activa"


    #P03: Comprobar el periodo academico
    if environment.get("academic_period")!="Active":
        return "DENY",  "Fuera del periodo academico"
    else:
        return "PERMIT", "Dentro del periodo academico"
    
    #P04: Comprobar el dispositivo
    if environment.get("device_registered") is not True:
        return "DENY", "Dispositivo no registrado"
    else:
        return "PERMIT", "Dispositivo registrado"
    
    
    #ACTIVIDAD 1
    #Comprobar que el recurso es calificaciones
    
    if resource.get("type")!="Calificaciones":
        return "DENY", "No hay calificaciones disponibles"
    else:
        return "PERMIT", "Calificaciones disponibles"


    
    #ACTTIVIDAD 2
    #REGLA PARA PROFESORES
    
    if subject.get("role")!= "Profesor": 
        return "DENY", "Solo personal autorizado"
    else:
        return "PERMIT", "Profesor autorizado"



    #Verificar grupos asignados y acción READ
    '''
    Si el campo de "group" esta vacio y la acción es de "Read" se deniega el acceso ya que no hay grupos asignados
    '''
    if subject.get("group")=="" and "action" == "Read":
        return "DENY", "No hay grupos asignados"
    else:
        return "PERMIT", "Grupos asignados"



    #Actividad 3
    #Implementar regla para estudiantes

    if subject.get("role")== "Alumno" and subject.get("status")=="Active":
        return "PERMIT", "Acceso permitido para estudiantes activos"
    else:
            return "DENY", "Acceso denegado para estudiantes inactivos"



    #Comparación subject id con owner id de la solicitud

    if subject.get("id") != resource.get("owner_id"):
        return "DENY", "Acceso denegado: propietario no coincide"
    else:
        return "PERMIT", "Acceso permitido"


    #Actividad 4
    '''
    Asegurar que WRITE, DELETE y DOWNLOAD no sean permitidos por esta política
    '''

    if action in ["write","delete","download"] == True:
        return "DENY", "Acción denegada"
    else:
        return "PERMIT", "Acción permitida"

    #P07 Default Deny
    