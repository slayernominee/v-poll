MONGO_DB_HOST = 'localhost'
MONGO_DB_PORT = 27017
MONGO_CONNECTION_STRING = f"mongodb://{MONGO_DB_HOST}:{MONGO_DB_PORT}"

# ---------------------

from flask import Flask, request, redirect, abort
from flask_cors import CORS, cross_origin
from time import time
from ua_parser import user_agent_parser
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
mo = MongoClient(MONGO_CONNECTION_STRING)

def logRequest(request, response_code: int, response_answer: str = None) -> str:
    """log a request in the db

    Args:
        request (_type_): the flask request
        response_code (int): http coded e.g. 200, 404
        response_answer (str, optional): a custom message that will be displayed in the db

    Returns:
        str: the id of the logged request
    """
    requests_collection = mo['polls']['requests']
    ua_dict = user_agent_parser.Parse(request.headers.get('User-Agent'))
    try:
        json_data = request.json
    except:
        json_data = None
    data = {
        'timestamp': time(),
        'ip': request.remote_addr,
        'user-agent': ua_dict,
        'method': request.method,
        'endpoint': request.path,
        'data': {
            'json': json_data,
            'form': 'planned feature',
            'params': 'planned feature'
        },
        'response': {
            'code': response_code,
            'answer': response_answer
        }
    }
    r = requests_collection.insert_one(data)
    return r.inserted_id


# API Routes

@app.route('/api/getPoll/<id>', methods=['POST'])
@cross_origin()
def getPoll(id):
    try:
        hex_id = int(id, 16)
    except:
        logRequest(request, 400, 'id is not hex')
        return abort(400)
    
    poll = (mo['polls']['polls'].find_one({'_id': ObjectId(id)}))
    if poll:
        poll['_id'] = id
        poll['id'] = id
        newpoll = poll
        for i, q in enumerate(poll['questions']):
            if type(q) == ObjectId:
                question = mo['polls']['questions'].find_one({'_id': q})
                question['id'] = str(q)
                question['_id'] = str(q)
                newpoll['questions'][i] = question
        logRequest(request, 200, 'success')
        return (newpoll)
    else:
        logRequest(request, 404, 'no poll with this id')
        return abort(404)

@app.route('/api/voteable/<id>', methods=['POST'])
@cross_origin()
def voteable(id):
    try:
        hex_id = int(id, 16)
    except:
        logRequest(request, 400, 'id is not hex')
        return abort(400)
    
    poll = mo['polls']['polls'].find_one({'_id': ObjectId(id)})
    if poll == None:
        logRequest(request, 404, 'no poll with this id')
        return abort(404)
    protection = poll['protection']
    
    other_answers_from_ip_for_this_poll = mo['polls']['answers'].find_one({'poll_id': id})
    if other_answers_from_ip_for_this_poll:
        already_voted = True
    else:
        already_voted = False
        
    if protection and already_voted:
        logRequest(request, 200, 'can not vote for this poll')
        return {'voteable': False}
    else:
        logRequest(request, 200, 'can vote for this poll')
        return {'voteable': True}
    

@app.route('/api/postPoll/<id>', methods=['POST'])
@cross_origin()
def postPoll(id):
    try:
        hex_id = int(id, 16)
    except:
        logRequest(request, 400, 'id is not hex')
        return abort(400)
    if 'answers' not in request.json:
        logRequest(request, 400, 'answers not in json')
        return abort(400)
    
    poll = mo['polls']['polls'].find_one({'_id': ObjectId(id)})
    if poll == None:
        logRequest(request, 404, 'no poll with this id')
        return abort(404)
    protection = poll['protection']
    
    other_answers_from_ip_for_this_poll = mo['polls']['answers'].find_one({'poll_id': id})
    if other_answers_from_ip_for_this_poll:
        already_voted = True
    else:
        already_voted = False
    
    if protection and already_voted:
            logRequest(request, 403, 'already voted')
            return 'already voted', 403
    
    request_log_id = logRequest(request, 200, 'success')
    
    r = mo['polls']['answers'].insert_one({
        'poll_id': id,
        'timestamp': time(),
        'ip': request.remote_addr,
        'answers': request.json['answers'],
        'request_log_id': request_log_id
    })
        
    return 'ok'

@app.route('/api/getPopularPolls', methods=['POST'])
@cross_origin()
def getPopularPolls():
    popular_polls = mo['polls']['polls'].find({'public': True}).sort('votes', -1).limit(9)
    popular_poll_list = []
    for x in popular_polls:
        popular_poll_list.append({
            'title': x['title'],
            'description': x['description'],
            'id': str(x['_id'])
        })
            
    return {'popular_polls': popular_poll_list}
    
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
