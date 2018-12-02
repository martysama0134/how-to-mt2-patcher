#################################
### crclist Maker
### created by martysama0134
import os
import zlib

_np = os.path.normpath
_j = os.path.join
def make_path(a, b):
	return _np(_j(a, b)).replace("\\", "/")

def get_crc32(filename):
	crc = 0
	with open(filename, "rb") as f:
		crc = zlib.crc32(f.read())
	return "%x" % (crc & 0xffFFffFF)

def get_mtime(filename):
	# http://support.microsoft.com/kb/167296
	# How To Convert a UNIX time_t to a Win32 FILETIME or SYSTEMTIME
	EPOCH_AS_FILETIME = 116444736000000000 # January 1, 1970 as MS file time
	HUNDREDS_OF_NANOSECONDS = 10000000
	return EPOCH_AS_FILETIME + long(os.path.getmtime(filename)) * HUNDREDS_OF_NANOSECONDS

input_folder = _np("client")
output_folder = _np("web")
output_version = _np("0.0.0.2")
output_fv = make_path(output_folder, output_version)
output_crclist = make_path(output_fv, "crclist")

file_list = []
for root, dir, files in os.walk(input_folder):
	for filename in files:
		file_elem = {}
		file_elem["path"] = make_path(root, filename)
		file_elem["real_path"] = file_elem["path"][len(input_folder)+1:].replace("/", "\\")
		# crc32 calculation
		file_elem["crc32"] = get_crc32(file_elem["path"])
		# size calculation
		file_elem["size"] = os.path.getsize(file_elem["path"])
		# mtime calculation
		mtime = get_mtime(file_elem["path"])
		file_elem["mtime1"] = mtime >> 32
		file_elem["mtime2"] = mtime & 0xFFffFFff
		# add in list
		file_list.append(file_elem)

# make path if missing
if not os.path.exists(output_fv):
	os.makedirs(output_fv)

# generate crclist
print("Generating crclist:")
with open(output_crclist, "wb") as f:
	for elem in file_list:
		buf = "%s %d %d %d %s\n" % (elem["crc32"], elem["size"], elem["mtime1"], elem["mtime2"], elem["real_path"])
		f.write(buf)
		print(buf.replace("\n", ""))

# generate lz files
ENABLE_LZ_GENERATION = True
if ENABLE_LZ_GENERATION:
	import subprocess
	print("Generating .lz:")
	for elem in file_list:
		filepath_in = make_path(input_folder, elem["real_path"])
		filepath_out = make_path(output_fv, elem["real_path"]) + ".lz"
		# create out dir
		dirpath_out = os.path.dirname(filepath_out)
		if not os.path.exists(dirpath_out):
			os.makedirs(dirpath_out)
		# create lz
		cmd = 'mt2lz pack "%s" "%s"' % (filepath_in, filepath_out)
		subprocess.call(cmd, shell=True)
		print(cmd)
#
