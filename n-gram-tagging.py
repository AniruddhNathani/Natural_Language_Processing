# Concept of N-Gram tagging

from nltk.corpus import brown
import nltk

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

tagger = nltk.NgramTagger(len(brown_tagged_sents),train=brown_tagged_sents)
print(tagger.tag(nltk.word_tokenize('We are using the programming language Python')))

print(tagger.evaluate(brown_tagged_sents))
