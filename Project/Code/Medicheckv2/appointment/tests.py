from django.test import TestCase
from rest_framework.decorators import MethodMapper
from .form import ApprovalForm

# Create your tests here.
class TestAppoinment(TestCase):
    def test_renew_form_date_too_far_in_future(self):
        form = ApprovalForm()
        self.assertFalse(form.is_valid())
