import unittest

import telebot.apihelper

import bot
import config

username = "Oleg"
me = "Jiraffe"
strange_username = "@34424фыфыфв"


class BotLogicTests(unittest.TestCase):


    def test_start_message(self):
        self.assertEqual(bot.start_message(username, me) , "Welcome, " + username +"! I'm - <b>"+ me +"</b>, bot designed to work with Jira.")

    def test_start_message_lang(self):
        self.assertEqual(bot.start_message(strange_username, me) , "Welcome, " + strange_username + "! I'm - <b>"+ me +"</b>, bot designed to work with Jira.")

    def test_create_jira(self):
       self.assertRegex(str(bot.create_jira_webhook("anything", [], "", config.SERVER, bot.REST_URL, config.LOGIN,
                                config.API_KEY)), r'^2.')

    def test_check_jira(self):
        self.assertEqual(bot.check_webhooks(config.SERVER, bot.REST_URL, config.LOGIN, config.API_KEY), 200)

    def test_incorrect_API_create(self):
        self.assertEqual(bot.create_jira_webhook("anything", "jira:issue_created", "", config.SERVER, bot.REST_URL, config.LOGIN,
                                "632468776"), 401)
if __name__ == "__main__":
  unittest.main()

# bot.create_jira_webhook("anything", ["jira:issue_created","jira:issue_updated"], "", config.SERVER, bot.REST_URL, config.LOGIN,
#                                 config.API_KEY)