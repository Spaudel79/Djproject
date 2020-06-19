from .models import MainMenu, SubMenu

def data_pass(request):
    data={
        'menudata':MainMenu.objects.prefetch_related('submenu_set').all()
    }
    return data

