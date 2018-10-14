
from copy import deepcopy
from datetime import datetime
from flask import Flask, request
import json
import uuid

from mongo_utils import insert 

app = Flask(__name__)

@app.route("/add_up", methods=["POST"])
def add_up():

    run_id = str(uuid.uuid4()) 
    


    input = request.form
    print "Input: {}".format(input)

    t_stamp = str(datetime.utcnow())

    input_dict = {
                      "run_id": run_id, 
                      "t_stamp": t_stamp,
                      "input": dict(input),
                 }

    insert("inputs", input_dict)

    total = int(input["a"]) + int(input["b"]) 

    result = {"answer": str(total)}
    print "Result: {}".format(result)

    t_stamp = str(datetime.utcnow())
    insert("results", {
                        "run_id": run_id,
                        "t_steamp": t_stamp,
                        "result": deepcopy(result), # modifies result
                       }
          )

    return json.dumps(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
