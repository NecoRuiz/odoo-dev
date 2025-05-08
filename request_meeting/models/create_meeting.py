from odoo import models, fields

class CreateMeeting(models.Model):
    _name = 'solicitud.reunion'
    _description = 'Solicitud de Reunión'

    fecha = fields.Date(string='Fecha', required=True)
    hora = fields.Char(string='Hora', required=True)
    motivo = fields.Text(string='Motivo', required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada')
    ], string='Estado', default='pendiente', required=True)
    usuario_id = fields.Many2one('res.users', string='Usuario', readonly=True)

    def action_aceptar(self):
        for record in self:
            record.estado = 'aceptada'

    def action_rechazar(self):
        for record in self:
            record.estado = 'rechazada'

