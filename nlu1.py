import random


BOT_CONFIG = {
"intent":{"hello":{"examples":["привет","как дела?"],"response":["привет","как дела?"] },
"bye":{"examples":['пока',"покакашка"], "response":['пока',"покакашка"],},
"failure_phrase":["перефразируйте","мне не понятно", "что-то я совсем непонятно"]}}



def get_failure_phrase():
    failure_phrase =["перефразируйте","мне не понятно", "что-то я совсем непонятно"]
    return random.choice(failure_phrase)

#print(get_failure_phrase())

def get_answer_by_intent(intent):
    phrases = BOT_CONFIG["intents"][intent]['response']
    return random.choice(phrases)

def get_intent(question):
    for x in BOT_CONFIG["intent"]:
        print(x)
    return "hello"
intent ="пока"
get_answer_by_intent(intent)

def bot(question):
    #nlu
    intent = get_intent(question)
    #получение ответа
    #заготовленные ответы
    if intent:
        return get_answer_by_intent(intent)
    #генерация
    answer = get_generative_answer(question)
    if answer:
        return answer
    return get_failure_phrase()