import os
import random
import telebot
from telebot import types
import pendulum
from time import sleep
from os import system


class Bot_mines_auto_dev():
def __init__(self, chat_id, token):
self.layout()
self.chat_id = chat_id
self.token = token
self.VARIAVEIS()
self.BOT_TELEGRAM()

def layout(self):
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
print(f""" x x
{re} T + + {cy} x x ,_________, x
{re} |___________ {cy} _ _ . _ _ ___ __ |_|__|__|_|
{re} | | + | | ´ {cy} |\ /| | |\ | |_ /__ \ \ | / /
{re} |___|___| | {cy} | \/ | | | \| |__x__/ \ \|/ / x
{re} + ____ __,___,____ +{cy} ___ ___ _ _ \ | /
{re} /_| | | + | | | {cy} |x \/ __/ \ x/ x \,/
{re} / | |__| | +|__| {cy} |__/\___x \/ x{gr}
""")
##### VARIAVEIS #####
def VARIAVEIS(self):
self.alert_sinal_id = 0
self.message_delete1 = False
self.hakeando = "CAACAgEAAxkBAAEJI0hkdA5R_-OJcKFvAAGHxf6rj0V4KwsAAi4EAALDbaBHkXOYO-NAdBsvBA"
self.fim_do_sinal = "CAACAgEAAxkBAAEJI15kdBggC0vFRwS_wcd_FLaPRNzXmQAC7wIAAk1zoUe81nImTxsciC8E"
self.sinal_entrada = "CAACAgEAAxkBAAEJI2RkdCNwRFJSiXk3bZ1Rfo4U6tcAAawAAr8CAAJB-6BHyH1H6rvQYkgvBA"
##### TRATAMENTO DAS HORAS #####
def GET_HORA_ATUAL(self):
timezone = pendulum.timezone('America/Sao_Paulo')
hora_local = pendulum.now(timezone)
return hora_local

#### SORTEANDO OS SINAIS DAS MINAS ####
def SORTEIO_MINAS(self):
print(f'''HORA ATUAL: {self.GET_HORA_ATUAL().format("HH:mm:ss")}''')
print(" ")
print("SINAIS MINES RIQUEZA")
print(f'''PROXIMO SINAL: {self.GET_HORA_ATUAL().add(minutes=4).format("HH:mm:ss")}''')
print(" ")
cores = ['💎','💣','💣','💣','💣','💎','💣','💣','💣','💣',
'💎','💣','💣','💣','💣','💎','💣','💣','💣','💣',
'💎','💣','💣','💣','💣']
for i in range (25):
self.sample = random.sample(cores, k=25)
#print(self.sample[0], self.sample[1], self.sample[2], self.sample[3], self.sample[4], self.sample[5], self.sample[6], self.sample[7], self.sample[8],self.sample[9], self.sample[10], self.sample[11], self.sample[12], self.sample[13], self.sample[14], self.sample[15], self.sample[16], self.sample[17], self.sample[18], self.sample[19], self.sample[20], self.sample[21], self.sample[22], self.sample[23], self.sample[24])
#### CRIANDO O BOT DO TELEGRAM ####
def BOT_TELEGRAM(self):
self.bot = telebot.TeleBot(self.token)

def SINAL_STIKER(self):
sinal = self.bot.send_message(self.chat_id, f'''⭐ɴᴏᴠᴏ ꜱɪɴᴀʟ⭐
⭐ᴍɪɴᴇꜱ ʟᴇɢᴇɴᴅᴀʀʏ⭐''')
self.message_delete1 = True
os.system("cls")
return sinal

def SINAL(self):
sinal = self.bot.send_message(self.chat_id, f'''💎ꜱɪɴᴀɪꜱ ᴍɪɴᴇꜱ ʟᴇɢᴇɴᴅᴀʀʏ💎
💣ᴍɪɴᴀꜱ: 3
🔄ᴄʜᴀɴᴄᴇꜱ: 2
{random.choice(self.sample[0])}{random.choice(self.sample[1])}{random.choice(self.sample[2])}{random.choice(self.sample[3])}{random.choice(self.sample[4])}
{random.choice(self.sample[5])}{random.choice(self.sample[6])}{random.choice(self.sample[7])}{random.choice(self.sample[8])}{random.choice(self.sample[9])}
{random.choice(self.sample[10])}{random.choice(self.sample[11])}{random.choice(self.sample[12])}{random.choice(self.sample[13])}{random.choice(self.sample[14])}
{random.choice(self.sample[15])}{random.choice(self.sample[16])}{random.choice(self.sample[17])}{random.choice(self.sample[18])}{random.choice(self.sample[19])}
{random.choice(self.sample[20])}{random.choice(self.sample[21])}{random.choice(self.sample[22])}{random.choice(self.sample[23])}{random.choice(self.sample[24])}
⏱ ᴠᴀʟɪᴅᴀᴅᴇ : {self.GET_HORA_ATUAL().add(minutes=4).format("HH:mm")}
⚠️ ᴏꜱ ꜱɪɴᴀɪꜱ ꜰᴜɴᴄɪᴏɴᴀᴍ ᴀᴘᴇɴᴀꜱ ᴄᴏᴍ ᴏ ʟɪɴᴋ ᴀʙᴀɪxᴏ''', reply_markup=self.BOTAO())
self.message_delete1 = True
return sinal

def BOTAO(self):
markup = types.InlineKeyboardMarkup()
markup.row_width = 2
markup.add(types.InlineKeyboardButton(text=f"🔗 Cadastre-se", url="https://www.flames.bet/c-ZrSlfflG?lang=pt"))
return markup

def EDITAR_MESSAGE(self):
os.system('cls' if os.name == 'nt' else 'clear')
message = self.bot.send_message(self.chat_id, f'''⭐ꜱɪɴᴀʟ ꜰɪɴᴀʟɪᴢᴀᴅᴏ⭐
✅ɢʀᴇᴇɴ✅
⏱ꜰɪɴᴀʟɪᴢᴀᴅᴏ: {self.GET_HORA_ATUAL().format("HH:mm")}''')

self.message_delete1 = False
return message
#self.bot.edit_message_text(text=f"""
#⭐𝙎𝙞𝙣𝙖𝙡 𝙛𝙞𝙣𝙖𝙡𝙞𝙯𝙖𝙙𝙤⭐
#⭐𝑴𝒊𝒏𝒆𝒔⭐
#⏱𝙁𝙞𝙣𝙖𝙡𝙞𝙯𝙖𝙙𝙤 𝙖́𝙨: {self.GET_HORA_ATUAL().format("HH:mm:ss")}""", chat_id=self.chat_id, message_id=m_id)
def ALERT_SINAL(self):
message = self.bot.send_message(self.chat_id, f'''⭐ᴘᴇɢᴀɴᴅᴏ ɴᴏᴠᴏ ᴘᴀᴅʀÃᴏ⭐
⭐ᴍɪɴᴇꜱ ʟᴇɢᴇɴᴅᴀʀʏ⭐
⏱ᴘʀᴇᴘᴀʀᴇᴍ ꜱᴇᴜꜱ ᴅᴇᴘÓꜱɪᴛᴏꜱ''', reply_markup=self.BOTAO())
self.message_delete1 = True
return message

def DELETE_MESSAGE(self, m_id):
if self.message_delete1:
self.bot.delete_message(chat_id=self.chat_id, message_id=m_id)
self.message_delete1 = False


##################################### STARTANDO O BOT ##################################################
def START_BOT(self):
while True:
system("cls")
self.layout()
self.SORTEIO_MINAS()
message_id_stiker_sinal = self.SINAL_STIKER().message_id
message_id_sinal = self.SINAL().message_id
sleep(240)
self.DELETE_MESSAGE(m_id=message_id_stiker_sinal)
self.message_delete1 = True
self.DELETE_MESSAGE(m_id=message_id_sinal)
message_id_editada = self.EDITAR_MESSAGE().message_id
sleep(60)
self.DELETE_MESSAGE(m_id=message_id_editada)
message_id_alerta = self.ALERT_SINAL().message_id
sleep(60)
self.DELETE_MESSAGE(message_id_alerta)

##################################################################################################################
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
print(f""" x
{re} T + + {cy} x x ,_________, x
{re} |___________ {cy} _ _ . _ _ ___ _x_ |_|__|__|_|
{re} | | + | | ´ {cy} |\ /| | |\ | / __//_ \ \ | / /
{re} |___|___| | {cy} | \/ | | | \| \___x__/ \ \|/ / x
{re} + ____ __,___,____ +{cy} ___ ___ _ _ \ | /
{re} /_| | | + | | | {cy} |x \/ __/ \ x/ x \,/
{re} / | |__| | +|__| {cy} |__/\___x \/ x {gr}
""")
print(" ")
print(" ")
chat_id = "-1001636512354"
token = "6073921642:AAGrmA2YZS8NWVjWFmFvFGtalsb6kyV2LXE"
system("cls")
bot = Bot_mines_auto_dev(chat_id, token)
bot.START_BOT()
