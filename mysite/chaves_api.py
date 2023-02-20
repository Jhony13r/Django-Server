import telebot
import openai
import chaves_api

openai.api_key = chaves_api.api_openai

bot = telebot.TeleBot(chaves_api.api_telegram)

@bot.message_handler(commands=['chat'])
def handle_chat(message):
    question = message.text[6:]
    response = openai.Completion.create(engine="text-davinci-002", prompt=question, max_tokens=1024)
    answer = response['choices'][0]['text']
    bot.send_message(message.chat.id, answer)
    bot.polling()