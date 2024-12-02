# -*- coding: utf-8 -*-

# from server.odoo import models, fields , api
from odoo import models, fields, api

class UniversityClassroom(models.Model):
    _name = 'university.classroom'
    _description = 'university.classroom'
    _rec_name = 'classroom_name'

    classroom_name = fields.Char(
        string='name'
    )
    code = fields.Char()

    student_ids = fields.One2many(
        comodel_name='university.student',
        inverse_name='classroom_id'
    )

    instructor_ids = fields.Many2many(
        comodel_name='university.instructor',
        relation='class_inst_rel',
        column1='name',
        column2='f_name'
    )
    subject_ids = fields.Many2many(
        comodel_name='university.subject',
        relation='class_sub_rel',
        column1='classroom_name',
        column2='name'
    )

    num_ins = fields.Integer(
        string = "Number of Instructors",
        compute='comp_ins'
    )
    num_sub = fields.Integer(
        string = "Number of Subjects",
        compute='comp_sub'
    )
    num_stud = fields.Integer(
        string = "Number of Students",
        compute='comp_stud'
    )

    def comp_ins(self):
        self.num_ins = len(self.instructor_ids)

    def comp_sub(self):
        self.num_sub = len(self.subject_ids)

    def comp_stud(self):
        self.num_stud = len(self.student_ids)

    @api.onchange('subject_ids')
    def check_number_of_subjects(self):
        if len(self.subject_ids) > 3:
            return {'warning': {'title': 'warning',
                                'message':'The number of subjects should be less than 3'}}




