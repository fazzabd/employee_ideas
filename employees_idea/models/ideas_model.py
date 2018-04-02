# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Ideas(models.Model):
	_name = 'ideas'
	_description = 'Ideas'
	# _inherits = 
	title = fields.Char('Title', required=True)
	date_create = fields.Date('Create Date')
	date_deadline = fields.Date('Deadline', required=True)
	user_id=fields.Many2one('res.users', 'Employee')
	company=fields.Many2one('res.company','Company')
	department=fields.Many2one('hr.department','Department')
	# department=fields.Char('Department')
	idea_type=fields.Many2one('ideas.types','Idea Type')
	details=fields.Text('Details', required=True)
	state = fields.Selection([
		('new','New'),
		('wait','Waiting for Approval'),
		('approve','Approved'),
		('close','Closed'),
		], string='Status', readonly=True, copy=False, index=True,
		 track_visibility='onchange', default='new')

	@api.one
	def do_post_idea(self):
		self.write({'state':'wait'})
	
	@api.one
	def do_approve(self):
		self.write({'state':'approve'})

	@api.one
	def do_reject(self):
		self.write({'state':'close'})
	# @api.one
	# def do_give_vote(self):
	# 	self.write({'state':'wait'})
	@api.one
	def do_close(self):
		self.write({'state':'close'})
