# -*- coding: utf-8 -*-
# from odoo import http


# class Al-itkan(http.Controller):
#     @http.route('/al-itkan/al-itkan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/al-itkan/al-itkan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('al-itkan.listing', {
#             'root': '/al-itkan/al-itkan',
#             'objects': http.request.env['al-itkan.al-itkan'].search([]),
#         })

#     @http.route('/al-itkan/al-itkan/objects/<model("al-itkan.al-itkan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('al-itkan.object', {
#             'object': obj
#         })
