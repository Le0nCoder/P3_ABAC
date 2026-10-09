#Politicas.py

def evaluar_acceso(solicitud):


    """
    PDP: evalua las politicasde autorización
    
    Retorna:
    
    ("PERMIT", motivo)
    ("DENY", motivo)
    """
    
    
    if not isinstance(solicitud, dict):
        return "DENY","Solicitud invalida"
    
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
        return "DENY","Periodo no vigente"
    
    #P03: Comprobar el periodo academico
    if environment.get("academic_period")!="Active":
        return "DENY",  "Dispositivo no registrado"
    
    #P04: Comprobar el dispositivo
    if environment.get("device_registered") is not True:
        return "DENY", "Dispositivo no registrado"
    
    
    #ACTIVIDAD 1
    #Comprobar que el recurso es calificaciones
    
    if resource.get("type")!="Calificaciones":
        return "DENY", "No hay calificaciones disponibles"
    
    #ACTTIVIDAD 2
    #REGLA PARA PROFESORES
    
    if subject.get("role")!= "Profesor": 
        return "PERMIT", "Solo personal autorizado"

    #Verificar grupos asignados y acción READ

    '''
    Si el campo de "group" esta vacio y la acción es de "Read" se deniega el acceso ya que no hay grupos asignados
    '''

    if subject.get("group")=="" and "action" == "Read":
        return "DENY", "No hay grupos asignados"

    #Actividad 3
    #Implementar regla para estudiantes

    if subject.get("role")== "Alumno" and subject.get("status"):
        return "PERMIT", "Acceso permitido para estudiantes activos"

    #Comparación subject id con owner id de la solicitud

    if subject.get("id") != resource.get("owner_id"):
        return "DENY", "Acceso denegado: propietario no coincide"

    #Actividad 4
    '''
    Asegurar que WRITE, DELETE y DOWNLOAD no sean permitidos por esta política
    '''

    if action in ["write","delete","download"] == True:
        return "DENY", "Acción denegada"

    #P07 Default Deny
    