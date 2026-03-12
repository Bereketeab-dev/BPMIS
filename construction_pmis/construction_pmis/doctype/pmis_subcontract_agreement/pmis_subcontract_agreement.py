import frappe
from frappe.model.document import Document
from frappe import _

class PMISSubcontractAgreement(Document):
    def validate(self):
        total = 0
        for item in self.items:
            item.amount = (item.quantity or 0) * (item.rate or 0)
            total += item.amount
        self.contract_amount = total
