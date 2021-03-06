#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import base64
import json

"""
	Python class from gurock's Python SDK: https://github.com/gurock/testrail-api
	
	My own modifications include:
		- making formatting consistent with the rest of my project.
	
	And most importantly:
		- swapping out urllib for requests cuz it's 9,612,984,987 times better (I forgot to mention that somewhere in a comment before)
	
"""


class APIClient:
	"""TestRail API binding for Python 3.x (API v2, available since
	TestRail 3.0)

	Learn more:

		http://docs.gurock.com/testrail-api2/start
		http://docs.gurock.com/testrail-api2/accessing

	Copyright Gurock Software GmbH. See license.md for details.
	"""
	def __init__(self, base_url):
		self.user = ''
		self.password = ''
		if not base_url.endswith('/'):
			base_url += '/'
		self.__url = base_url + 'index.php?/api/v2/'

	def send_get(self, uri, filepath=None):
		"""Issue a GET request (read) against the API.

		:param uri: The API method to call including parameters, e.g. get_case/1.
		:param filepath: The path and file name for attachment download; used only
		for 'by_id/:attachment_id'.
		:return: A dict containing the result of the request.
		"""
		return self.__send_request('GET', uri, filepath)

	def send_post(self, uri, data):
		"""Issue a POST request (write) against the API.

		:param uri: The API method to call, including parameters, e.g. add/1.
		:param data: The data to submit as part of the request as a dict; strings
				must be UTF-8 encoded. If adding an attachment, must be the
				path to the file.
		:return: A dict containing the result of the request.
		"""
		return self.__send_request('POST', uri, data)

	def __send_request(self, method, uri, data):
		url = self.__url + uri

		auth = str(
			base64.b64encode(
				bytes('%s:%s' % (self.user, self.password), 'utf-8')
			),
			'ascii'
		).strip()
		headers = {'Authorization': 'Basic ' + auth}

		if method == 'POST':
			if uri[:14] == 'add_attachment':  # add_attachment API method
				files = {'attachment': (open(data, 'rb'))}
				response = requests.post(url, headers=headers, files=files)
				files['attachment'].close()
			else:
				headers['Content-Type'] = 'application/json'
				payload = bytes(json.dumps(data), 'utf-8')
				response = requests.post(url, headers=headers, data=payload)
		else:
			headers['Content-Type'] = 'application/json'
			response = requests.get(url, headers=headers)

		if response.status_code > 201:
			try:
				error = response.json()
			except:  # response.content not formatted as JSON
				error = str(response.content)
			raise APIError('TestRail API returned HTTP %s (%s)' % (response.status_code, error))
		else:
			if uri[:15] == 'by_id/':  # Expecting file, not JSON
				try:
					open(data, 'wb').write(response.content)
					return (data)
				except:
					return ("Error saving attachment.")
			else:
				try:
					return response.json()
				except:  # Nothing to return
					# ...but do we want an empty dict or should we assume response.text will be good enough?
					return response.text

class APIError(Exception):
	pass


class APIValidationError(ValueError):
	pass
