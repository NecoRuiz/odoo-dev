{
    'name': 'Reservar Servicios',
    'version': '1.0',
    'summary': 'Permite reservar servicios desde una app externa',
    'depends': ['base'],
    'author': 'Neco Ruiz Crisóstomo',
    'category': 'Tools',
    'installable': True,
    'application': False,
    'auto_install': False,
    'data': [
    'views/booking_service_views.xml',
    'security/ir.model.access.csv',
],
}
