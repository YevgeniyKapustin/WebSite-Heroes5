from django.shortcuts import render

from cabbagesite.settings import kateusta_version, kateusta_link


def show_kateusta(request):
    context = {
        'title': 'Kateusta',
        'version': kateusta_version,
        'link': kateusta_link
    }
    return render(request, 'kateusta/kateusta.html', context)
