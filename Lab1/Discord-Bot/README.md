# Setup (1)

### Dependencies 

  1. Install **Python 3** 
      - `sudo apt install python3`
      
  2. Install **Python 3 Pip** 
      - `sudo apt install python3-pip`
      
  3. Install **Discord version 2.0.1** *(compatible with Discord API v10)*
      - `pip3 install -U discord.py==2.0.1`
      
  4. Install **discord.py** using pip 
      - `pip3 install -U discord.py`

  5. Install **Python dotenv** *(to read file contaning bot's API Token)* 
      - `pip3 install -U python-dotenv`
  
  6. Install the **[code](https://github.com/WSU-kduncan/ceg3120-monreed/blob/main/Lab1/bot.py)**

### Discord.py v 2.0.1 Error Workaround (Optional) 

  1. Install **Python3.8**
      - `sudo apt install python3.8`
  
  2. Update **pip** for **Python3.8** 
      - `python3.8 -m pip install --upgrade pip`
  
  3. Install **discord.py v 2.0.1** 
      - `python3.8 -m pip install -U discord.py==2.0.1`
      
### API Token

  1. How to get one ..
      - Upon creating your bot, navigate to the `Bot` section within the **Discord Developer Portal** and under `Token` copy your bot's **API Token**. 
   
      ***Note //** If token does not display, you will need to "Reset Token" and copy the new one.*
      
   >   ![image](https://user-images.githubusercontent.com/97551273/190925976-460226ae-805b-4e2c-bacd-e1e5f1f03caf.png)
      
   >   ![image](https://user-images.githubusercontent.com/97551273/190925993-536bd970-7aac-49da-9109-e5c6e859d3e5.png)

  2. How to use it ..
      - Create file `.env` with this configuration:
        - `1. # .env` <br> 
        `2. DISCORD_TOKEN={your_discord_token}` ***Note //** Remove {}'s*
        
      - It is important that you add your `.env` file to `.gitignore` as this is sensitive information and your token will be reset if it is detected being published to a public domain.
      - Upon executing `python3 bot.py` your code will read and utilize your bot's token with lines:
        1. `from dotenv import load_dotenv`
        2. `load_dotenv()` <br>
        `TOKEN = os.getenv('DISCORD_TOKEN')`
        3. `client.run(TOKEN)`

# Usage (2)

### Command

   1. Use `trap!` to output a randomized quote from the **1998 Parent Trap** with Lindsay Lohan: 

 >  ![image](https://user-images.githubusercontent.com/97551273/190927358-c3a79e82-718d-49dc-bb44-e9822dea4c08.png)

# Research (3)

### 24/7 Bot Uptime ...
   - Upon doing some research, the general consensus about how to keep your bot running 24/7 is to use some sort of cloud service. Since, (depending on the specific provider) this instance will never "power off" like your computer does. This should, in theory, allow your bot to run 24/7. 
   
   - Something I stumbled upon is a site called `Discloud` which is a cloud service made specifically to allow Discord users to add the bots they want to run around the clock. This service works by prompting you for your bot's `Client ID` under "Client Information" on the **Discord Developer Portal**. Discloud also prompts you for a ZIP file containing all of the components needed to run/configure your specific bot. 
      - For editing purposes, users can join Discloud's server and use `.c` to submit an updated ZIP folder containing the new or revised bot code and the changes will be applied.
      
   - The majority of recommended solutions for 24/7 bot uptime include the use of some sort of cloud service, but I did come upon a forum that suggests using process managers `pm2` or `forever`. These are both software that aid users in keeping their applications alive around the clock and also perform system administrative tasks.
 
### Takeaway 
   - If it were me, I believe that based off of the research I completed I would choose to use some sort of cloud service to keep my bot running 24/7. `Discloud` seemed like an all around good choice, but I would probably commence more research to confirm the security and reliability of the service before uploading my bot's information.  

> ![giphy](https://user-images.githubusercontent.com/97551273/190928383-4ad6f8f1-596c-42a6-a92c-9f33a383ed92.gif)

^ Me to myself when I see that my bot code worked ...
