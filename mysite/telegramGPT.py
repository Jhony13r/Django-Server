import telebot
import openai

openai.api_key = "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"

bot = telebot.TeleBot("6235177809:AAHxeB6QK-ALNz1Jx5ciFfMBgRh2Zdt6X3k")

@bot.message_handler(commands=['chat'])
def handle_chat(message):
    question = message.text[6:]
    response = openai.Completion.create(engine="text-davinci-002", prompt=question, max_tokens=1024)
    answer = response['choices'][0]['text']
    bot.send_message(message.chat.id, answer)

bot.polling()