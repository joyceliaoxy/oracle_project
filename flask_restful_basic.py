from flask import Flask, request
from flask_restful import Resource, Api
from collections import OrderedDict


# restful Api
app = Flask(__name__)
api = Api(app)

class clean_string(Resource):
    def get(self, str1):
        return {'result': ''.join(OrderedDict.fromkeys(str1))}, 200

class clean_string_1(Resource):
    def get(self, str1):
        temp, temp1 = list(str1), []
        for item in temp:
            if item not in temp1:
                temp1.append(item)

        return {'result': ''.join(temp1)}, 200

class largest_block(Resource):
    def get(self, str2):
        temp, dict = list(str2), {}
        for char in temp:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1

        return {'result': dict.get(max(dict, key = dict.get))}, 200

class sort_string(Resource):
    def get(self, str3):
        temp = list(str3)
        temp.sort()
        return {'result': ''.join(temp)}, 200

class sort_string_1(Resource):
    def get(self, str3):
        temp, result = list(str3), []
        for i in range(0, len(temp)):
            m = min(temp)
            result.append(m)
            temp.remove(m)

        return {'result': ''.join(result)}, 200


api.add_resource(clean_string, '/clean_string/<string:str1>')
api.add_resource(clean_string_1, '/clean_string_1/<string:str1>')
api.add_resource(largest_block, '/largest_block/<string:str2>')
api.add_resource(sort_string, '/sort_string/<string:str3>')
api.add_resource(sort_string_1, '/sort_string_1/<string:str3>')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
