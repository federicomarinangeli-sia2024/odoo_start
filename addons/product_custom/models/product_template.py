from odoo import models, fields

class BeachEstablishment(models.Model):
    _name = 'beach.establishment'
    _description = 'Beach Establishment'

    name = fields.Char(string='Stabilimento', required=True)
    region = fields.Many2one('res.country.state', string='Regione', required=True)
    city = fields.Char(string='Città o Località', required=True)
    concession_number = fields.Char(string='Numero Concessione')

    umbrella_count_per_row = fields.Integer(string='Numero Ombrelloni per Fila')
    row_count = fields.Integer(string='Numero di File')
    
    price_first_row = fields.Monetary(string='Prezzo Prima Fila', required=True)
    price_other_rows = fields.Monetary(string='Prezzo Altre File', required=True)
    
    currency_id = fields.Many2one('res.currency', string='Valuta', required=True)
    
    image = fields.Binary(string='Immagine Stabilimento')
    starting_price = fields.Monetary(string='A partire da', compute='_compute_starting_price')

    # Funzione per calcolare il prezzo di partenza
    def _compute_starting_price(self):
        for record in self:
            record.starting_price = record.price_other_rows
