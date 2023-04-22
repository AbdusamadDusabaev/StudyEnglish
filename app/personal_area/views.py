from django.views import View
from django.views.generic import ListView, DetailView

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .models import Word, WordDictionary, LearnedWord


class MainPageView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        amount_all_dictionaries = len(request.user.word_dictionaries.all())
        amount_all_learned_words = len(request.user.learned_words.all())
        amount_of_verbs = len(LearnedWord.objects.filter(user=request.user, part_of_speech="Verb").all())
        amount_of_adverbs = len(LearnedWord.objects.filter(user=request.user, part_of_speech="Adverb").all())
        amount_of_adjectives = len(LearnedWord.objects.filter(user=request.user, part_of_speech="Adjective").all())
        amount_of_nouns = len(LearnedWord.objects.filter(user=request.user, part_of_speech="Noun").all())
        percent_of_verbs = round(amount_of_verbs / amount_all_learned_words * 100, 2)
        percent_of_adverbs = round(amount_of_adverbs / amount_all_learned_words * 100, 2)
        percent_of_adjectives = round(amount_of_adjectives / amount_all_learned_words * 100, 2)
        percent_of_nouns = round(amount_of_nouns / amount_all_learned_words * 100, 2)
        context = {
            "amount_all_dictionaries": amount_all_dictionaries,
            "amount_all_learned_words": amount_all_learned_words,
            "percent_of_verbs": percent_of_verbs,
            "percent_of_adverbs": percent_of_adverbs,
            "percent_of_adjectives": percent_of_adjectives,
            "percent_of_nouns": percent_of_nouns,
        }
        return render(request=request, template_name="personal_area/main-page.html", context=context)


class DictionaryListView(ListView):
    template_name = "personal_area/dictionary-list.html"

    def get_queryset(self):
        queryset = WordDictionary.objects.filter(user=self.request.user).all()
        return queryset


class DictionaryDetailView(DetailView):
    model = WordDictionary
    template_name = "personal_area/dictionary-detail.html"
