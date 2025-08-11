import telebot
import webbrowser
bot = telebot.TeleBot('8433354441:AAHY0bJvFKhR350xeIDvqWbP8Sq-RXUlXXE')
buttonlist = ['Разработка 💻','Сети 🌐','Этичный хакинг 🎭','Открыть сайт']


@bot.message_handler(commands=['start'])
def main(message):
  markup = telebot.types.ReplyKeyboardMarkup()
  for button in range(len(buttonlist)):
    markup.row(telebot.types.KeyboardButton(buttonlist[button]))  
  bot.send_message(message.chat.id,  f'Привет, {message.from_user.first_name}, если ты за установкой <b style="color:red;">KaliLinux</b>, то тебе <a href="https://www.kali.org/" style="color:red; text-decoration:none;">сюда</a>', parse_mode='html',reply_markup=markup)
  bot.register_next_step_handler(message,on_click)


def on_click(message):
  if message.text == buttonlist[0]:
    bot.send_message(message.chat.id, 'Очень надеюсь, что в ближайшее время выйдут все курсы по разработке')
  elif message.text == buttonlist[2]:
    bot.send_message(message.chat.id, 'Очень надеюсь, что в ближайшее время выйдут все курсы по этичному хакингу')
  elif message.text == buttonlist[1]:
    bot.send_message(message.chat.id, 'Очень надеюсь, что в ближайшее время выйдут все курсы по сетям')
  elif message.text == buttonlist[3]:
     bot.send_message(
            message.chat.id,
            'Вот ссылка на iPhone 14 Pro: <a href="https://exampleexe.ru/iphone14prophp/">Перейти</a>',
            parse_mode='html'
        )
  keyboard = telebot.types.ReplyKeyboardRemove()  
  bot.send_message(message.chat.id, 'Удаляю клавиатуру', reply_markup=keyboard)      
  
  
@bot.message_handler(content_types=['text'])
def get_text(message):
  if message.text == 'Мой ID':
    bot.reply_to(message,message.chat.id)
    return
  if message.chat.id != 484209456:
    bot.send_message(484209456,f'Пришло сообщение от {message.from_user.first_name} \n его ID: {message.chat.id} \n А уникальный ID {message.from_user.id}\n 💌 {message.text}')
    return
  markup = telebot.types.InlineKeyboardMarkup()
  markup.add(telebot.types.InlineKeyboardButton('Открыть сайт', callback_data='open'))
  bot.reply_to(message,message.text,reply_markup = markup)
  bot.send_message(1199196232, message.text)
  

@bot.message_handler(content_types=['photo','file'])
def get_photo(message):
  markup = telebot.types.InlineKeyboardMarkup()
  btn1 = telebot.types.InlineKeyboardButton('Я тебя понял 😎', callback_data='any1')
  btn2 = telebot.types.InlineKeyboardButton('Буду ждать 😱', callback_data='any2')
  markup.row(btn1,btn2)
  bot.reply_to(message,"Подожди, я пока в процессе разработки", reply_markup = markup) 
  

#------------------------------------Обработка нажатий инлайн кнопок------------------------------------
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
  if callback.data == 'any1':
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(callback.message.chat.id, "Что же, надеюсь лишний раз не будешь меня загружать")
  elif callback.data == 'any2':
    bot.send_message(callback.message.chat.id, "Давай, только не уходи никуда")  
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
  elif callback.data == 'open':
    bot.send_message(callback.message.chat.id, 'Вот ссылка на iPhone 14 Pro: <a href="https://exampleexe.ru/iphone14prophp/">Перейти</a>',
            parse_mode='html')
    bot.delete_message(callback.message.chat.id, callback.message.message_id) 
#-------------------------------------------------------------------------------------------------------  


  

  
  
bot.polling(non_stop=True)
