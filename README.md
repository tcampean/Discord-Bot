# Discord-Bot
A Discord Bot dedicated to managing user entries and block suspicious accounts.

The bot's main functionalities revolve around the users' account creation date. A newly created discord account might be considered suspect depending on the server's role and activity

The settings of each server are saved in a list and they are independent of eachother.


All commands have an asterisk (*) as prefix


**User Commands**

* *kickafter <given_date>
  
  Kicks every account on the server that has been created after the given date. If no date is provided, every account which is newer than 14 days will be kicked
  
  The date format is dd/mm/yyyy


* *banafter <given_date>
  
  Bans every account on the server that has been created after the given date. If no date is provided, every account which is newer than 14 days will be banned
  
  The date format is dd/mm/yyyy


* *whitelist <discord.Member>
  
  The member received as parameter will be added to the whitelist. If a user is whitelisted, they won't be affected by other commands. If no parameter given, every user from the server will be added to the whitelist


* *rwhitelist <discord.Member>

  The member received as parameter will be removed from the whitelist. The user can now be affected by bot commands. If no parameter given, every user from the server will be removed from the whitelist


* *setmindate <given_date>
 
  Sets a minimum account creation date for users that try to enter the server. Accounts that have been created after the minimum date won't be able to join the server. Implicitly set to None.
  
  The date format is dd/mm/yyyy
  

* *getmindate
  
  The bot sends a message in the same channel where the command was called containing the minimum entry creation date for the new members of that server



