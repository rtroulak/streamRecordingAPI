import unittest
import requests


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
        r = requests.post("http://127.0.0.1:5000/channel", data=payload)
        print(r)
        self.assertEqual(r.status_code, 200)

    def test_recording_add(self):
        payload = {
            "channel_id": 1,
            "start_time": "2020-03-15 01:10:13.960190",
            "end_time": "2020-03-15 01:40:13.960195",
            "path": "http://hlsliveamdgl1-lh.akama\nihd.net/i/hlsdvrlive_1@584096\n/index_0400_av-p.m3u8?sd=10&r"
                    "\nebase1=on"
        }
        r = requests.post(self.__api_base_url + self.__recording_url, data=payload)
        self.assertEqual(r.status_code, 200)

    def test_channel_update(self):
        payload = {
            "keyname": "gr-rstpk-3",
            "name": "RastaPank UOC ",
            "type": "radio",
            "url": "http://rs.radio.uoc.gr:8000/uoc_64.mp3"
        }
        channel = '/4'
        r = requests.put(self.__api_base_url + self.__channel_url + channel, data=payload)
        self.assertEqual(r.status_code, 200)

    def test_recording_update(self):
        payload = {
            "channel_id": 12,
            "end_time": "2021-03-15 01:40:13.960195",
            "path": "http://hlsliveamdgl1-lh.akama\nihd.net/i/hlsdvrlive_1@584096\n/index_0400_av-p.m3u8?sd=10&r"
                    "\nebase1=on",
            "start_time": "2021-03-15 01:10:13.960190",
        }
        recording = '/1'
        r = requests.put(self.__api_base_url + self.__recording_url + recording, data=payload)
        self.assertEqual(r.status_code, 200)

    def test_get_channel(self):
        channel = '/4'
        r = requests.get(self.__api_base_url + self.__channel_url + channel)
        self.assertEqual(r.status_code, 200)

    def test_get_channel_all(self):
        r = requests.get(self.__api_base_url + self.__channel_url)
        self.assertEqual(r.status_code, 200)

    def test_get_recording(self):
        recording = '/1'
        r = requests.get(self.__api_base_url + self.__recording_url + recording)
        self.assertEqual(r.status_code, 200)

    def test_get_recording_all(self):
        r = requests.get(self.__api_base_url + self.__recording_url)
        self.assertEqual(r.status_code, 200)

    def test_get_recording_channel(self):
        channel = '/1'
        r = requests.get(self.__api_base_url + self.__channel_url + channel + self.__recording_url)

        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRecordingRestApi)
    unittest.TextTestRunner().run(suite)
