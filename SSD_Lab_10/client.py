import requests
from flask import jsonify


while(True):
    print()
    inp = input("Choose an option:\n1:Add student\n2:Fetch all students\n3:Update student\n4:Delete student\n5:Exit\n")
    if(inp == "1"):
        id = input("Enter id: ")
        name = input("Enter name: ")
        stream = input("Enter stream: ")
        data = {"id":id,"name":name,"stream":stream}
        response = requests.post('http://localhost:8000/create', json=data).content
        print()
        print(response.decode('utf-8'))

    elif(inp == "2"):
        response = requests.get('http://localhost:8000/read').content
        print()
        print(response.decode('utf-8'))
        
    elif(inp == "3"):
        id = input("Enter id: ")
        name = input("Enter name: ")
        stream = input("Enter stream: ")
        data = {"id":id,"name":name,"stream":stream}
        response = requests.put('http://localhost:8000/update',json=data).content
        print()
        print(response.decode('utf-8'))

    elif(inp == "4"):
        id = input("Enter id: ")
        response = requests.delete('http://localhost:8000/delete/{}'.format(id)).content
        print()
        print(response.decode('utf-8'))
    elif(inp == "5"):
        exit(1)