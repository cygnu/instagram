# 「python-dotenvを使って環境変数を設定する」(https://qiita.com/harukikaneko/items/b004048f8d1eca44cba9)
import os
from os.path import join, dirname
from dotenv import load_dotenv


load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")