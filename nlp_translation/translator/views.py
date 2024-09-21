from django.shortcuts import render

 
from django.http import JsonResponse
from .translation_model import Translator

translator = Translator()

def translate_view(request):
    text = request.GET.get('text', '')
    translated_text = translator.translate(text)
    return JsonResponse({'translated_text': translated_text})
