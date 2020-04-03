# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ


@respond_to('献立')
def mention_func(message):
    message.reply('kondate') # メンション

@listen_to('hiokichi')
def listen_func(message):
    message.send('誰かが呼んでいる…')      # ただの投稿
    message.reply('君だね？')                           # メンション