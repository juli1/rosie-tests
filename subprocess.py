import subprocess
subprocess.Popen('/bin/ls -l %s' % ('something',), shell=True)
