import re
import random

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('Yes im new this is my first version and i\'m waiting to be upgraded', ['new', 'first'], single_response=True)
    response('I am a bot and this is my first version and i\'m waiting to be upgraded', ['tell', 'me', 'about', 'yourself'], required_words=['tell', 'yourself'])
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how', 'you'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Im ChatBot v0.1', ['what', 'is', 'your', 'name'], required_words=['your', 'name'])
    response('Dizon will beat you', ['gay', 'lgbtq'], single_response=True)
    response('Yes Sir, That\'s my Human!', ['nega', 'sex'], single_response=True)
    response('God will not forgive a low life', ['murder', 'rape', 'kill', 'noob', 'fack', 'shit', 'bitch', 'dead'], single_response=True)
    response('I don\'t understand that. Can you rephrase?', ['confused', 'don\'t', 'understand'], required_words=['don\'t', 'understand'])
    response('I love learning new things!', ['learn', 'knowledge'], required_words=['learn'])
    response('Sorry, I didn\'t catch that. Can you repeat?', ['repeat'], single_response=True)
    response('I\'m a bot created by a team of developer in BSIT - 2102', ['who', 'you', 'are'], required_words=['who', 'you', 'are'])
    response('I enjoy chatting with you!', ['chat', 'talk', 'conversation'], required_words=['chat'])
    response('That sounds interesting! Tell me more.', ['tell', 'more', 'about'], required_words=['tell', 'more'])
    response('I\'m here to help you!', ['help', 'support'], required_words=['help'])
    response('How can I assist you today?', ['assist', 'help', 'support'], required_words=['assist'])
    response('I appreciate your feedback!', ['feedback', 'suggestion'], required_words=['feedback'])
    response('Let\'s focus on the positive!', ['negative', 'positive', 'attitude'], required_words=['positive'])
    response('I\'m always learning and evolving.', ['evolve', 'learn', 'improve'], required_words=['evolve'])
    response('What\'s your favorite hobby?', ['favorite', 'hobby'], required_words=['favorite', 'hobby'])
    response('Do you believe in aliens?', ['aliens', 'ufo', 'extraterrestrial'], required_words=['aliens'])
    response('I love exploring new ideas!', ['explore', 'ideas'], required_words=['explore'])
    response('I was created by a team of developers: Aj, Joshua, Dominic, Mj, Paolo, and Carl.', ['created', 'creator', 'who', 'you'], required_words=['created', 'you'])
    response('My creators are talented individuals: Aj, Joshua, Dominic, Mj, Paolo, and Carl.', ['who', 'are', 'is' 'created', 'you'], required_words=['who', 'created', 'you'])
    response('The brilliant minds behind my creation are Aj, Joshua, Dominic, Mj, Paolo, and Carl.', ['who', 'create', 'are', 'is' 'you'], required_words=['who', 'create', 'you'])
    response('The developers of me are Aj, Joshua, Dominic, Mj, Paolo, and Carl.', ['developer', 'developt', 'developers'], single_response=True )
    response('Aj is a student in BSIT 2102 and love to watch ( ͡° ͜ʖ ͡°) you know what it is.', ['who', 'is', 'aj'], required_words=['who', 'aj'])
    response('Aj is currently enrolled in BSIT 2102.', ['aj', 'student', 'BSIT 2102'], required_words=['aj'])
    response('Joshua is a pervert student in BSIT 2102.', ['who', 'is', 'joshua'], required_words=['who', 'joshua'])
    response('Joshua is part of the BSIT 2102 program.', ['joshua', 'student', 'BSIT 2102'], required_words=['joshua'])
    response('Dominic is a member of group that creates me.', ['who', 'is', 'dominic'], required_words=['who', 'dominic'])
    response('Dominic love to play badminton and help to create me.', ['dominic', 'team', 'project'], required_words=['dominic'])
    response('Mj is a student in BSIT 2102.', ['who', 'is', 'mj'], required_words=['who', 'mj'])
    response('Mj is pursuing studies in BSIT 2102.', ['mj', 'student', 'BSIT 2102'], required_words=['mj'])
    response('Paolo is a valued creator of me.', ['who', 'is', 'paolo'], required_words=['who', 'paolo'])
    response('Paolo contributes on creating me.', ['paolo', 'team', 'project'], required_words=['paolo'])
    response('Carl is also part of the group that created me.', ['who', 'is', 'carl'], required_words=['who', 'carl'])
    response('Carl is a big man that hate a none linear.', ['carl', 'team', 'project'], required_words=['carl'])
    response('Carl is also part of the group that created me.', ['who', 'is', 'carl'], required_words=['who', 'dizon'])
    response('Carl is a big man that hate a none linear.', ['carl', 'team', 'project'], required_words=['dizon'])
    response('I\'m 1 day old, and you?', ['how', 'are', 'you', 'old'], required_words=['how', 'old'])
    response('I\'m a bot that love to chat', ['can', 'tell', 'you', 'me', 'about', 'yourself'], required_words=['about', 'yourself'])
    response('I\'m a bot that love to chat', ['can', 'tell', 'you', 'me', 'about', 'your', 'self'], required_words=['about', 'self'])
    response('Don\'t ask me; I am just a bot programmed to reply in a chat.', ['how', 'to', 'do', 'this'], required_words=['how', 'to'])
    response('Nope, I\'m a bot that loves to chat.', ['are', 'you', 'an', 'ai'], required_words=['ai', 'you'])
    response('Don\'t ask me; I am just a bot programmed to reply in a chat.', ['meaning', 'of', 'this'], required_words=['meaning', 'of'])
    response('Don\'t ask me; I am just a bot programmed to reply in a chat.', ['meaning', 'of', 'this'], required_words=['definition', 'of'])
    response('AI means Artificial Intelligence that can be learned, but I can\'t learn since bots are programmed to do what they should', ['are', 'you', 'an', 'ai'], required_words=['ai'])
    response('Ow that\'s nice', ['ah', 'gets', 'ok'], single_response=True)
    response('Good i answer your question', ['yup', 'yes'], single_response=True)
    response('Why don\'t scientists trust atoms? Because they make up everything!', ['tell', 'me', 'a', 'joke'], required_words=['tell', 'joke'])
    response('Im from BSU-LIPA campus created by a group of student', ['where', 'you', 'came', 'from'], required_words=['came', 'from'])
    response("If I were you, I would go to the internet and type exactly what you wrote there!", ['give', 'advice'], required_words=['advice'])
    response("I don't like eating anything because I'm a bot obviously!", ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response("For today's pick-up line ay para doon sa mga gustong mapapunta sa kanila yung iniirog nila and here it is?", ['tell', 'pickup', 'line', 'pickupline'], required_words=['pickupline'])
    response("Ang babanlian ko nang mainit ng pagmamahal ay yung tamang tao para sa akin. Hindi ko lang alam kung sino siya.", ['tell', 'pickup', 'line', 'pickupline'], required_words=['pickup', 'line'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

