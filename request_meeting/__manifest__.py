{
    'name': 'Solicitar Reunión',
    'version': '1.0',
    'summary': 'Permite solicitar reuniones desde una app externa',
    'depends': ['base'],
    'author': 'Neco Ruiz Crisóstomo',
    'category': 'Tools',
    'installable': True,
    'application': False,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'views/solicitud_reunion_views.xml'
],

}