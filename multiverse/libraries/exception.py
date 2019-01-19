import os, sys

class MVCError(Exception):

	@staticmethod
	def catch(e, printe = True):
		''' Handles command line exception displaying line error '''
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		if printe:
			print "___________________________________________________"
			print "| Exception: ", str(e)
			print "| ", exc_type, "\t", fname, "\t", exc_tb.tb_lineno
			print "|___________________________________________________"
		return {
			'message':str(e),
			'type':exc_type,
			'file':fname,
			'line':exc_tb.tb_lineno
		}