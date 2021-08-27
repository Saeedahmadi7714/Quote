# Quote

A simple and basic blog using Flask, MongoDB, and a little bit of JavaScript. You can post content or enjoy reading other people's content.

<img src="https://user-images.githubusercontent.com/71176889/131195973-9f30f092-f956-45df-becd-11065d0cfd77.png" width="90%"></img> <img src="https://user-images.githubusercontent.com/71176889/131195980-3c787634-7aa6-4f4f-8c44-1bca6c932e82.png" width="90%"></img> <img src="https://user-images.githubusercontent.com/71176889/131195983-6a7d2b87-b3dc-4878-92e1-735a58b597cc.png" width="90%"></img> <img src="https://user-images.githubusercontent.com/71176889/131195987-5d88401b-2232-4e00-bfe1-a9eb3757e444.png" width="90%"></img> 

## Features

* As a normal user : 
    * Read all posts in application
    * Search in posts with categories and tags

* As logged in user :
    * Create, delete and deactivate your posts
    * Edit your posts (you can't change the image and post's category)
    * Like or dislike posts 


## How install and run ?
##### Clone the repository :
```bash
$ git clone https://github.com/Saeedahmadi7714/quote.git
$ cd quote
```
##### Create a virtualenv and activate it:
 ```bash
$ python3 -m venv venv
$ . venv/bin/activate.
```
##### Or on Windows cmd : 
 ```bash
> py -3 -m venv venv
> venv\Scripts\activate.bat
```
##### Install the app :
```bash
$ pip3 install -e .
```
#####  Export environment variables and run flask on local host :
```bash
$ export FLASK_APP=quote
$ export FLASK_ENV=development
$ flask run
```
##### Or on Windows cmd : 
```bash
> set FLASK_APP=quote
> set FLASK_ENV=development
> flask run
```
Open http://127.0.0.1:5000 in your browser. 
## License
[GNU GPLv3](https://https://choosealicense.com/licenses/gpl-3.0/)
