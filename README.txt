Getting Started:
- Installing Django on Windows (https://docs.djangoproject.com/en/2.0/howto/windows/)
  - This is all done on Command Prompt or Terminal of Macs.
  - Install the latest Python version. This build runs on Python 3 so if you have Python 2, it won't work.
  - IMPORTANT: Make sure you set Python to PATH to be able to run Python commands on Command Prompt.
  - You can check your Python version by running: python --version
  - Last but not least, install Django by running the command: pip install django
  - If you cannot run the pip command, then the link above will show you how to install pip.

How to Open the Site:
- Wherever you've cloned the UCI-GameCatalog-Main-Folder to, you'll see another
  folder called GameCatalogSite within.
- Open that folder and you'll see a manage.py file.
- In Command Prompt/Terminal, set the current directory to the path of   GameCatalogSite.
- Example: cd C:\Users\...\...\GitHub\UCI-GameCatalog-Main-Folder\GameCatalogSite
- Now run the command: python manage.py runserver
- Now open up a browser and enter 127.0.0.1:8000 to see the site hosted locally.

It's suggested to look up some guides to Django, HTML/CSS, and mySQL. It's fairly easy to pick up.
A suggest YouTube Guide for Django:
- https://www.youtube.com/watch?v=FNQxxpM1yOs&list=PLQVvvaa0QuDeA05ZouE4OzDYLHY-XH-Nd

Things that were done:
- Implementation of site. (This could continuously change, the start from scratch is already done for you)
- The excel sheet have already been uploaded to the UCI database provided.

Things that needed to be continued:
- Connecting of the database to the site.
- Adding a search function. (search bar directly links to only game page)