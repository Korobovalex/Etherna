from django import template

register = template.Library()

banned_list = ['idiot', 'stupid', 'donkey']


@register.filter('censor')
def censor(sentence=''):
    new_sentence = ''

    for word in sentence.split():
        if word in banned_list:
            new_sentence += '* '
        else:
            new_sentence += word + ' '

        return new_sentence
