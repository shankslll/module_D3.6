from django import template
from datetime import datetime


register = template.Library()

bad_words = ['dsf', 'fds', 'som', 'fds', 'afs']


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.utcnow().strftime(format_string)


@register.filter()
def censor(value):
    low = value.lower()
    for i in bad_words:
        if i.find(low):
            low = value.replace(i[3:5:], '*' * len(i))
    return f'{low}'