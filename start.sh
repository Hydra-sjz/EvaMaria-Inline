if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Hydra-sjz/EvaMaria-Inline.git /EvaMaria-Inline
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /EvaMaria-Inline
fi
cd /EvaMaria-Inline
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
