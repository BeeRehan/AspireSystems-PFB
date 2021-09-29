from re import A
from django.test import TestCase
from .form import PatientDetails
from appointment.form import ApprovalForm
from checkup.form import checklistForm

# Create your tests here.
class TestchecklistForm(TestCase):
    def test_Checkup_Details(self):
        form = checklistForm(
            data={
                "temprature": "test",
                "sugar_level": "test",
                "bp_level": "test",
                "advice": "test",
                "prescription": "test",
                "con_deseas": "test",
            }
        )
        self.assertTrue(form.is_valid())


class TestApprovalForm(TestCase):
    def test_ApprovalForm(self):
        form = ApprovalForm(data={"status": "approved"})
        self.assertTrue(form.is_valid())
