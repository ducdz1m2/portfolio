from django.shortcuts import render

# Create your views here.
def tools(request):
    return render(request, "tools/tools.html")


def word_counter(request):
    result = {}
    if request.method == 'POST':
        text = request.POST.get('text', '')
        result['word_count'] = len(text.split())
        result['char_count'] = len(text)
        result['sentence_count'] = text.count('.') + text.count('!') + text.count('?')
        result['input_text'] = text
    return render(request, 'tools/word_counter.html', {'result': result})