#import anaconda
import random
import nltk


BOT_CONFIG = {
    'intents': {'hello': {'examples': ['Привет', 'Здравствуйте', 'Добрый день',"привет","как дела?"],\
                        'responses': ['Привет, человек', 'Здравствуйте!', 'Шалом, юзер']},\
                'bye':   {'examples': ['Пока', 'Досвидания', 'Увидимся','пока',"покакашка"],\
                        'responses': ['Прощай, человек. Приходи ещё.', 'Увидимся']}},\
    'failure_phrases': ['Мне непонятно','Перефразируйте, пожалуйста','Не умею отвечать на такое',\
           "перефразируйте","мне не понятно", "что-то я совсем непонятно"]\
           }



def get_failure_phrase():
    failure_phrase =BOT_CONFIG['failure_phrases']
    return random.choice(failure_phrase)



def get_intent(question):
    
    for intent, intent_value in BOT_CONFIG["intents"].items():
        #print(intent, intent_value['examples'])
        for example in intent_value['examples']:
            #print (example)
            #if example != question:
            d = nltk.edit_distance(example.lower(), question.lower())
            #print(question)
            diff = d/ len(example)
            if diff <0.4:
                return intent

def get_generative_answer(question):
    return

def get_answer_by_intent(intent):
    phrases = BOT_CONFIG["intents"][intent]['responses']
    #return print(phrases[0])
    return print(random.choice(phrases) )          

def bot(question):
    #nlu
    intent = get_intent(question)
   
    #получение ответа
    #заготовленные ответы
    if intent:
        return get_answer_by_intent(intent)
    print(get_answer_by_intent(intent))
    
    #генерация
    answer = get_generative_answer(question)
    if answer:
        return answer
    #Заглушка
    return get_failure_phrase()





question = "пивет"
bot(question)
print("161020")

