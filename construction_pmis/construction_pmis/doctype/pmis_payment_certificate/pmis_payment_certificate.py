import frappe
from frappe.model.document import Document
from frappe import _

class PMISPaymentCertificate(Document):
    def validate(self):
        self.calculate_totals()

    def calculate_totals(self):
        total_claimed = 0
        total_certified = 0
        total_paid = 0
        for item in self.items:
            item.claimed_amount = (item.quantity or 0) * (item.rate or 0)
            total_claimed += item.claimed_amount
            total_certified += (item.certified_amount or 0)
            total_paid += (item.paid_amount or 0)

        self.total_claimed_amount = total_claimed
        self.total_certified_amount = total_certified
        self.total_paid_amount = total_paid
        self.balance_amount = self.total_certified_amount - self.total_paid_amount
