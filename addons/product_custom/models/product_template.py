# models/product_template.py
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    regione = fields.Selection(
        [
            ('liguria', 'Liguria'),
            ('toscana', 'Toscana'),
            ('lazio', 'Lazio'),
            ('campania', 'Campania'),
            ('calabria', 'Calabria'),
            ('sicilia', 'Sicilia'),
            ('sardegna', 'Sardegna'),
            ('puglia', 'Puglia'),
            ('basilicata', 'Basilicata'),
            ('marche', 'Marche'),
            ('abruzzo', 'Abruzzo'),
            ('molise', 'Molise'),
            ('veneto', 'Veneto'),
            ('friuli', 'Friuli-Venezia Giulia')
        ],
        string="Regione"
    )

    localita = fields.Char(string="Località")
