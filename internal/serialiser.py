import json
from  pydantic import BaseModel


class CustomType(BaseModel):
    id: int
    item_name: str
    guid: str
    description: str

    def toJSON(self):
        '''
        Serialize the object custom object
        '''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def get_json_data():
    '''
    Convert string array to json array
    '''
    result = []
    for item in data:
        obj = CustomType("title(n)",item)
        result.append(json.loads(obj.toJSON()))

    return json.dumps(result)