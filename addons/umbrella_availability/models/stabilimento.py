from odoo import models, fields

class Stabilimento(models.Model):
    _name = 'umbrella.stabilimento'
    _description = 'Stabilimento Ombrelloni'

    name = fields.Char(string='Nome Stabilimento', required=True)
    regione = fields.Selection([
        ('toscana', 'Toscana'),
        ('lazio', 'Lazio'),
        ('liguria', 'Liguria'),
        ('sicilia', 'Sicilia'),
        ('puglia', 'Puglia'),
        ('campania', 'Campania'),
        ('sardegna', 'Sardegna'),
        ('calabria', 'Calabria'),
        ('basilicata', 'Basilicata'),
        ('abruzzo', 'Abruzzo'),
        ('marche', 'Marche'),
        ('friuli-venezia giulia', 'Friuli-Venezia Giulia'),
        ('veneto', 'Veneto'),
        ('molise', 'Molise'),
        ('emilia romagna', 'Emilia Romagna'),
    ], string='Regione', required=True)
    localita = fields.Char(string='Località', required=True)
