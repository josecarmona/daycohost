# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectSubTask(http.Controller):
#     @http.route('/project_sub_task/project_sub_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_sub_task/project_sub_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_sub_task.listing', {
#             'root': '/project_sub_task/project_sub_task',
#             'objects': http.request.env['project_sub_task.project_sub_task'].search([]),
#         })

#     @http.route('/project_sub_task/project_sub_task/objects/<model("project_sub_task.project_sub_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_sub_task.object', {
#             'object': obj
#         })
