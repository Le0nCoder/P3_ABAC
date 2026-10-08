from politicas import evaluar_acceso
from solicitudes import solicitud_1, solicitud_2, solicitud_3, solicitud_4

def aplicar_decision(solicitud):
    """
    PEP: Aplica la decisión del PDP
    """

    decision, motivo = evaluar_acceso(solicitud)

    print("Usuario:", solicitud.get("subject", {}).get("id"))
    print("Decision:", decision)
    print("Motivo:", motivo)

    if decision == "PERMIT":
        print("Operacion Exitosa")
    else:
        print("Acceso Bloqueado")

    print("+" * 40)

aplicar_decision(solicitud_1)
aplicar_decision(solicitud_2)
aplicar_decision(solicitud_3)
aplicar_decision(solicitud_4)