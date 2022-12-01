#1: Import libraries need for the test
from application.models import Entry
import datetime as datetime
import pytest
from flask import json
#Unit Test
#2: Parametrize section contains the data for the test
@pytest.mark.parametrize("entrylist",[
[ 1, 0, 1, 1, 0, 1, 0, 1, 1, 0], #Test integer arguments
[0.1, 0.2, 0.3, 0.4, 1, 0.2, 0.3, 0.4, 0.5, 1] #Test float arguments
])
#3: Write the test function pass in the arguments
def test_EntryClass(entrylist,capsys):
    with capsys.disabled():
        print(entrylist)
        now = datetime.datetime.utcnow()
        new_entry = Entry(
        HighBP= entrylist[0],
        HighChol = entrylist[1],
        BMI= entrylist[2],
        Smoker = entrylist[3],
        Stroke = entrylist[4],
        Diabetes = entrylist[5],
        HvyAlcoholConsump = entrylist[6],
        Sex = entrylist[7],
        Age = entrylist[8],
        prediction = entrylist[9],
        predicted_on= now)
        assert new_entry.HighBP == entrylist[0]
        assert new_entry.HighChol == entrylist[1]
        assert new_entry.BMI == entrylist[2]
        assert new_entry.Smoker == entrylist[3]
        assert new_entry.Stroke == entrylist[4]
        assert new_entry.Diabetes == entrylist[5]
        assert new_entry.HvyAlcoholConsump == entrylist[6]
        assert new_entry.Sex == entrylist[7]
        assert new_entry.Age == entrylist[8]
        assert new_entry.prediction == entrylist[9]
        assert new_entry.predicted_on == now


#4: Expected Failure Testing
# What if input contains 0 or negative values
# What if output is negative
@pytest.mark.xfail(reason="arguments <= 0")
@pytest.mark.parametrize("entrylist",[
[ 0, 1, 1, 1, 0, 0, 1, 0, 10, 1],
[ 0, 1, 1, 1, 0, 0, 1, 0, 10, 1],
[ 0, 1, 1, 1, 0, 0, 1, 0, 10, 1],
[ 0, 1, 1, 1, 0, 0, 1, 0, 10, 1],
[ 0, 1, 1, 1, 0, 0, 1, 0, 10, 1],
])
def test_EntryValidation(entrylist, capsys):
    test_EntryClass(entrylist, capsys)


#5: Test add API
@pytest.mark.parametrize("entrylist",[
[ 0, 1, 1, 1, 0, 0, 1, 0, 10, 1],
[0.1, 0.2, 0.3, 0.4, 1, 0.2, 0.3, 0.4, 0.5, 1],
])
def test_addAPI(client,entrylist,capsys):
    with capsys.disabled():
        #prepare the data into a dictionary
        data1 = { 
            'HighBP': entrylist[0],
            'HighChol' : entrylist[1],
            'BMI': entrylist[2],
            'Smoker' : entrylist[3],
            'Stroke' : entrylist[4],
            'Diabetes' : entrylist[5],
            'HvyAlcoholConsump' : entrylist[6],
            'Sex' : entrylist[7],
            'Age' : entrylist[8],
            'prediction' : entrylist[9]}
        #use client object to post
        #data is converted to json
        #posting content is specified
        response = client.post('/api/add',
        data=json.dumps(data1),
        content_type="application/json",)
        #check the outcome of the action
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        response_body = json.loads(response.get_data(as_text=True))
        assert response_body["id"]


#Test get API
@pytest.mark.parametrize("entrylist",[
[ 0, 0, 0, 0, 0, 0, 0, 0, 40, 1, 2],
[ 0, 1, 1, 1, 0, 0, 1, 0, 10, 1, 3]
])
def test_getAPI(client, entrylist, capsys):
    with capsys.disabled():   
        response = client.get(f'/api/get/{entrylist[10]}')
        ret = json.loads(response.get_data(as_text=True))
        #check the outcome of the action
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        response_body = json.loads(response.get_data(as_text=True))
        assert response_body["id"] == entrylist[10]
        assert response_body["HighBP"] == float(entrylist[0])
        assert response_body["HighChol"] == float(entrylist[1])
        assert response_body["BMI"] == float(entrylist[2])
        assert response_body["Smoker"] == float(entrylist[3])
        assert response_body["Stroke"] == float(entrylist[4])
        assert response_body["Diabetes"] == float(entrylist[5])
        assert response_body["HvyAlcoholConsump"] == float(entrylist[6])
        assert response_body["Sex"] == float(entrylist[7])
        assert response_body["Age"] == float(entrylist[8])
        assert response_body["prediction"] == float(entrylist[9])


#Test delete API
@pytest.mark.parametrize("entrylist", [
    [1, 1, 1, 1, 1, 1, 1, 1, 30, 0]
])
def test_deleteAPI(client, entrylist, capsys):
    with capsys.disabled():
        #prepare the data into a dictionary
        datal = {'HighBP': entrylist[0],
                 'HighChol': entrylist[1],
                 'BMI': entrylist[2],
                 'Smoker': entrylist[3],
                 'Stroke': entrylist[4],
                 'Diabetes': entrylist[5],
                 'HvyAlcoholConsump': entrylist[6],
                 'Sex': entrylist[7],
                 'Age': entrylist[8],
                 'prediction': entrylist[9]}
        #use client object  to post data  and converted to json
        response = client.post('/api/add', data=json.dumps(datal),
                    content_type='application/json',)
        response_body = json.loads(response.get_data(as_text=True))
        assert response_body['id']
        id = response_body['id']

        response2 = client.get(f'/api/delete/{id}')
        ret = json.loads(response2.get_data(as_text = True))

        # check the outcome of the action
        assert response2.status_code == 200
        assert response2.headers["Content-Type"] == 'application/json'
        response2_body = json.loads(response2.get_data(as_text = True))
        assert response2_body['result'] == 'ok'