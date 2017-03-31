from django.forms.utils import ErrorList
from .contact import ContactForm


def generate_contact_form_instance(data=None):
    return ContactForm(data, error_class=BootstrapErrorList)


class BootstrapErrorList(ErrorList):
    def __str__(self):
        return self.as_bootstrap_divs()

    def as_bootstrap_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(
            ['<div class="alert alert-danger">%s</div>' % e for e in self])
