__author__ = 'wadehuang'

def get_next_url(path):
    if path.find('next') > 0:
        return path.split('next=')[1]
    else:
        return '/index'