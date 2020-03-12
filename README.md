# streamRecordingAPI
Create a RestAPI using Flask, Marsmallow and SQLAlchemy


Python Libraries to install:
* pip install flask
* pip install Flask-SQLAlchemy
* pip install flask_marshmallow



# API endpoints:

Run the main app.py file of our RestAPI and terminal must display something like this:
```
FLASK_APP = app.py
FLASK_ENV = development
FLASK_DEBUG = 0
In folder /home/babufrik/PycharmProjects/bmat_rtroulak
/home/babufrik/PycharmProjects/bmat_rtroulak/venv/bin/python -m flask run
 * Serving Flask app "app.py"
 * Environment: development
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
well http://127.0.0.1 is our locahost server and 5000 is our port.We will use these for our examples otherwise if you have other ip and port you can replace them


#### Retrieve all channels 

```/channel ``` (GET)
		
Example: 	
```
curl http://127.0.0.1:5000/channel
```

#### Retrieve the channel with the specified id 

```/channel/<id> ``` (GET)
		
Example: 	
```
curl http://127.0.0.1:5000/channel/1
```

#### Retrieve all recordings 

```/recording ``` (GET)
		
Example: 	
```
curl http://127.0.0.1:5000/recording
```



#### Retrieve the recording with the specified id 

```/recording/<id> ``` (GET)
		
Example: 	
```
curl http://127.0.0.1:5000/recording/1
```


#### Retrieve all recordings of the specified channel 

```/channel/<channel_id>/recordings ``` (GET)
		
Example: 	
```
curl http://127.0.0.1:5000/channel/<channel_id>/recordings
```




#### Add channel in the database

```/channel ``` (POST)

Required request data params:
 `name=[string]`
 `keyname=[string] must have 10 char length`
 `type=[string] enum['radio','TV']`
 `url=[string]`

 
 Example: 
 ```
curl --header "Content-Type: application/json" \
 --request POST \
 --data '{
	"name": "Rock FM",
  "keyname": "es-rock-01",
	"type": "radio",
	"url": "http://rockfmlive.mdc.akamaized.net/strmRCFm/userRCFm/playlist.m3u8"}' http://127.0.0.1:5000/channel
  ```
 
#### Add Recording in the database

```/recording ``` (POST)

Required request data params:
 `channel_id=[int]`
 `start_time=[int] timestamp (datetime)`
 `end_time=[int] timestamp (datetime)`
 `path=[string]`

 
 Example: 
 ```
curl --header "Content-Type: application/json" \
 --request POST \
 --data '{
	"channel_id": 2,
  "start_time": 1583929812000,
	"end_time": 1583929812000,
	"url": "http://hlsliveamdgl1-lh.akamaihd.net/i/hlsdvrlive_1@584096/index_0400_av-p.m3u8?sd=10&rebase=on"}' http://127.0.0.1:5000/recording
  ```
  
#### Create a new channel, or update an existing one
    
```/channel/<id> ``` (PUT)

Required request data params: 
  `name=[string]` or
 `keyname=[string] must have 10 char length` or
 `type=[string] enum['radio','TV']` or
 `url=[string]`
 
Optional request data params:
 `name=[string]`
 `keyname=[string] must have 10 char length`
 `type=[string] enum['radio','TV']`
 `url=[string]`
 
Example:
```
curl --header "Content-Type: application/json" \
 --request PUT \
--data '{
	"name": "Rock FM",
  "keyname": "es-rock-01",
	"type": "radio",
	"url": "http://rockfmlive.mdc.akamaized.net/strmRCFm/userRCFm/playlist.m3u8"}' http://127.0.0.1:5000/channel/4
 ``` 
 
 #### Create a new channel, or update an existing one
    
```/recording/<id> ``` (PUT)

Required request data params: 
  `channel_id=[int]` or
  `start_time=[int] timestamp (datetime)` or
 `end_time=[int] timestamp (datetime)` or
 `path=[string]`
 
Optional request data params:
`channel_id=[int]`
 `start_time=[int] timestamp (datetime)`
 `end_time=[int] timestamp (datetime)`
 `path=[string]`

Example:
```
curl --header "Content-Type: application/json" \
 --request PUT \
 --data '{
	"channel_id": 2,
  "start_time": 1583929812000,
	"end_time": 1583929812000,
	"url": "http://hlsliveamdgl1-lh.akamaihd.net/i/hlsdvrlive_1@584096/index_0400_av-p.m3u8?sd=10&rebase=on"}' http://127.0.0.1:5000/recording/3
  ```

There is a sub-directory test_api, where I've added some sample data (scraped with Scrapy) to the databse, using the API.




  

 #### Delete a channel
 
 ```/channel/<id> ``` (DELETE)
 
 
 Example:

```
curl --request DELETE  http://127.0.0.1:5000/channel/2
```

 #### Delete a recording
 
 ```/channel/<id> ``` (DELETE)
 
 
 Example:

```
curl --request DELETE  http://127.0.0.1:5000/recording/2
```
I decided not to require Authentication to make testing easier 
