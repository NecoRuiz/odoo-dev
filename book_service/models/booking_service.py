from odoo import models, fields

class ReservaServicio(models.Model):
    _name = 'reserva.servicio'
    _description = 'Reserva de Servicio'

    tipo_servicio = fields.Char(string='Tipo de Servicio', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    horas = fields.Integer(string='Horas', required=True)
    ubicacion = fields.Char(string='Ubicación', required=True)
    precio = fields.Float(string='Precio', required=True)
    usuario_id = fields.Many2one('res.users', string='Usuario', required=True)
