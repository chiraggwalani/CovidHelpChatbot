from flask import Flask, request, make_response, jsonify
import json
import os
from flask_cors import cross_origin
import Excel
from datetime import datetime	

# initialize the flask app
app = Flask(__name__)
# default route
@app.route('/')
def index():
    return 'Hello World'
@app.route('/webhook', methods=['POST'])

def webhook():

    req = request.get_json(silent=True, force=True)
    
    res = processRequest(req)

    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

# processing the request from dialogflow
def processRequest(req):
    
    sessionID=req.get('responseId')

    result = req.get("queryResult")
    parameters = result.get("parameters")
	
    helpitems=''
    res_name=''
    no_of_beds=''
    bed_type=''
    city=''
    mobile_no=''
    v_person=''
	
    for data in result['outputContexts']:
       if 'helpitems' in  data['parameters']:
           helpitems=data['parameters']['helpitems']
       if 'res_name' in  data['parameters']:
           res_name=data['parameters']['res_name']
       if 'no_of_beds' in  data['parameters']:
           no_of_beds=data['parameters']['no_of_beds']
       if 'bed_type' in  data['parameters']:
           bed_type=data['parameters']['bed_type']
       if 'city' in  data['parameters']:
           city=data['parameters']['city']  
       if 'mobile_no' in  data['parameters']:
           mobile_no=data['parameters']['mobile_no']   
       if 'v_person' in  data['parameters']:
           v_person=data['parameters']['v_person']   
	
    data={			
			'Help Item': helpitems,
			'Resource Name':res_name,
			'Available Bed/Cylinder/Recovery Date':no_of_beds,
			'Type':bed_type,
			'City':city,
			'Contact No':mobile_no,
			'Verified By' :v_person,
			'Verified On' :datetime.now().isoformat("#","seconds"),
		}
    x=Excel.write(data)
    print(x)

    fulfillmentText="Thaks for helping us Do you have any other leads?"
    return {
            "fulfillmentText": fulfillmentText
        }
    
# run the app
if __name__ == '__main__':
   app.run()
