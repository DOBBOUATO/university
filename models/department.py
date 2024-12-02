# -*- coding: utf-8 -*-

# from server.odoo import models, fields
# , api
from odoo import models, fields, api

class UniversityDepartment(models.Model):
    _name = 'university.department'
    _description = 'university.department'

    name = fields.Char()
    code = fields.Char()

    instructor_ids = fields.One2many(comodel_name='university.instructor', inverse_name='department_id')
    subject_ids = fields.One2many(comodel_name='university.subject', inverse_name='department_id')





