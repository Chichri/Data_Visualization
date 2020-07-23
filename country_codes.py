from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

#This short program returns the two digit code that pygal uses for countries
