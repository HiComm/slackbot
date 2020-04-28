# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

import glob,os
import plugins.sendmail as sendmail

class Path:
    def __init__(self):
        self.pwd = (r"\\fileserver9\products")
    

path = Path()

mailer = sendmail.Mail()
os.chdir(path.pwd)

def ls(_path):
    output = ""
    if os.path.exists(_path):
        for item in os.listdir(_path):
            item = os.path.join(_path, item)
            if os.path.isfile(item):
                output += ("[File] " + os.path.basename(item) + "\n")
            elif os.path.isdir(item):
                output += ("[Dir] " + os.path.basename(item) + "\n")
            else:
                output += ("[Unknown!]" + item + "\n")
    else:
        output = "'" + _path + "'にアクセスできません。(存在しない)"
    return output

@respond_to(r'^ls$')
def exec_simplels(message):
    message.send(ls(path.pwd))

@respond_to(r'^pwd$')
def exec_simplels(message):
    message.send(path.pwd)

@respond_to(r'^ls\s.+$')
def exec_remove(message):
    arg = (message.body['text']).split(' ')
    if arg[0] == 'ls':
        if arg[1] == '':
            message.send(ls(path.pwd))
        else:
            message.send(ls(arg[1]))

@respond_to(r'^cd\s.+$')
def exec_remove(message):
    arg = (message.body['text']).split(' ')
    if arg[0] == 'cd':
        if arg[1] != '':
            try:
                os.chdir(arg[1])
                path.pwd = os.getcwd()
                message.send(path.pwd+"\n------")
                message.send(ls(path.pwd))
            except:
                message.send("'" + arg[1] +"'に移動できません")

@respond_to(r'^get\s.+\s.+$')
def exec_sendmail(message):
    arg = (message.body['text']).split(' ')
    if arg[0] == 'get':
        fullpath = os.path.abspath(arg[1])
        address = arg[2] + "@hioki.co.jp"
        if(os.path.exists(fullpath)):      
            mailer.sendMail(address, "ファイル送信", "自動送信されたメールです。\n"+fullpath, arg[1])
            message.send(address + "宛てに'" + fullpath + "'を添付したメールを送信しました。")
        else:
            message.send("'" + fullpath + "'が存在しません。")

@listen_to('hiokichi')
def listen_func(message):
    message.send('誰かが呼んでいる…')      # ただの投稿
    message.reply('君だね？')                           # メンション