from django.urls import path
from Adopciones.views import(
    Home,
    MascotasCreateView,
    ListaMascotas,
    DetallesMascotas,
    user,
    listaUsuarios,
    mostrarUsuario,
    eliminarUsuario,
    editarUsuario,
    enviar,
    DetalleMascota_pdf,
    ListaMascotas_admin,
    eliminarMascota,
    ActualizarDatos_Mascotas,
)
app_name = 'Adopciones'
urlpatterns = [
    path('', Home, name = "index"),
    path('user/crearMascota/',MascotasCreateView,name ="crearMascota"),
    path('mascotas/',ListaMascotas,name ="lista_mascotas"),
    path('<int:myID>/',DetallesMascotas,name ="detalles"),
    path('user/', user, name="operacionesUsuario"),
    path('usuarios/', listaUsuarios, name='listaUsuarios'),
    path('usuarios/<int:myID>/', mostrarUsuario, name='detallesUsuario'),
    path('usuarios/<int:myID>/eliminar', eliminarUsuario, name='eliminarUsuario'),
    path('usuarios/<int:myID>/editar', editarUsuario, name='editarUsuario'),
    path('<int:myID>/enviar',enviar),
    path('<int:myID>/pdf/',DetalleMascota_pdf.as_view(),name = "detalles_pdf"),
    path('user/ListaMascotas/',ListaMascotas_admin),
    path('user/ListaMascotas/<int:myID>/eliminar',eliminarMascota),
    path('user/ListaMascotas/<int:myID>/editar',ActualizarDatos_Mascotas)
] 