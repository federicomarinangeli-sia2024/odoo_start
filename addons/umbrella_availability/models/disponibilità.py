from odoo import models, fields

class Disponibilita(models.Model):
    _name = 'umbrella.disponibilita'
    _description = 'Disponibilità Ombrellone'
#Collegamento Many2one al modello Ombrellone. Ogni disponibilità si riferisce a un ombrellone specifico.
    ombrellone_id = fields.Many2one('umbrella.ombrellone', string='Ombrellone', required=True, ondelete='cascade')
#Date per rappresentare la data specifica per la quale l'ombrellone è disponibile o prenotato.
    data = fields.Date(string='Data', required=True)
# Campo booleano che indica se l'ombrellone è stato prenotato in quella data.
    prenotato = fields.Boolean(string='Prenotato', default=False)
