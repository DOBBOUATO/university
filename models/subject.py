# -*- coding: utf-8 -*-

# from server.odoo import models, fields
# , api
from odoo import models, fields

class UniversitySubject(models.Model):
    _name = 'university.subject'
    _description = 'university.subject'

    name = fields.Char()
    code = fields.Char()

    department_id = fields.Many2one(comodel_name='university.department')

    instructor_ids = fields.Many2many(comodel_name='university.instructor',
                                      relation='sub_inst_rel',
                                      column1='name',
                                      column2='f_name')





