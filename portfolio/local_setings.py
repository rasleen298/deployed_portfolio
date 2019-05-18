SECRET_KEY = 'dajwc*0d5@s!d)=gr40m@3)772o9)%e*2iy%g+ob+1f#0@+1cr(c#6'

ALLOWED_HOSTS = ['159.89.173.184']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfoliodb',
        'USER': 'djangohost',
        'PASSWORD':'djangohost@123',
        'HOST': 'localhost',
        'PORT':'5432',
    }
}
