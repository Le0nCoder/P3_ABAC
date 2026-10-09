import copy
import unittest

from solicitudes import solicitud_1
from politicas import evaluar_acceso

class TestABAC(unittest.TestCase):

    def setUp(self):
        self.solicitud = copy.deepcopy(solicitud_1)

    def test_profesor_autorizado(self):
        decision,_ = evaluar_acceso(self.solicitud)
        self.assertEqual(decision, "PERMIT")

    def test_cuenta_inactiva(self):
        self.solicitud["subject"]["status"] = "Inactive"
        decision,_ = evaluar_acceso(self.solicitud)
        self.assertEqual(decision, "DENY")

    def test_grupo_no_asignado(self):
        self.solicitud["resource"]["group"] = "9Z"
        decision,_ = evaluar_acceso(self.solicitud)
        self.assertEqual(decision, "DENY")

    def test_accion_no_permitida(self):
        self.solicitud["action"] = "Delete"
        decision,- = evaluar_acceso(self.solicitud)
        self.assertEqual(decision, "DENY")

    def test_atributo_faltante(self):
        del sef.solicitud["subject"]["assigned_groups"]
        decision,_ evaluar_acceso(self.solicitud)
        self.assertEqual(decision, "DENY")

if __name__ == "__main__":
    unittest.main()