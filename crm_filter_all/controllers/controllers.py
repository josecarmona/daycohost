# -*- coding: utf-8 -*-
# from odoo import http


# class CrmFilterAll(http.Controller):
#     @http.route('/crm_filter_all/crm_filter_all/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_filter_all/crm_filter_all/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_filter_all.listing', {
#             'root': '/crm_filter_all/crm_filter_all',
#             'objects': http.request.env['crm_filter_all.crm_filter_all'].search([]),
#         })

#     @http.route('/crm_filter_all/crm_filter_all/objects/<model("crm_filter_all.crm_filter_all"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_filter_all.object', {
#             'object': obj
#         })
