# Welcome-to-my-hood
Welcome to my hood is a project where a user can join only 1 neighbourhood at a time and post blogs or businesses.
#### User stories: 
* Sign up and login
* Add a neighbourhood and view posts & businesses in that neighbourhood
* Search for a business
* Logout
* 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
To run this project you will need to install Python3 and any code editor tool 

```
e.g Atom or VS code
```

### Installing
#### Cloning the repository:  
 ```bash 
https://github.com/JoyChristine/Welcome-to-my-hood.git
```
#### Navigate into the folder and install requirements  
 ```bash 
cd Welcome-to-my-hood 
pip install -r requirements.txt 
```
##### Install Virtual environment
 ```bash 
 python3 -m venv virtual
```  
##### activate Virtual  environment 
 ```bash 
source virtual/bin/activate  
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

## Running the tests

 ```bash 
 make test
```

### Break down into end to end tests
The tests can be located in the app/tests.py file

They test for the creation,saving and deletion of a model
 ```bash 
 def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

 def test_save_profile(self):
        self.user.save()
       
 def test_delete_profile(self):
        self.user.delete()
```
 
## Deployment

I used [Heroku](https://heroku.com)   to deploy the app 


## Built With

* [Python3.8](https://www.python.org/)  
* [Django 4.0.4](https://docs.djangoproject.com/en/4.0/)  

## Contributing
To contribute to this project, fork the repo, create a new branch then develop on that branch

## Authors

* **[Joy Christine](https://github.com/JoyChristine)** 



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
