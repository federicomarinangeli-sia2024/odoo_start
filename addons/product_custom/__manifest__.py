{
    'name': 'Product Custom Fields',
    'version': '1.0',
    'category': 'Product',
    'summary': 'Aggiungi campi personalizzati ai prodotti',
    'description': """
        Modulo personalizzato per aggiungere campi 'Regione' e 'Località' ai prodotti.
    """,
    'author': 'Il tuo nome',
    'depends': ['product'],  # Dipendenza dal modulo 'product'
    'data': [
        'views/product_template_view.xml',  # Include il file XML per le viste
    ],
    'installable': True,
    'auto_install': False,
}
