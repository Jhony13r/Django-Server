import requests

bot_token = '6235177809:AAHxeB6QK-ALNz1Jx5ciFfMBgRh2Zdt6X3k'
api_url = f'https://api.telegram.org/bot{bot_token}/deleteWebhook'

response = requests.get(api_url)

print(response.content)
