#Manifest iniziale prdocut cust#{
 #   'name': 'Product Custom Fields',
  #  'version': '1.0',
   # 'category': 'Product',
    #'summary': 'Aggiungi campi personalizzati ai prodotti',
    #'description': """
        #Modulo personalizzato per aggiungere campi 'Regione' e 'Località' ai prodotti.
        #E gestire ombrelloni alla scheda del prodotto e al sistema di ricerca.
    #""",
    #'author': 'Il tuo nome',
    #'depends': ['product'],  
    #'data': [
        #'views/product_template_view.xml',  # Include la vista form e i filtri di ricerca
    #],
    #'installable': True,
    #'application': False,
    #'auto_install': False,
    #'license': 'LGPL-3',
    #'post_init_hook': 'post_init_check',  # Se necessario puoi mantenerlo o toglierlo se non serve
#}
{
    'name': 'Product Custom',
    'version': '1.0',
    'summary': 'Custom product module for beach establishments',
    'description': """
        This module customizes the product model to handle beach establishments
        with availability of umbrellas, different prices, and booking functionality.
    """,
    'category': 'Sales',
    'depends': ['base', 'product', 'website_sale'],
    'data': [
        'views/product_template_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
