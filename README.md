<div align="center">
    <h1>TgL꩜꩜k<br>¯\_(ツ)_/¯</h1>
    <p><b>Simple Telegram self bot to scrape information about groups and users using Telethon</b></p>
    <p>Check Userinfo | Check Username | Scrape member </p>
</div>
<br>

# ・┆ Installation 𓍊𓋼𓍊𓋼𓍊
1. **Installing requirement**<br>
     You need to install `python`, `pip` and `virtualenv` before using this bot. simply install them via your package manager<br>
   
2. **Clone repository**
    ```bash
    git clone https://github.com/kozyol/TgLook
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
<br> 

# ・┆ Usage 𓆝 𓆟 𓆞 𓆝
+ **Group members scraper**<br>
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
+ **Username availability checker**<br>
    Send `$username` following username as argument to check its status:
    - **Taken**: The Username is taken
    - **Available**: The username is not in use by anyone else yet.
    - **Not Valid or Banned**: The username is not valid or banned by Telegram.<br>
    E.G. `$username username_without_at`

+ **User info checker**
    Send `$whois` following username as argument to check its account status:
    ```plaintetxt
    ×͜× Who IS Lookup
    ┆ Chat-ID: 123xxxx789
    ┆ Access Hash: 12313xxxxxx876969
    ┆ First Name: Alex
    ┆ Last Name: None
    ┆ Username: xxx
    
    𖣠 Account status
    ┆ Is restricted: False
    ┆ Is scam: False
    ┆ Is fake: False
    ┆ Is bot: False
    ┆ Is self: True
    ┆ Is premium: True
    
    ⊹ Bio
    Hey, I'm a developer :)
    
    ᨒ Restriction Reason:
    ```
    And that is, self bot will send you inforamtion when you use these commands.

    > Note: Don't use @ in usernames, send it witout @.
    > Here is list of examples
    ```plaintext
    $username johndoe  -> look for username 
    $chats             -> show all groups
    $get 0             -> get first groups members
    $whois johndoe     -> get information abour user
    ```

<br>

# ・┆ Proxy Chain 𓆝 𓆟 𓆞 𓆝
If you have limitation for your region, you can simply use tor and proxychains to run your bot with proxy<br>
+ **run script**
    ```bash
    # Use -q for quiet mode
    proxychains -q python main.py
    ```
+ **re-New IP address**
    ```bash
    sudo pkill -HUP tor
    ```
+ **check your IP address**
    - Using TorProject API:
        ```bash
        proxychains -q https://check.torproject.org/api/ip
        # Output e.g {"IsTor":true,"IP":"111.222.333.444"}
        ```
        
    - Using AmazonAws API:
        ```bash
        proxychains -q https://checkip.checkip.amazonaws.com
        # Output e.g 111.222.333.444
        ```
<br>

# ・┆ Thanks ˗ˏˋ ♡ ˎˊ˗
Thank you for using this tool. hope you like it :D
