from .base import *


try:
    from .local import *
    live = False
    print 'testing locally'
except:
    live = True

if live == True:
    from .production import *
    print 'testing in production'
