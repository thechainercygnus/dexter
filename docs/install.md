# Install Dexter

Requirements:

```
Python 3.8.5
git
pipenv
screen
```

Clone the repo to your machine and enter the project directory:
```
git clone https://github.com/thechainercygnus/dexter.git
cd dexter
```

Install Python Modules:

```
pipenv install
```

Copy the example `.env` file from docs and enter your details:

```
cp docs/.env .
nan .env
```

The template `.env` has all the environment variable names set. Simply provide the correct values. You will need to create applications under Discord and Spotify's Developer Portals to obtain the required information.

```
DISCORD_TOKEN=''
DISCORD_CHANNELS=''
SPOTIFY_ID=''
SPOTIFY_SECRET=''
```

Run Dexter with the following:

`screen pipenv run python3 main.py`

You can exit the screen by pressing `Ctrl+A` then `D`. This will allow Dexter to run in the background on your host. You can get back to the Dexter screen to stop him if needed using `screen -R`.
