# -*- coding: utf-8 -*-
{
    'name': "salary_sheet",

    'summary': "Addition of bonus , loan etc etc fields in Contract Form",

    'description': "Fields are added in the Contract Form",

    'author': "Tax Tech",
    'website': "http://www.taxtech.com",


    # any module necessary for this one to work correctly
    'depends': ['base','hr_payroll',],

    # always loaded
    'data': [
        'salary_report.xml',
        'views/report_hryearlysalary.xml',
        'views/report_hrsalarybymonth.xml',
        'wizard/hr_salary_employee_bymonth_view.xml',
        'wizard/hr_yearly_salary_detail_view.xml',
        
    ],
}
