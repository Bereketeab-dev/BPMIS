import frappe
from frappe.model.document import Document
from frappe import _

class PMISBOQ(Document):
    def validate(self):
        self.calculate_totals()

    def calculate_totals(self):
        total = 0
        for item in self.items:
            item.amount = (item.quantity or 0) * (item.rate or 0)
            total += item.amount
        self.total_amount = total
