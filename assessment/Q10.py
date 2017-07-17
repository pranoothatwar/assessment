from time import mktime
from datetime import datetime

print mktime(datetime.utctimetuple(datetime.strptime("20110830_1117","%Y%m%d_%H%M")))
