from bs4 import BeautifulSoup  #del módulo bs4, necesitamos BeautifulSoup
import requests
import schedule

def bot_send_text(bot_message):
        
    bot_token = 'Your Token'
    bot_chatID = 'Your Chat ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response

#test_bot = bot_send_text('Soy el bot creado por Juan, Cómo puedo ayudarte???')

def btc_scraping():
    url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'text-larger text-price'})
    format_result = result.text

    return format_result

def report():
    btc_price = f'El precio de Bitcoin es de {btc_scraping()}'
    bot_send_text(btc_price)

if __name__ == '__main__':
        
    schedule.every().day.at("11:46").do(report)

    while True:
        schedule.run_pending()