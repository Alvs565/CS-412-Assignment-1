from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random

FDR_quotes = [
    "'The only thing we have to fear is fear itself.'",
    "'I ask you to judge me by the enemies I have made.'",
    "'A smooth sea never made a skilled sailor.'",
]

FDR_pics = [
    "FDR-pics/FDR-1944-Campaign-Portrait_(3x4_retouched,_cropped).jpg",
    "FDR-pics/fdr-portrait_square.avif",
    "FDR-pics/fdr3.avif",
]


# Create your views here.
def quote(request):
    template_name = "quotes/quote.html"
    # dictionary of context variables (key-value pairs)
    context = {
        "quote": FDR_quotes[random.randint(0, 2)],
        "picture": FDR_pics[random.randint(0, 2)],
    }
    return render(request, template_name, context)


def show_all(request):
    """Respond to the URL, delegate work to a template"""

    template_name = "quotes/show_all.html"
    # dictionary of context variables (key-value pairs)
    context = {
        "quote1": "'The only thing we have to fear is fear itself.'",
        "quote2": "'I ask you to judge me by the enemies I have made.'",
        "quote3": "'A smooth sea never made a skilled sailor.'",
        "img1": "FDR-pics/FDR-1944-Campaign-Portrait_(3x4_retouched,_cropped).jpg",
        "img2": "FDR-pics/fdr-portrait_square.avif",
        "img3": "FDR-pics/fdr3.avif",
    }
    return render(request, template_name, context)


def about(request):
    """Respond to the URL, delegate work to a template"""

    template_name = "quotes/about.html"
    # dictionary of context variables (key-value pairs)
    context = {
        "Bio": "Born in January 1882 in Hyde Park, NY. Franklin D. Rooselvelt grew up to become the 32nd president of the United States from 1933-1945. His leadership pulled America through the Great Depression and Second World War.",
        "Fun-fact": "Did you know: He created the modern social security system!",
    }
    return render(request, template_name, context)
