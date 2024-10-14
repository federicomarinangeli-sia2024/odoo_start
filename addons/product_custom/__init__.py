from . import models

#def post_init_check(cr, registry):
    #"""Controlla se il modulo è installato correttamente."""
    #from odoo import api, SUPERUSER_ID
    #import logging

#    _#logger = logging.getLogger(__name__)

    #env = api.Environment(cr, SUPERUSER_ID, {})
    #if not env['ir.model'].search([('model', '=', 'product.template')]):
#        _#logger.error("Errore durante il caricamento del modulo: il modello 'product.template' non è stato trovato.")
    #else:
#        _#logger.info("Il modulo 'product.template' è stato caricato correttamente.")
#nascondiamo la funzione definita per il manifest originale