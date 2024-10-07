from django import forms

from argus_htmx.dateformat.constants import DATETIME_DEFAULT, DATETIME_FORMATS
from argus_htmx.incidents.constants import DEFAULT_PAGE_SIZE, ALLOWED_PAGE_SIZES
from argus_htmx.themes.utils import get_themes


_DATETIME_CHOICES = tuple((format, format) for format in DATETIME_FORMATS)
_PAGE_SIZE_CHOICES = tuple((ps, ps) for ps in ALLOWED_PAGE_SIZES)
_THEME_CHOICES = tuple((theme, theme) for theme in get_themes())


class PreferencesForm(forms.Form):
    theme = forms.ChoiceField(required=False, choices=_THEME_CHOICES)
    datetime_format = forms.ChoiceField(required=False, choices=_DATETIME_CHOICES)
    page_size = forms.TypedChoiceField(required=False, choices=_PAGE_SIZE_CHOICES, coerce=int)

    def clean_datetime_format(self):
        return self.cleaned_data.get("datetime_format", DATETIME_DEFAULT)

    def clean_page_size(self):
        return self.cleaned_data.get("page_size", DEFAULT_PAGE_SIZE)
