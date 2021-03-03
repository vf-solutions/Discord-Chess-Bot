# Discord-Chess-Bot
![Chess-Bot Logo](/assets/img/chess.png)
<div align="left">
<a href="https://github.com/Kaweees/Discord-Chess-Bot/stargazers"><img src="https://img.shields.io/github/stars/Kaweees/Discord-Chess-Bot" alt="Stars Badge"/></a>
<a href="https://github.com/Kaweees/Discord-Chess-Bot/members"><img src="https://img.shields.io/github/forks/Kaweees/Discord-Chess-Bot" alt="Forks Badge"/></a>
<a href="https://github.com/elangosundar/Kaweees/Discord-Chess-Bot/pulls"><img src="https://img.shields.io/github/issues-pr/Kaweees/Discord-Chess-Bot" alt="Pull Requests Badge"/></a>
<a href="https://github.com/elangosundar/Kaweees/Discord-Chess-Bot"><img src="https://img.shields.io/github/issues/Kaweees/Discord-Chess-Bot" alt="Issues Badge"/></a>
<a href="https://github.com/Kaweees/Discord-Chess-Bot"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Kaweees/Discord-Chess-Bot?color=2b9348"></a>
<a href="https://github.com/Kaweees/Discord-Chess-Bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Kaweees/Discord-Chess-Bot?color=2b9348" alt="License Badge"/></a>
</div>
<br>
In this repository, you will find the source code for the a Discord bot that is capable of hosting multiplayer chess games and Chess.com player information wrapper. Enjoy!

# How to Use the Bot
## Method 1: Invite Link:
In the case you are interested in just using the bot, you can invite the bot to your server by following [this link](https://discord.com/api/oauth2/authorize?client_id=744024313476415540&permissions=8&scope=bot).

## Method 2: Hosting it Independently
### Installation Instructions
You can download or modify the program by Cloning or Downloading the project or by saving it as a ".zip" file.
Once the downloaded file is extracted into a separate folder, follow these instructions:

### Discord.py + Other Dependencies Setup
1. Use the command `pip install Discord` in cmd or terminal to install `Discord.py 1.6.1` or the latest version.
2. Use the command `pip install chess.com` in cmd or terminal to install `Chess.com Wrapper 1.2.1` or the latest version.
3. Use the command `pip install chess` in cmd or terminal to install `python-chess 1.4.1` or the latest version. Also download `ChessGame` the [here](https://github.com/ljordan51/ChessGame) and download it in the root directory.
4. Use the command `pip install cairosvg` in cmd or terminal to install `CairoSVG 1.1` or the latest version.
5. Documentation for Discord.py could be found [here](https://discordpy.readthedocs.io/en/latest/index.html).
6. Documentation for Chess.com Wrapper could be found [here](https://chesscom.readthedocs.io/en/latest/) and [here](https://www.chess.com/news/view/published-data-api).
7. Documentation for CairoSVG could be found [here](https://cairosvg.org/documentation/).

### Before Running
1. Open `token.txt` and copy and paste the Discord Token so that the corresponding Discord bot is able to run the given program.

## Running via Heroku
### Via Heroku Git
1. Log onto Heroku.
2. Create a new application or open an existing application. Note the name of the application.
3. Go to `Settings > Add Build path > Python`
4. Install the Heroku CLI by following [this link](https://devcenter.heroku.com/articles/heroku-cli).
5. Navigate to the directory of the bot.
6. Create two files named `Procfile` and `requirements.txt`
7. Initialize and commit all of the files in your discord bot directory into a git repository. Sign into heroku via the command line and push the git repository to heroku.
    ```git
    heroku login
    heroku git:clone -a "NAME_OF_HEROKU_APPLICATION_GOES_HERE"
    git add .
    git commit -am “whatever commit text you want here”
    git push heroku master
    ```
8. Turn our bot on from heroku dashboard.
9. Navigate to the Bot Directory run `echo > Procfile` in that directory
10. Edit `requirements.txt` to include the following:
git+https://github.com/Rapptz/discord.py
dnspython==1.16.0
PyNaCl==1.3.0
async-timeout==3.0.1
11. Go to Heroku.com and go to `Resources`. Press `Edit`, and hit the sliding button so that it is on and hit `Confirm`.
12. The bot should be active after a few minutes, and enjoy!

### Via Heroku Website
1. Log onto Heroku.
2. Create a new application or open an existing application.
3. Go to `Deploy > Deployment method > Connect with GitHub` and add this repository. You must have access to this repository on a Github account for this to work, or create your own and include all of the files found in this repository.
4. Go to `Deploy > Deploy Branch > Main Branch` to depoly the recent version of the Main branch.
5. Repeat steps 2-4 whenever the Main Branch is updated to have access the latest features of the bot.
6. Go to `Resources`. Press `Edit`, and hit the sliding button so that it is on and hit `Confirm`.
7. The bot should be active after a few minutes. Enjoy!

# Contribute
Contributions are always welcome! Please create a PR and include a description of how your PR will improve the overall program and what it does.

## License

This project is licensed under [MIT](https://opensource.org/licenses/MIT) license.

## Support Us!

Give this repo a ⭐️ if you found this project helpful!
