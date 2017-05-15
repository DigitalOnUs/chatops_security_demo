import sys
import json,ast

from st2actions.runners.pythonrunner import Action

class MyAuthUser(Action):

    def run(self, secret_list , new_user, secret_file):
        
    	secret_list = ast.literal_eval(json.dumps(secret_list))	

    	new_user = new_user.encode("utf-8")

        if secret_list.has_key('users') :
            secret_list['users'].append(new_user)
        else :
            secret_list={'users':[new_user]}

        try:
            with open(secret_file,"w+") as myfile:
                myfile.write(str(secret_list).encode("utf-8"))

            return True
        except: 
            exit(1)
