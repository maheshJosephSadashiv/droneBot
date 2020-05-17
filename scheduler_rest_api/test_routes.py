from flask import Flask, request, Blueprint
import json
from routes import bp


def test_base_route():
    app = Flask(__name__)
    app.register_blueprint(bp)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Success'
    assert response.status_code == 200


def test_post_route__success():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(bp)
    client = app.test_client()

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = [        
        {
            
        "destination_x": 30,
	    "destination_y": 24,
	    "item_x": 22,
	    "item_y": 50
    },
    {
	    "destination_x": 56,
	    "destination_y": 2,
	    "item_x": 30,
	    "item_y": 33
	}
    ]

    url = '/setstatus'

    response = client.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 200

def test_get_route_success():
    app = Flask(__name__)
    app.register_blueprint(bp)
    client = app.test_client()
    url = '/getstatus'

    response = client.get(url)
    assert response.status_code == 200
