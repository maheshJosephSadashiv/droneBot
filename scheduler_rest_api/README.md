# Flask

# Make sure that you have Python version 3.6 and above

* First install virtualenv `pip install virtualenv`
* Run `virtualenv venv` in the project root.
* Run `.\venv\Scripts\Activate`
* Run `pip install -r requirements.txt`
* Run `python db_init.py`
* Run `python app.py`

Go to  http://127.0.0.1:5000/  you should see success on the screen

## Endpoint to added data to db

`http://127.0.0.1:5000/setstatus`

```
curl -X POST \
  http://127.0.0.1:5000/setstatus \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 12d5cdcb-7842-0d36-0cfc-92d4b14594f2' \
  -d '[	
	{
	    "destination_x": 10,
	    "destination_y": 10,
	    "item_x": 2,
	    "item_y": 5
	},
		
	{
	    "destination_x": 1,
	    "destination_y": 1,
	    "item_x": 10,
	    "item_y": 3
	},
		{
	    "destination_x": 3,
	    "destination_y": 8,
	    "item_x": 10,
	    "item_y": 3
	},
		{
	    "destination_x": 8,
	    "destination_y": 3,
	    "item_x": 6,
	    "item_y": 3
	}
	
]'
```

## Endpoint to get data from db `http://127.0.0.1:5000/getstatus`

```
curl -X GET \
  http://127.0.0.1:5000/getstatus \
  -H 'cache-control: no-cache' \
  -H 'postman-token: 16f21aed-5239-2b47-0f9d-22ac8454c8ad'
```

### RESPONSE:
```
[
    {
        "assigned_drone": "Assigned to drone 0",
        "destination_x": 10,
        "destination_y": 10,
        "item_id": 1,
        "item_x": 2,
        "item_y": 5,
        "status": "Pending",
        "time": "2020-04-15T15:55:23.431320"
    },
    {
        "assigned_drone": "Assigned to drone 1",
        "destination_x": 1,
        "destination_y": 1,
        "item_id": 2,
        "item_x": 10,
        "item_y": 3,
        "status": "Pending",
        "time": "2020-04-15T15:55:23.434286"
    },
    {
        "assigned_drone": "Assigned to drone 0",
        "destination_x": 3,
        "destination_y": 8,
        "item_id": 3,
        "item_x": 10,
        "item_y": 3,
        "status": "Pending",
        "time": "2020-04-15T15:55:23.435113"
    },
    {
        "assigned_drone": "Assigned to drone 1",
        "destination_x": 8,
        "destination_y": 3,
        "item_id": 4,
        "item_x": 6,
        "item_y": 3,
        "status": "Pending",
        "time": "2020-04-15T15:55:23.435113"
    }
]
```
