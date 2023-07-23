from django.test import TestCase, Client
from .models import *
# Create your tests here.
from .views import *
from django.urls import reverse
from django.http import HttpResponseRedirect

class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.adding = Laboratorio.objects.create(
            nombre = "Laboratorio",
            ciudad = "Chillan",
            pais = "Chile"
        )

    def test_fields(self):
        self.assertIsInstance(self.adding.id, int)
        self.assertIsInstance(self.adding.nombre, str)
        self.assertIsInstance(self.adding.ciudad, str)
        self.assertIsInstance(self.adding.pais.name, str)
        self.assertIsInstance(self.adding.pais, object)

    
    def test_nombre_correcto(self):
        '''
        En el setup se creo un laboratorio, ahora al consultar debe existir un laboratorio
        Se compara que el nombre del Laboratorio es igual a la creacion en setup
        '''
        labs = Laboratorio.objects.all()
        self.assertEqual(labs.count(), 1)
        self.assertNotEqual(labs.count(), 2)
        self.assertEqual(self.adding.nombre, "Laboratorio")
        self.assertEqual(labs.first().nombre,"Laboratorio")

    def test_crear_retorna_status_200(self):
        '''
        Envio una petecion /laboratorio/create
        retornar status 200 y crea un laboratorio
        '''
        response = self.client.post("/laboratorio/add", {
            "nombre": "Laboratorio",
            "ciudad": "Chillan",
            "pais": "Chile"
        }, follow=True)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'add_laboratorio.html')

    def test_form_submission_redirect(self):
    # Create a URL to the view where the form is submitted (replace 'your_view_name' with the actual view name)
        client = Client()
        form_data = {
            "nombre": "Laboratorio 3",
            "ciudad": "Chillan",
            "pais": "Chile"
        }

        get_response = client.get('/laboratorio/add', {}, True)
        post_response = client.post(reverse('mostrar_laboratorio'), data=form_data, follow=True)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(post_response.status_code, 200)

class DirectorModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        laboratorio = Laboratorio(nombre="Laboratorio 1", ciudad="ciudad 1", pais="CL")
        laboratorio.save()
        self.adding = DirectorGeneral.objects.create(
            nombre = "Name example",
            laboratorio = laboratorio,
            especialidad = "Especialidad 1",
            )
        
    def test_fields(self):
        self.assertIsInstance(self.adding.id, int)
        self.assertIsInstance(self.adding.nombre, str)
        self.assertIsInstance(self.adding.laboratorio.nombre, str)
        self.assertIsInstance(self.adding.laboratorio, object)
        self.assertIsInstance(self.adding.especialidad, str)

class ProductoModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.adding = Producto.objects.create(
            nombre = "Name example",
            laboratorio = "Professional certificate",
            especialidad = "Especialidad",
            f_fabricacion = "200-02-03",
            p_costo = 1000,
            p_venta = 1500
            )
