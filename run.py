#coding: utf-8

from slackbot.bot import Bot


import requests
requests.packages.urllib3.disable_warnings() 

def main():
        bot = Bot()
        bot.run()

if __name__ == "__main__":
        print("starting slackbot...")
        main()