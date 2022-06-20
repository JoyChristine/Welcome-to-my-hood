# Welcome-to-my-hood


## Description
Welcome to my hood is a project where a user can join only 1 neighbourhood at a time and post blogs or businesses.
#### User stories: 
* Sign up and login
* Add a neighbourhood and view posts & businesses in that neighbourhood
* Search for a business
* Logout


### Prerequisites

# Setup and Installation  

  
#### Cloning the repository:  
 ```bash 
https://github.com/JoyChristine/Welcome-to-my-hood.git
```
#### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
make migrations
 ``` 
 Now Migrate  
 ```bash 
 make migrate 
```
##### Run the application  
 ```bash 
 make
``` 
The application opens up on `127.0.0.1:8000`. <br>
If you want to use new server run e.g 9000
```bash 
 make 9000
```
##### Testing the application  
 ```bash 
 make test
```


  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 4.0.4](https://docs.djangoproject.com/en/4.0/)  
* [Heroku](https://heroku.com)  
  


## Authors

* **[Joy Christine](https://github.com/JoyChristine)** 



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
