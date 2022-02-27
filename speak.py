from speaklater import make_lazy_string, make_lazy_gettext, is_lazy_string
from threading import local

sval = 'Hello World'
string = make_lazy_string(lambda: sval)
print(string)
# lu'Hello World'
print(string.upper())
# u'HELLO WORLD'
sval = 'Hallo Welt'
print(string.upper())
# u'HALLO WELT'
l = local()
l.translations = {u'Yes': 'Ja'}
lazy_gettext = make_lazy_gettext(lambda: l.translations.get)
yes = lazy_gettext(u'Yes')
print(yes)
# Ja
l.translations[u'Yes'] = u'Si'
print(yes)
# Si

print(is_lazy_string(u'yes'))
# False
print(is_lazy_string(yes))
# True