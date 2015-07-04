import unittest
import json

from app import app


class TestPostFromAlexa(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_turn_on(self):
        request_body = {
            "session": {
                "new": True,
                "sessionId": "amzn1.echo-api.session.8dd5e3cc-b0e9-4dc4-9e78-cb7c76a07c44",
                "user": {
                    "userId": "amzn1.account.AHSMN72XJPRTGNUUYRUDD7EINGYQ"
                }
            },
            "version": "1.0",
            "request": {
                "intent": {
                    "slots": {
                        "action": {
                            "name": "action",
                            "value": "on"
                        }
                    },
                    "name": "turn"
                },
                "type": "IntentRequest",
                "requestId": "amzn1.echo-api.request.68c848f5-c3b0-4b74-9016-a8caf6333b3a"
            }
        }

        response = self.app.post('/',
                                data=json.dumps(request_body),
                                content_type='application/json')

        self.assertEqual(response.status, "200 OK")
        self.assertNotEqual(response.data, None)
        parsed_json = json.loads(response.data)
        self.assertNotEqual(parsed_json["response"]["outputSpeech"]["text"], "")

    def test_turn_off(self):
        request_body = {
            "session": {
                "new": True,
                "sessionId": "amzn1.echo-api.session.8dd5e3cc-b0e9-4dc4-9e78-cb7c76a07c44",
                "user": {
                    "userId": "amzn1.account.AHSMN72XJPRTGNUUYRUDD7EINGYQ"
                }
            },
            "version": "1.0",
            "request": {
                "intent": {
                    "slots": {
                        "action": {
                            "name": "action",
                            "value": "off"
                        }
                    },
                    "name": "turn"
                },
                "type": "IntentRequest",
                "requestId": "amzn1.echo-api.request.68c848f5-c3b0-4b74-9016-a8caf6333b3a"
            }
        }

        response = self.app.post('/',
                                data=json.dumps(request_body),
                                content_type='application/json')
        self.assertEqual(response.status, "200 OK")
        self.assertNotEqual(response.data, None)
        parsed_json = json.loads(response.data)
        self.assertNotEqual(parsed_json["response"]["outputSpeech"]["text"], "")