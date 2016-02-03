# -*- coding: utf-8 -*-

from openerp import models, fields, api
class hr_custom_contract(models.Model):
	_inherit = 'hr.contract'
	bonus = fields.Float('Bonus')
	loan_and_advance = fields.Float('Loan & Advance')
	medical_opd = fields.Float('Medical OPD')
	fuel_other = fields.Float('Fuel/others')
	overtime = fields.Float('Overtime')
	sr_other = fields.Float('SR/other')

class hr_custom_employee(models.Model):
	#_name = 'hr.custom.employee'
	_inherit = 'hr.employee'
	show_engineer = fields.Boolean('Is a Engineer ?')
	engineer = fields.Char('PEC #', size=64)
	blood_group = fields.Char('Blood Group', size=10)
	
