{
    'name': 'Product Custom Fields',
    'version': '1.0',
    'category': 'Product',
    'summary': 'Aggiungi campi personalizzati ai prodotti',
    'description': """
        Modulo personalizzato per aggiungere campi 'Regione', 'Località', 
        e gestione ombrelloni alla scheda del prodotto e al sistema di ricerca.
    """,
    'author': 'Il tuo nome',
    'depends': ['product'],
    'data': [
        'views/product_template_view.xml',  # Include la vista form e i filtri di ricerca
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'post_init_hook': 'post_init_check',  # Richiamo del post_init_hook senza definizione della funzione qui
}
