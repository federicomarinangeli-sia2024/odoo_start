from odoo import http
from odoo.http import request

class UmbrellaAvailabilitySearch(http.Controller):
    
    @http.route('/umbrella/shop', type='http', auth="public", website=True)
    def shop_search(self, locality=None, date=None, **kwargs):
        domain = []
        
        if locality:
            domain.append(('locality', '=', locality))
        if date:
            domain.append(('availability_date', '=', date))
        
        umbrellas = request.env['product.template'].sudo().search(domain)
        
        return request.render('umbrella_availability.umbrella_search_results', {
            'umbrellas': umbrellas,
            'locality': locality,
            'date': date,
        })
