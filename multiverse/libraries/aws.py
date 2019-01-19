from .repo import Repo
from .exception import MVCError
import config.aws as AWSC
import config.mail as MAIL
import boto3, uuid
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename

class AWS:

	@staticmethod
	def SESMailSend(props):
		status = False; content = {}
		try:
			fromaddr = props.get('source', MAIL.SOURCE)
			toaddr = props.get('to', '')
			subject = props.get('subject', '')
			text = props.get('text', '')
			html = props.get('html', '')
			client = boto3.client('ses',
			    region_name=AWSC.REGION,
			    aws_access_key_id=AWSC.ACCESS_KEY,
			    aws_secret_access_key=AWSC.SECRET_KEY
			)
			response = client.send_email(
				Source=fromaddr,
				Destination={
					'ToAddresses':[ toaddr ]
				},
				Message={
					'Subject':{
						'Data':subject,
						'Charset':'UTF-8'
					},
					'Body':{
						'Text':{
							'Data':text,
							'Charset':'UTF-8'
						},
						'Html':{
							'Data':html,
							'Charset':'UTF-8'
						}
					}
				}
			)
			print response
			content['props'] = props
			status = True
			content['code'] = 'USER:SUCCESS:EMAIL_SENT'
		except MVCError as e: content['code'] = str(e)
		except ClientError as e: content['exception'] = e.response
		except Exception as e: content['exception'] = MVCError.catch(e)
		return Repo.api('libraries:aws#SESMailSend', status, content)

	@staticmethod
	def S3MediaUpload(props):
		status = False; content = {'code':'PLATFORM:ERROR:MEDIA_NOT_UPLOADED'}
		try:
			key = props.get('key', '')
			body = props.get('body')
			if len(key) == 0 or body is None:
				raise MVCError('REQUEST:ERROR:EMPTY_INPUT')
			client = boto3.client('s3',
			    region_name=AWSC.REGION,
			    aws_access_key_id=AWSC.ACCESS_KEY,
			    aws_secret_access_key=AWSC.SECRET_KEY
			)
			response = client.put_object(
			    ACL='public-read',
			    Body=body,
			    Bucket=AWSC.BUCKET,
			    Key=secure_filename(key),
			)
			content['props'] = props
			content['response'] = response
			status =  response.get('ResponseMetadata', {}).get('HTTPStatusCode', '404') == '200'
			content['code'] = 'PLATFORM:SUCCESS:MEDIA_UPLOADED'
		except MVCError as e: content['code'] = str(e)
		except ClientError as e:
			print e.response
			content['exception'] = e.response
		except Exception as e:
			print e
			content['exception'] = str(e)
		return Repo.api('libraries:aws#S3MediaUpload', status, content)

	
	@staticmethod
	def S3MediaRemove(props):
		status = False; content = {'code':'PLATFORM:ERROR:MEDIA_NOT_REMOVED'}
		try:
			key = props.get('key', '')
			if len(key) == 0:
				raise MVCError('REQUEST:ERROR:EMPTY_INPUT')
			client = boto3.client('s3',
			    region_name=AWSC.REGION,
			    aws_access_key_id=AWSC.ACCESS_KEY,
			    aws_secret_access_key=AWSC.SECRET_KEY
			)
			response = client.delete_object(
			    Bucket=AWSC.BUCKET,
			    Key=secure_filename(key)
			)
			content['props'] = props
			content['response'] = response
			status = response.get('ResponseMetadata', {}).get('HTTPStatusCode', '404') == '204'
			content['code'] = 'PLATFORM:SUCCESS:MEDIA_REMOVED'
		except MVCError as e: content['code'] = str(e)
		except ClientError as e:
			print e
			content['exception'] = e.response
		except Exception as e: 
			print e
			content['exception'] = str(e)
		return Repo.api('libraries:aws#S3MediaRemove', status, content)