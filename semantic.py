import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

'''
Cat and monkey have the highest similarity, most likely because they're both animals. It's interesting as a human might 
score monkey and banana closer than monkey and cat in casual conversations depending on context.
Cat and banana have the least similarity despite both words having some similarity to monkey. This makes sense as cats 
do not eat fruit. Interestingly both words are scored as having more similarity with monkey than with each other. It 
seems the similarity between two words does not carry over when comparing each to a third word.
'''
#My own examples:
example1 = nlp("butterfly")
example2 = nlp("plane")
example3 = nlp("bird")
example4 = nlp("fly")
print()
print(example1.similarity(example2))
print(example3.similarity(example2))
print(example3.similarity(example1))
print(example4.similarity(example1))
print(example4.similarity(example2))
print(example4.similarity(example3))

'''
In my examples I compared an insect, a bird and a plane. As expected the two living things had the highest similarity. 
Both birds and butterflies are living things and small while planes are neither. I decided to add the insect fly to see 
what effect that had but interestingly the other meaning of fly might be used here. There's a higher correlation between
plane and fly than fly and any other word and there is very little similarity between butterfly and fly. This highlights
the pitfalls and difficulties of deciphering intent. I meant fly as in the insect but the word has many meanings and the 
program has to make a guess as to which meaning is appropriate.
'''

# I'm now going to run 'en_core_web_sm' to see the difference+
nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''
The first thing I see is that it gives me a red user warning:
'UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will 
be based on the tagger, parser and NER, which may not give useful similarity judgements.'

This tells me immediately that sm is less accurate than md. 
The scores for md were:
Cat and monkey 59%
banana and monkey 40%
banana and cat 22%

With sm it's cat and monkey are 67%, banana and monkey are 72% and banana and cat are 68% similar. This answer is a lot
less valuable than with md as all the words are now considered similar, there's only 1% difference between the first and
third comparisons and 5% between the lowest and highest similarities. Interestingly, banana and monkey are now closer 
than before but cat and banana being 68% similar makes no sense. Banana and monkey both have 6 letters and share a letter
in common. All three words are proper nouns as well. This may explain why sm puts them close together in similarity as it
is only looking at each word's properties and not how likely they are to be used together. In this scenario, cat and monkey
having the lowest score makes sense as they don't share any letters unlike cat and banana.


'''