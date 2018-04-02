# -*- coding: utf-8 -*-
from odoo import models, fields, api

class employee_vote(models.TransientModel):
	_name = 'employee.vote'
	_description = 'vote from employee'
	rating = fields.Integer('Rating')
	comments = fields.Text('Post your comments here..', required=True)
	