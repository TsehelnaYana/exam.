class FlaskAppTests(unittest.TestCase):

	def setUp(self):
	    self.app = app.app.test_client()

        def test_app(self):
            r = self.app.get('/')
	    self.assertEqual(r.status, '200 OK')

	def test_sumOfAP(self):
	    self.assertEqual(r.data, 157)
	    self.assertIsNotNone(r.data)
	    self.assertGreater(r.data, 0)

if __name__ =='__main__':
	unittest.main()
