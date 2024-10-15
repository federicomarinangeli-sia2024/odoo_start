from odoo import models, fields

class Ombrellone(models.Model):
    _name = 'umbrella.ombrellone'
    _description = 'Ombrellone'

    name = fields.Char(string='Nome Ombrellone', required=True)
    stabilimento_id = fields.Many2one('umbrella.stabilimento', string='Stabilimento', required=True, ondelete='cascade')
    numero_per_fila = fields.Integer(string='Numero Ombrelloni per Fila', default=1, required=True)
    numero_file = fields.Integer(string='Numero di File', default=1, required=True)
    prezzo = fields.Float(string='Prezzo per Giorno', required=True)
    disponibilita_ids = fields.One2many('umbrella.disponibilita', 'ombrellone_id', string='Disponibilità')
