from requests import post

def test_ping():
    expected_output = '{"Receiver": "Cisco is the best!"}'
    output = post('http://localhost:8080/api/v1/ping', data={'url': 'http://ReceiverService:8080/api/v1/info'}).json()
    assert output == expected_output
