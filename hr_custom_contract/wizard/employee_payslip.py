from openerp.osv import fields, osv
from openerp.tools.translate import _
class validate_account_move_lines(osv.osv_memory):
    _name = "employee_payslip.hr.payslip"
    _description = "Recharge Fuel Cards"


    def hr_verify_sheet(self, cr, uid, ids, context=None):
        obj_move_line = self.pool.get('hr.payslip')
        move_ids = []
        if context is None:
            context = {}
        data_line = obj_move_line.browse(cr, uid, context['active_ids'], context)
        for line in data_line:
            self.compute_sheet(cr, uid, ids, context)
            self.write(cr, uid, ids, {'state': 'verify'}, context=context)
            print "Code **************************"
        return {'type': 'ir.actions.act_window_close'}
    def get_contract(self, cr, uid, employee, date_from, date_to, context=None):
        contract_obj = self.pool.get('hr.contract')
        clause = []
        clause_1 = ['&',('date_end', '<=', date_to),('date_end','>=', date_from)]
        clause_2 = ['&',('date_start', '<=', date_to),('date_start','>=', date_from)]
        clause_3 = ['&',('date_start','<=', date_from),'|',('date_end', '=', False),('date_end','>=', date_to)]
        clause_final =  [('employee_id', '=', employee.id),'|','|'] + clause_1 + clause_2 + clause_3
        contract_ids = contract_obj.search(cr, uid, clause_final, context=context)
        return contract_ids

    def compute_sheet(self, cr, uid, ids, context=None):
        obj_move_line = self.pool.get('hr.payslip')
        move_ids = []
        if context is None:
            context = {}
        payslip_type = obj_move_line.browse(cr, uid, context['active_ids'], context)
        slip_line_pool = self.pool.get('hr.payslip.line')
        sequence_obj = self.pool.get('ir.sequence')
        for payslip in payslip_type:
            number = payslip.number or sequence_obj.get(cr, uid, 'salary.slip')
            #delete old payslip lines
            old_slipline_ids = slip_line_pool.search(cr, uid, [('slip_id', '=', payslip.id)], context=context)
#            old_slipline_ids
            if old_slipline_ids:
                slip_line_pool.unlink(cr, uid, old_slipline_ids, context=context)
            if payslip.contract_id:
                #set the list of contract for which the rules have to be applied
                contract_ids = [payslip.contract_id.id]
            else:
                #if we don't give the contract, then the rules to apply should be for all current contracts of the employee
                contract_ids = self.get_contract(cr, uid, payslip.employee_id, payslip.date_from, payslip.date_to, context=context)
            lines = [(0,0,line) for line in self.pool.get('hr.payslip').get_payslip_lines(cr, uid, contract_ids, payslip.id, context=context)]
            self.write(cr, uid, [payslip.id], {'line_ids': lines, 'number': number,}, context=context)
        return True
        #print "Code **************************"
        return {'type': 'ir.actions.act_window_close'}