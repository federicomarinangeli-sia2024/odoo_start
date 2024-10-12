{
    'name': 'Product Custom Fields',
    'version': '1.0',
    'category': 'Product',
    'summary': 'Aggiungi campi personalizzati ai prodotti',
    'description': """
        Modulo personalizzato per aggiungere campi 'Regione' e 'Località' ai prodotti. 
        Questo modulo aggiunge campi personalizzati alla scheda del prodotto e al sistema di ricerca.
    """,
    'author': 'Il tuo nome',
    'depends': ['product'],  # Dipendenza dal modulo 'product'
    'data': [
        # Viste
        'views/product_template_view.xml',  # Include la vista form e i filtri di ricerca
    ],
    # Aggiunta di controlli extra per assicurare che il modulo funzioni correttamente
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'post_init_hook': 'post_init_check',  # Hook per verificare che il modulo si sia caricato correttamente
}

# Aggiungi questo nel file `__init__.py` del modulo per definire il post_init_hook:
def post_init_check(cr, registry):
    """Controlla se il modulo è installato correttamente."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    if not env['ir.model'].search([('model', '=', 'product.template')]):
        _logger.error("Errore durante il caricamento del modulo: il modello 'product.template' non è stato trovato.")
    else:
        _logger.info("Il modulo 'product.template' è stato caricato correttamente.")
