#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to reply to telgram messages with the tips the teacher uploaded as a text file
Written by: Abebe Amare
            Moses Makangila
            Moarabi Kakalalo
"""
import random
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
update_id = None

from pathlib import Path

import telegram
from telegram.ext import Updater

def reply(StudentAns,update):
    Str = StudentAns.split(",")
    ques=Str[0]
    q_num=int(ques[2])
    file = open("HACKDUKEQUESTION.txt").read()
    totalq = file.count("QQ")
    
    Strings = file.split(";")
  
    StudentQinput ="QQ"+str(q_num)
    Solutionset =  Strings[Strings.index(StudentQinput)+1:(int)(Strings.index(StudentQinput)+1+(len(Strings)/totalq))]
    
    SAA = Str[1:]
    #Checking Answer
    j=1
    for i in SAA: 
        if( i==Solutionset[j]):
            update.message.reply_text(Solutionset[j+1])

            
        else:
            update.message.reply_text(Solutionset[j+2])

        j=j+3
    return

def ques(q_num, update):
    file = open("HACKDUKEQUESTION.txt").read()
    totalq = file.count("QQ")
    Strings = file.split(";")
    StudentQinput ="QQ"+str(q_num)
    Solutionset =  Strings[Strings.index(StudentQinput):(int)(Strings.index(StudentQinput)+(len(Strings)/totalq))]
    Str = Solutionset[1]
    
    
    update.message.text=("please put your values to the list and send your answer again "+Str)
    
    return

 
    #this method will get the file from the instructor and store it as a text file
def text_f(update, context):
    user=update.message.from_user
    text_file=update.message.document.get_file()
    text_file.download("HACKDUKEQUESTION.txt")
    update.message.text="We get your document!"

def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('1039784861:AAHZ_dtqsFwoExC59didFOvPQ7s1TRRNm4s')

    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=30):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            #
            if(update.message.text==None):
                if(update.message.document==None):
                    update.message.reply_text("Please upload a file")
                else:
                    text_f(update, "hi")
                    update.message.reply_text(update.message.text)
            
            
            
            elif(update.message.text[0]=="C" and len(update.message.text)==3):
                ques(update.message.text[2], update)
                update.message.reply_text(update.message.text)
            elif(update.message.text[0]=="Q"):
                reply(update.message.text, update)
                update.message.reply_text(update.message.text)
            else:
            
                update.message.reply_text(update.message.text)
                


if __name__ == '__main__':
    main()
