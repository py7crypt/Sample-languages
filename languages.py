'''
  import get_wsgi_application for using settings of django
'''
from django.core.wsgi import get_wsgi_application
get_wsgi_application()

'''
  import gettext_lazy for translate the _(languages)
'''
from django.utils.translation import gettext_lazy as _
from django.utils.translation import activate

'''
  change activete with code i18n of language you need
'''
activate("el")


language = [
        ('af', _('Afrikaans')),
        ('ak', _('Akan')),
        ('sq', _('Albanian')),
        ('am', _('Amharic')),
        ('ar', _('Arabic')),
        ('hy', _('Armenian')),
        ('as', _('Assamese')),
        ('az', _('Azerbaijani')),
        ('bm', _('Bambara')),
        ('eu', _('Basque')),
        ('be', _('Belarusian')),
        ('bn', _('Bengali')),
        ('bs', _('Bosnian')),
        ('br', _('Breton')),
        ('bg', _('Bulgarian')),
        ('my', _('Burmese')),
        ('ca', _('Catalan')),
        ('km', _('Central Khmer')),
        ('ce', _('Chechen')),
        ('zh', _('Chinese')),
        ('kw', _('Cornish')),
        ('hr', _('Croatian')),
        ('cs', _('Czech')),
        ('da', _('Danish')),
        ('nl', _('Dutch')),
        ('dz', _('Dzongkha')),
        ('en', _('English')),
        ('eo', _('Esperanto')),
        ('et', _('Estonian')),
        ('ee', _('Ewe')),
        ('fo', _('Faroese')),
        ('fi', _('Finnish')),
        ('fr', _('French')),
        ('ff', _('Fulah')),
        ('gl', _('Galician')),
        ('lg', _('Ganda')),
        ('ka', _('Georgian')),
        ('de', _('German')),
        ('el', _('Greek')),
        ('gu', _('Gujarati')),
        ('ha', _('Hausa')),
        ('he', _('Hebrew')),
        ('hi', _('Hindi')),
        ('hu', _('Hungarian')),
        ('is', _('Icelandic')),
        ('ig', _('Igbo')),
        ('id', _('Indonesian')),
        ('ia', _('Interlingua')),
        ('ga', _('Irish')),
        ('it', _('Italian')),
        ('ja', _('Japanese')),
        ('jv', _('Javanese')),
        ('kl', _('Kalaallisut')),
        ('kn', _('Kannada')),
        ('ks', _('Kashmiri')),
        ('kk', _('Kazakh')),
        ('ki', _('Kikuyu')),
        ('rw', _('Kinyarwanda')),
        ('ky', _('Kirghiz')),
        ('ko', _('Korean')),
        ('ku', _('Kurdish')),
        ('lo', _('Lao')),
        ('lv', _('Latvian')),
        ('ln', _('Lingala')),
        ('lt', _('Lithuanian')),
        ('lu', _('Luba-Katanga')),
        ('lb', _('Luxembourgish')),
        ('mk', _('Macedonian')),
        ('mg', _('Malagasy')),
        ('ms', _('Malay')),
        ('ml', _('Malayalam')),
        ('mt', _('Maltese')),
        ('gv', _('Manx')),
        ('mi', _('Maori')),
        ('mr', _('Marathi')),
        ('mn', _('Mongolian')),
        ('ne', _('Nepali')),
        ('nd', _('North Ndebele')),
        ('se', _('Northern Sami')),
        ('no', _('Norwegian')),
        ('or', _('Oriya')),
        ('om', _('Oromo')),
        ('os', _('Ossetian')),
        ('pa', _('Panjabi')),
        ('fa', _('Persian')),
        ('pl', _('Polish')),
        ('pt', _('Portuguese')),
        ('ps', _('Pushto')),
        ('qu', _('Quechua')),
        ('ro', _('Romanian')),
        ('rm', _('Romansh')),
        ('rn', _('Rundi')),
        ('ru', _('Russian')),
        ('sg', _('Sango')),
        ('gd', _('Scottish Gaelic')),
        ('sr', _('Serbian')),
        ('sh', _('Serbo-Croatian')),
        ('sn', _('Shona')),
        ('ii', _('Sichuan Yi')),
        ('sd', _('Sindhi')),
        ('si', _('Sinhala')),
        ('sk', _('Slovak')),
        ('sl', _('Slovenian')),
        ('so', _('Somali')),
        ('es', _('Spanish')),
        ('sw', _('Swahili')),
        ('sv', _('Swedish')),
        ('tl', _('Tagalog')),
        ('tg', _('Tajik')),
        ('ta', _('Tamil')),
        ('tt', _('Tatar')),
        ('te', _('Telugu')),
        ('th', _('Thai')),
        ('bo', _('Tibetan')),
        ('ti', _('Tigrinya')),
        ('to', _('Tonga')),
        ('tr', _('Turkish')),
        ('tk', _('Turkmen')),
        ('ug', _('Uighur')),
        ('uk', _('Ukrainian')),
        ('ur', _('Urdu')),
        ('uz', _('Uzbek')),
        ('vi', _('Vietnamese')),
        ('cy', _('Welsh')),
        ('fy', _('Western Frisian')),
        ('wo', _('Wolof')),
        ('xh', _('Xhosa')),
        ('yi', _('Yiddish')),
        ('yo', _('Yoruba')),
        ('zu', _('Zulu')),
]