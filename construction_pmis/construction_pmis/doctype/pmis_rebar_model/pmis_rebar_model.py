import frappe
from frappe.model.document import Document
from frappe import _

class PMISRebarModel(Document):
    def validate(self):
        for item in self.items:
            item.total_weight = (item.cutting_length or 0) * (item.unit_weight or 0) * (item.number_of_bars or 0)
