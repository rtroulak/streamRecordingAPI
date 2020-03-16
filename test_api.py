import unittest
import requests
import pytest

pytest.channel_id = 0
pytest.recording_id = 0


class TestRecordingRestApi(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestRecordingRestApi, self).__init__(*args, **kwargs)
        self.__api_base_url = "http://127.0.0.1:5000"
        self.__channel_url = "/channel"
        self.__recording_url = "/recording"

    def test_channel_add(self):
        payload = {
            "keyname": "gr-rstpk-3",
            "name": "RastaPank UOC ",
            "type": "radio",
            "url": "http://rs.radio.uoc.gr:8000/uoc_64.mp3"
        }
        r = requests.post(self.__api_base_url + self.__channel_url, json=payload)
        pytest.channel_id = r.json()["id"]
        self.assertEqual(r.status_code, 200)

    def test_recording_add(self):
        payload = {
            "channel_id": pytest.channel_id,
            "start_time": "2020-03-15 01:10:13.960190",
            "end_time": "2020-03-15 01:40:13.960195",
            "path": "/recording/"
        }
        r = requests.post(self.__api_base_url + self.__recording_url, json=payload)
        pytest.recording_id = r.json()["id"]
        self.assertEqual(r.status_code, 200)

    def test_get_channel_all(self):
        r = requests.get(self.__api_base_url + self.__channel_url)
        self.assertEqual(r.status_code, 200)

    def test_get_channel(self):
        channel = '/' + str(pytest.channel_id)
        r = requests.get(self.__api_base_url + self.__channel_url + channel)
        self.assertEqual(r.status_code, 200)

    def test_channel_update(self):
        payload = {
            "keyname": "gr-rstpk-3",
            "name": "RastaPank UOC ",
            "type": "radio",
            "url": "http://rs.radio.uoc.gr:8000/uoc_64.mp3"
        }
        channel = '/' + str(pytest.channel_id)
        r = requests.put(self.__api_base_url + self.__channel_url + channel, json=payload)
        self.assertEqual(r.status_code, 200)

    def test_get_recording_all(self):
        r = requests.get(self.__api_base_url + self.__recording_url)
        self.assertEqual(r.status_code, 200)

    def test_get_recording(self):
        recording = '/' + str(pytest.recording_id)
        r = requests.get(self.__api_base_url + self.__recording_url + recording)
        self.assertEqual(r.status_code, 200)

    def test_get_recording_channel(self):
        channel = '/' + str(pytest.recording_id)
        r = requests.get(self.__api_base_url + self.__channel_url + channel + self.__recording_url)

        self.assertEqual(r.status_code, 200)

    def test_recording_update(self):
        payload = {
            "channel_id": pytest.channel_id,
            "end_time": "2021-03-15 01:40:13.960195",
            "path": "/recording/",
            "start_time": "2021-03-15 01:10:13.960190",
        }
        recording = '/' + str(pytest.recording_id)
        r = requests.put(self.__api_base_url + self.__recording_url + recording, json=payload)
        self.assertEqual(r.status_code, 200)

    def test_trash_recording(self):
        recording = '/' + str(pytest.recording_id)
        r = requests.delete(self.__api_base_url + self.__recording_url + recording)
        self.assertEqual(r.status_code, 200)

    def test_trash_channel(self):
        channel = '/' + str(pytest.channel_id)
        r = requests.delete(self.__api_base_url + self.__channel_url + channel)
        self.assertEqual(r.status_code, 200)

    def test_will_shutdown(self):
        r = requests.post(self.__api_base_url + '/shutdown')
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRecordingRestApi)
    unittest.TextTestRunner().run(suite)
