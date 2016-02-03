# -*- coding: utf-8 -*-

from openerp import models, fields, api

class qualification_list(models.Model):
    _name = 'qualification.list'

    name = fields.Char(string='Name of Degree')
    list_code = fields.Integer(string='Qualification Code')

class institute_list(models.Model):
    _name = 'institute.list'

    name = fields.Char(string='Name of Institute')
    list_code = fields.Integer(string='Institute Code')

class year_list(models.Model):
    _name = 'year.list'

    name = fields.Char(string='Create Year')
    list_code = fields.Integer(string='Year Code')



class hr_custom_contract(models.Model):
	_inherit = 'hr.contract'
	bonus = fields.Float('Bonus')
	loan_and_advance = fields.Float('Loan & Advance')
	medical_opd = fields.Float('Medical OPD')
	fuel_other = fields.Float('Fuel/others')
	overtime = fields.Float('Overtime')
	sr_other = fields.Float('SR/other')
	employee_number = fields.Char('Employee ID')

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
	service_period = fields.Char('Service Period')
	last_working_day = fields.Char('Last Working Day')
	accounts_and_finance = fields.Char('Accounts & Finance')
	administration_and_hrm = fields.Char('Administration & HRM')
	it_dept = fields.Char('IT Department')
	site_settlement = fields.Char('Site Settlement')
	hse_dept = fields.Char('HSE Department')
	security_settlement = fields.Char('Security Settlement')
	others_if_any = fields.Char('Others (if any)')


	


class family_info(models.Model):
	_name = 'family_info'
	kid_name = fields.Char('Kid Name')
	sex = fields.Char('Sex')
	dob = fields.Date('Date of Birth')
	age = fields.Integer('Age')
	family_info_id = fields.Many2one('hr.employee','Family Information')


class employee_qualification(models.Model):
	_name = 'employee_qualification'
	qualification = fields.Many2one('qualification.list','Qualification')
	passing_year = fields.Many2one('year.list','Passing Year')
	institue = fields.Many2one('institute.list','Institue')
	employee_qualification_id = fields.Many2one('hr.employee','Employee Qualification')



class employee_certification(models.Model):
	_name = 'employee_certification'
	certification = fields.Char('Certification')
	year = fields.Many2one('year.list','Year')
	conducting_institute = fields.Many2one('institute.list','Conducting Institute')
	employee_certification_id = fields.Many2one('hr.employee','Employee Certification')


class employee_experience(models.Model):
	_name = 'employee_experience'
	company = fields.Char('Company')
	designation = fields.Char('Designation')
	experience_from = fields.Date('Experience From')
	experience_to = fields.Date('Experience To')
	total_experience_diff = fields.Integer('Total')
	employee_experience_id = fields.Many2one('hr.employee','Employee Experience')



