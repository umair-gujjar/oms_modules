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
	family_id = fields.One2many('family_info','family_info_id',string='Details')
	spouse_name = fields.Char('Spouse Name')
	s_dob = fields.Date('Date of Birth')
	s_contact = fields.Char('Spouse Contact')
	s_cnic = fields.Char('CNIC #')
	first_email = fields.Char('Primary Email')
	second_email = fields.Char('Secondary Email')
	email_password = fields.Char('Password')
	employee_qualify_id = fields.One2many('employee_qualification','employee_qualification_id',string='Details')
	employee_certify_id = fields.One2many('employee_certification','employee_certification_id',string='Details')
	total_experience = fields.Integer('Total Experience  :  Years:')
	employee_expert_id = fields.One2many('employee_experience','employee_experience_id',string='Details')

	


class family_info(models.Model):
	_name = 'family_info'
	kid_name = fields.Char('Kid Name')
	sex = fields.Char('Sex')
	dob = fields.Date('Date of Birth')
	age = fields.Integer('Age')
	family_info_id = fields.Many2one('hr.employee','Family Information')


class employee_qualification(models.Model):
	_name = 'employee_qualification'
	qualification = fields.Char('Qualification')
	passing_year = fields.Char('Passing Year')
	institue = fields.Date('Institue')
	employee_qualification_id = fields.Many2one('hr.employee','Employee Qualification')



class employee_certification(models.Model):
	_name = 'employee_certification'
	certification = fields.Char('Certification')
	year = fields.Char('Year')
	conducting_institute = fields.Date('Conducting Institute')
	employee_certification_id = fields.Many2one('hr.employee','Employee Certification')


class employee_experience(models.Model):
	_name = 'employee_experience'
	company = fields.Char('Company')
	designation = fields.Char('Designation')
	experience_from = fields.Date('Experience From')
	experience_to = fields.Date('Experience To')
	employee_experience_id = fields.Many2one('hr.employee','Employee Experience')