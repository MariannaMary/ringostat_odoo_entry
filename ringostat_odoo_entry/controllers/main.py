
from odoo import http

class RingostatRedirect(http.Controller):
    @http.route('/ringostat/link', auth='public', website=True)
    def index(self, **kw):
        return http.local_redirect('https://ringostat.com/ua/integration')
