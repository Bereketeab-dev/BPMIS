import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	return [
		{ "label": _("ID"), "fieldname": "name", "fieldtype": "Link", "options": "PMIS BOQ", "width": 120 },
		{ "label": _("Project"), "fieldname": "project", "fieldtype": "Link", "options": "PMIS Project", "width": 120 },
		{ "label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100 },
	]

def get_data(filters):
	return frappe.get_all("PMIS BOQ", fields=["name", "project", "status"])
