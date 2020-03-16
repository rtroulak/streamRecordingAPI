# Stream Recording API
Create a CRUD recording RestAPI using Flask, Marsmallow and SQLAlchemy



## Technologies
Project is created with:
* Python version: 3.6
* Flask version: 1.1.1
* Flask-SQLAlchemy version: 2.4.1
* flask-marshmallow version: 2.4.1
* pytest
* ffmpeg 1.4
* ffmpeg-python
* OS: Ubuntu 18.04
* IDE: Pycharm

## Submitted Files

### Files
* ```app.py``` (server and restAPI file)
* ```classes.py``` (Classes and instances of Db for this project)
* ```recorder.py``` ( The maine recording code with the function that do this job )
* ```recs.db``` (db file that used in this project)
* ```requirements.txt``` (all required libraries and packages)
* ```setup.py```
* ```start.py``` (start all saved streams in db to record)
* ```test_api.py``` (unit test file)
* ```rtroulak_Logic_Test_BMAT.xlsx``` (logic test)
* ```clear``` (bash script that clear dump files and kill thread processes after unit testing)
### Folders
* ```sample_recordings_results ```(submitted only to check some results with recordings of 1min(!) each to avid large files
* ```recording``` (The main folder that recordings will be saved)


# Installation
In the application folder create python environment. Python virtual environment is a self-contained directory tree that includes a Python installation and number of additional packages.


Check python version:

```python3 -V```

Install Virtual Environment in your system:

```sudo apt install python3-venv```

Run the following command to create your new virtual environment:

``` python3 -m venv env ```

 Activate your new virtual environment, to start using this:

```. env/bin/activate ```

In the requirements file there are all the required packages that required for this project, run :

```pip install -r requirements.txt```


or install Python Libraries that required for this porject manually:
* ```pip install flask```
* ```pip install Flask-SQLAlchemy```
* ```pip install flask_marshmallow```
* ```pip install marshmallow-sqlalchemy```
* ```pip install ffmpeg-python```
* ```pip install -U pytest```
* ```pip install ffmpeg==1.4```
* ```pip install requests```

# Unit Testing for RestAPI

Start the restAPI server with this command:

```python3 app.py```

Τerminal will display something like this:


Output:
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
http://127.0.0.1 is our locahost server and 5000 is our port.We will use these for our examples otherwise if you have
 other ip and port you can replace them
 
 Then run the test file named:
 ``` pytest test_api.py ```
 

If all tests passed you will have this output:
```

============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-5.4.1, py-1.8.1, pluggy-0.13.1 -- /home/babufrik/PycharmProjects/bmat_rtroulak/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/babufrik/PycharmProjects/bmat_rtroulak
collecting ... collected 12 items

test_api.py::TestRecordingRestApi::test_channel_add PASSED               [  8%]
test_api.py::TestRecordingRestApi::test_channel_update PASSED            [ 16%]
test_api.py::TestRecordingRestApi::test_get_channel PASSED               [ 25%]
test_api.py::TestRecordingRestApi::test_get_channel_all PASSED           [ 33%]
test_api.py::TestRecordingRestApi::test_get_recording PASSED             [ 41%]
test_api.py::TestRecordingRestApi::test_get_recording_all PASSED         [ 50%]
test_api.py::TestRecordingRestApi::test_get_recording_channel PASSED     [ 58%]
test_api.py::TestRecordingRestApi::test_recording_add PASSED             [ 66%]
test_api.py::TestRecordingRestApi::test_recording_update PASSED          [ 75%]
test_api.py::TestRecordingRestApi::test_trash_channel PASSED             [ 83%]
test_api.py::TestRecordingRestApi::test_trash_recording PASSED           [ 91%]
test_api.py::TestRecordingRestApi::test_will_shutdown PASSED             [100%]

============================== 12 passed in 0.23s ==============================

Process finished with exit code 0

```

Then clear server from the test files and thread processes that will be created with bash
script 
``` ./clear ```

or run manually 2 commands:

* ``` rm recordings/*.aac ``` 

* ``` rm recordings/*.mp4 ``` 

(delete all files from recording folder that created from unit test post and put cases)

* ``` sudo killall ffmpeg  ``` 

(delete all ffmpeg processes that created from unit test post and put cases)

# Use Stream Recording API

Tp start the restAPI server normally and use application start server with this command:

```python3 app.py```

Τerminal will display something like this:


Output:
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
http://127.0.0.1 is our locahost server and 5000 is our port.We will use these for our examples otherwise if you have other ip and port you can replace them

Run:

```python3 start.py```

And then the recording code file to start with the server and start to record all the existing channels from database and 
wait to get api user commands via API (main functionality of recording is on ```recorder.py```)

Output:
```
Start Record TV Streaming : MAD TV Greece 
Start Record TV Streaming : RTV Murcia 
Start Record Radio Streaming : Rock FM 
Start Record Radio Streaming : RastaPank UOC 
```


All the recordings saved on /recordings directory in the project.



Use all the API endpoints to retrieve,create,edit or retrieve new channel and recording while server is running.
We have the complete CRUD endpoints for channel and recording (in this project we need only CRUD of channel but
i  create for recordings too, maybe for future work of this project will be useful)





# API endpoints:
## Retrieve

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
curl http://127.0.0.1:5000/channel/1/recordings
```


## Create

#### Add channel in the database

```/channel ``` (POST)

Required request data params:
 `name=[string]`
 `keyname=[string] must have 10 char length`
 `type=[string] enum['radio','TV']`
 `url=[string]`

 
 Example: 
 ```
 
curl --location --request POST 'http://127.0.0.1:5000/channel' \
--header 'Content-Type: application/json' \
--data-raw '{
    "keyname": "gr-rstpk12",
    "name": "RastaPank UOC11",
    "type": "radio",
    "url": "http://rs.radio.uoc.gr:8000/uoc_64.mp3"
}'

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
curl --location --request POST 'http://127.0.0.1:5000/recording' \
--header 'Content-Type: application/json' \
--data-raw '    {
        "channel_id": 1,
        "end_time": 158392981021020,
        "path": "/recording/",
        "start_time": 158392981021030
    }'
  ```
  
## Update
 
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
curl --location --request PUT 'http://127.0.0.1:5000/channel/4' \
--header 'Content-Type: application/json' \
--data-raw '{
    "keyname": "gr-rstp-04",
    "name": "RastaPank UOC ",
    "type": "radio",
    "url": "http://rs.radio.uoc.gr:8000/uoc_64.mp3"
}'
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

curl --location --request PUT 'http://127.0.0.1:5000/recording/3' \
--header 'Content-Type: application/json' \
--data-raw '{
	"channel_id": 2,
  "start_time": 1583929812000,
	"end_time": 1583929812000,
	"path": "/recording/"}'
    

  ```


## Delete
  

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
I decided not to require Authentication from my api calls to avoid conflicts and make testing easier 

### Shutdown

```
curl --request POST  http://127.0.0.1:5000/shutdown
```

```
curl --location --request POST 'http://127.0.0.1:5000/shutdown' \
--header 'Content-Type: application/json' \
--data-raw ''
```

Models
---

### Channel table

Our database tables are:

| Field | Type | Options | Description | 
| :---: | :---: | --- | :---: |
| id | INTEGER |  -  | Channel id  (PK)|
| name| TEXT  | -  | Name of channel|
| keyname| TEXT|  Must be 10 characters long  | The keyname of channel |
| type| TEXT|   Enum: <ul><li>radio</li><li>TV</li></ul>  | type of channel, will be radio or TV |
| url| TEXT  | -  | Url of channel|


### Recordings

| Field | Type | Options | Description | 
| --- | --- | --- | --- |
| id | INTEGER |  -  |Recording id (PK) |
| channel_id| INTEGER| - | Channel id (FK on Channel table)|
| start_time | TEXT|  Datetime ISO 8601 format (YYYY-MM-DD HH:MM:SS)  | start time of recording streaming |
| end_time | TEXT|  Datetime ISO 8601 format (YYYY-MM-DD HH:MM:SS)  | end time of recording streaming |
| path | TEXT|  -  | the path of the saved recording |


## Additional Information and usefull links for testing 

Some playable stream urls for TV and Radio which have permissions to read from our application:

|     Name       | Keyname  |  type  | url  |
|-------------| :-----:| :--------------:| :-----:|
| RTV Murcia | es-mur--03|    TV  | http://rtvmurcia_01-lh.akamaihd.net/i/rtvmurcia_1_0@507973/master.m3u8 |
|   Kool London Radio  |     uk-koo--01    |   TV  |  http://w10.streamgb.com:1935/kool/kool/playlist.m3u8   |
|  MAD TV Greece   |     gr-mad--03    |   TV  |   https://itv.streams.ovh/magictv/magictv/playlist.m3u8  |
|   Music Top TV  |     ar-top--01    |   TV  |   http://live-edge01.telecentro.net.ar/live/msctphd-720/playlist.m3u8  |
|    Kuriakos Music  |  us-kmus-01     |  TV   | http://c2.manasat.com:1935/kmusic/kmusic3/FluxusTV.m3u8?fluxustv.m3u8   |
|  Radio 3   |    es-rn3--01     |   radio  |  http://hlsliveamdgl0-lh.akamaihd.net/i/rnerne3_1@793568/index_32_a-p.m3u8   |
|   Rock FM  |     es-rock-01    |  radio   |   http://rockfmlive.mdc.akamaized.net/strmRCFm/userRCFm/playlist.m3u8  |
|  RastaPank UOC   |     gr-rstpk-1    |  radio   |   http://rs.radio.uoc.gr:8000/uoc_64.mp3  |
|   Kritikorama  |     gr-kriti-2    |  radio   | http://46.4.37.132:9382/;    |
|   Radio 21 Hannover  |   de-hann-02      |   radio  |  http://api.new.livestream.com/accounts/22300508/events/6675945/live.m3u8   |

