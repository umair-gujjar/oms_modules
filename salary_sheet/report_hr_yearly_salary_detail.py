#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
import datetime
from openerp.report import report_sxw
from openerp.osv import osv

class employees_yearly_salary_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(employees_yearly_salary_report, self).__init__(cr, uid, name, context)

        self.localcontext.update({
            'time': time,
            'get_employee': self.get_employee,
            'get_employee_detail': self.get_employee_detail,
            'cal_monthly_amt': self.cal_monthly_amt,
            'get_periods': self.get_periods,
        })

        self.context = context

    def get_periods(self, form):
        #self.mnths = []
#       Get start year-month-date and end year-month-date
        #first_year = int(form['date_from'][0:4])
        #last_year = int(form['date_to'][0:4])

        first_month = int(form['date_from'][5:7])
        monthDict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 
            7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

        month = monthDict[first_month] 
        print month   
        #last_month = int(form['date_to'][5:7])
        #no_months = (last_year-first_year) * 12 + last_month - first_month + 1
        #current_month = first_month
        #current_year = first_year

        #Get name of the months from integer
        #mnth_name = []
        #for count in range(0, no_months):
         #   m = datetime.date(current_year, current_month, 1).strftime('%b')
          #  mnth_name.append(m)
           # self.mnths.append(str(current_month) + '-' + str(current_year))
            #if current_month == 12:
                #current_month = 0
                #current_year = last_year
            #current_month = current_month + 1
        #for c in range(0, (12-no_months)):
            #mnth_name.append('')
            #self.mnths.append('')
      
        #return [mnth_name]
        return month

    def get_employee(self, form):
        employes = self.pool.get('hr.payslip').browse(self.cr,self.uid, form.get('employee_ids', []), context=self.context)
        return employes

    def get_employee_detail(self, obj):
        payslip_lines = self.cal_monthly_amt(obj.employee_id)
        return payslip_lines

    def cal_monthly_amt(self, employee_id):
        contract_obj = self.pool.get('hr.payslip').search(self.cr,self.uid, [('employee_id','=',employee_id.id)], context=self.context)
        res = self.pool.get('hr.payslip').browse(self.cr, self.uid, contract_obj)
        return res

class wrapped_report_payslip(osv.AbstractModel):
    _name = 'report.salary_sheet.report_hryearlysalary'
    _inherit = 'report.abstract_report'
    _template = 'salary_sheet.report_hryearlysalary'
    _wrapped_report_class = employees_yearly_salary_report

