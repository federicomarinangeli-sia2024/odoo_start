from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Campo per la selezione della regione con un menu a tendina
    regione = fields.Selection([
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
    ], string="Regione")

    # Campo per inserire la località
    localita = fields.Char(string="Località")

    # Nuovi campi per la gestione degli ombrelloni
    fila_ombrelloni = fields.Integer(string='Numero di file')
    ombrelloni_per_fila = fields.Integer(string='Ombrelloni per fila')
    disponibilita_ombrelloni = fields.One2many(
        'umbrella.availability',
        'product_id',
        string='Disponibilità ombrelloni'
    )
