from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    fila_ombrelloni = fields.Integer(string='Numero di file')
    ombrelloni_per_fila = fields.Integer(string='Ombrelloni per fila')
    disponibilita_ombrelloni = fields.One2many(
        'umbrella.availability',
        'product_id',
        string='Disponibilità ombrelloni'
    )

class UmbrellaAvailability(models.Model):
    _name = 'umbrella.availability'
    _description = 'Disponibilità Ombrelloni'

    product_id = fields.Many2one('product.template', string='Ombrellone')
    data_disponibilita = fields.Date(string='Data di disponibilità')
    ombrelloni_disponibili = fields.Integer(string='Ombrelloni disponibili')
