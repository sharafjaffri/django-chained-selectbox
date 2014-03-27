from widgets import ChainedSelect, ChainedSelectMultiple
from django_filters.filters import Filter
from django.forms import ChoiceField, MultipleChoiceField


class ChainedChoiceField(ChoiceField):
    def __init__(self, parent_field, ajax_url, choices=None, *args, **kwargs):

        self.parent_field = parent_field
        self.ajax_url = ajax_url
        self.choices = choices or (('', '--------'), )
        self.widget = ChainedSelect(parent_field=parent_field,
                                    ajax_url=ajax_url)
        defaults = {'widget': self.widget}
        defaults.update(kwargs)

        super(ChainedChoiceField, self).__init__(choices=self.choices, *args, **defaults)


    def valid_value(self, value):
        "Dynamic choices so just return True for now"
        return True


class ChainedMultipleChoiceField(MultipleChoiceField):
    def __init__(self, parent_field, ajax_url, choices=None, *args, **kwargs):
        self.parent_field = parent_field
        self.ajax_url = ajax_url
        self.choices = choices or ()
        self.widget = ChainedSelectMultiple(parent_field=parent_field,
                                            ajax_url=ajax_url)
        defaults = {'widget': self.widget}
        defaults.update(kwargs)

        super(ChainedMultipleChoiceField, self).__init__(choices=self.choices, *args, **defaults)


    def valid_value(self, value):
        "Dynamic choices so just return True for now"
        return True

class ChainedChoiceFilter(Filter):
    field_class = ChainedChoiceField
