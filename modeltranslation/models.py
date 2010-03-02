# -*- coding: utf-8 -*-
import sys

from django.conf import settings
from django.db import models

from modeltranslation.translator import translator

# Every model registered with the modeltranslation.translator.translator
# is patched to contain additional localized versions for every 
# field specified in the model's translation options.

# Import the project's global "translation.py" which registers model 
# classes and their translation options with the translator object. 
try: 
    import translation
except ImportError:
    sys.stderr.write("modeltranslation: Error can't find the file " \
                     "'translation.py' in your project root.\n")
    sys.exit(1)

# After importing all translation modules, all translation classes are 
# registered with the translator.
if settings.DEBUG:
    try:
        if sys.argv[1] in ('runserver', 'runserver_plus'):
            translated_model_names = ', '.join(
                t.__name__ for t in translator._registry.keys())
            print "modeltranslation: Registered %d models for translation " \
                  "(%s)." % (len(translator._registry),
                             translated_model_names)
    except IndexError:
        pass