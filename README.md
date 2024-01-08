<div align="center">
    <h1>¯\_(ツ)_/¯<br>ᯤ TgLook</h1>
    <p><b>Simple Telegram self to scrape info about groups and users using Telethon</b></p>
    <p>Check Userinfo | Check Username | Scrape member </p>
</div>
<br>

# ・┆ Installation
1. **Installing requirement**<br>
     You need to install `python`, `pip` and `virtualenv` before using this bot. simply install them via your package manager<br>
   
2. **Clone repository**
    ```bash
    git clone https://github.com/Kourva/TgLook
    ```
3. **Navigate to script directory**
    ```bash
    cd TgLook
    ```
4. **Activate virtual environment**
    ```bash
    virtualenv venv && source venv/bin/activate
    ```
5. **Install requirements**
    ```bash
    python -m pip install -r requirements.txt
    ```
6. **Configure credential**<br>
    run `setup.py` and enter your api-ID and api-Hash. you can get it from [Telegram](https://my.telegram.org).
    ```bash
    python setup.py
    ```
7. **Run self bot**
    ```bash
    python main.py
    ```
   
# ・┆ Usage 
+ **Scrape group members**<br>
    Send `$chats` to self bot and it will show you list of your groups which you are member of it.
    ```plaintext
    ×͜× Please choose group to get member from it:

    ┆ Idx0: Group 1 
    ┆ Idx1: Text group
    ... and so on
    
    ⁀➴ Send $get [index] to get members.
    E.G. $get 0
    ```
    Then send `$get` with index as argument to get list of members in the group.
    ```csv
    chat_id,first_name,last_name,username,phone,access_hash,group_title,group_id
    123xxxx890,John,Doe,JohnDoe,+1xxxxxx,188420xxxxxxxx58432,Group 1,12xxxx7662
    ```
    
