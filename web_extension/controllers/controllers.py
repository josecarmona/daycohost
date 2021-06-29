# -*- coding: utf-8 -*-
# from odoo import http


# class WebExtension(http.Controller):
#     @http.route('/web_extension/web_extension/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_extension/web_extension/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_extension.listing', {
#             'root': '/web_extension/web_extension',
#             'objects': http.request.env['web_extension.web_extension'].search([]),
#         })

#     @http.route('/web_extension/web_extension/objects/<model("web_extension.web_extension"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_extension.object', {
#             'object': obj
#         })
