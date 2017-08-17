#! /usr/bin/python
#-*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:32:22 2017

@author: joohhn
"""

# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=["text"])

def words_sort(message):
    word=message.text.split()
    vopros_a=['а?','А?']
    lol=['лол', 'ЛОЛ', 'Лол']
    if message.text in lol:
        bot.send_message(message.chat.id, 'Кек\nЧебурек')
    elif message.text in vopros_a:
        bot.send_message(message.chat.id, 'Хуй на!')
    elif len(word)==1:
        word1=[]
        myString = ''.join(word)
        filter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z','😀', '😄', '😅', '🤣', '☺', '️', '😊', '😇', '🙂',
                '🙃', '😉', '😋', '😚', '😙', '😗', '😘', '😍', '😌', '😜',
                '😝', '😛', '🤑', '🤗', '🤓', '😎', '😟', '😔', '😞', '😒',
                '😏', '🤠', '🤡', '😕', '🙁', '☹', '️', '😣', '😖', '😫', '😩',
                '😯', '😑', '😐', '😶', '😡', '😠', '😤', '😦', '😧', '😮',
                '😲', '😵', '😳', '😱', '😓', '😭', '😥', '🤤', '😢', '😰',
                '😨', '👍', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                '-', '=', '!', '"', '№', ';', '%', ':', '?', '*', '(', ')',
                '_', '+', '!', '@', '#', '$', '%', '^', '&', '*', '{', '}',
                '[', ']', '"', "'", '.', ',', '😃', '😁', '😆', '😂']
        glasnie1='аоиеёыуэюя'
        for i in myString.lower():
            if i not in filter:
                word1.append (i)
        print(word1)
        y=0
        x=0
        while y<= len(word1):
            if len(word1)==0:
                break
            x=word1[y]
            if len(word1)>1 and word1[0] in glasnie1 and word1[1] in glasnie1:
                word1.remove(word1[0])
            elif x  in glasnie1:
                if x in 'у':
                    word1.remove(word1[0])
                    word1.insert(0, 'ю')
                elif x in 'о':
                    word1.remove(word1[0])
                    word1.insert(0, 'ё')
                elif x in 'а':
                    word1.remove(word1[0])
                    word1.insert(0, 'я')
                elif x in 'ы':
                    word1.remove(word1[0])
                    word1.insert(0, 'и')
                elif x in 'э':
                    word1.remove(word1[0])
                    word1.insert(0, 'е')
                break
            else:
                word1.remove(word1[y])
        word1.insert(0, 'Ху')
        if len(word1)>=3:
            word1.append('!')
        myString=''.join(word1)
        myString=myString.capitalize()
        if len(myString)>=4:
            bot.send_message(message.chat.id, myString)

if __name__ == '__main__':
    bot.polling(none_stop=True)