from . import models

def post_init_check(cr, registry):
    """Controlla se il modulo è installato correttamente."""
    from odoo import api, SUPERUSER_ID
    import logging

    _logger = logging.getLogger(__name__)

    env = api.Environment(cr, SUPERUSER_ID, {})
    if not env['ir.model'].search([('model', '=', 'product.template')]):
        _logger.error("Errore durante il caricamento del modulo: il modello 'product.template' non è stato trovato.")
    else:
        _logger.info("Il modulo 'product.template' è stato caricato correttamente.")
