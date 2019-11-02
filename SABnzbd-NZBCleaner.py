import sys
import re

try:
    (scriptname, nzbname, postprocflags, category, script, prio, downloadsize, grouplist, showname, season, episodenumber, episodename) = sys.argv
    nzbname = re.sub('(?i)[._-](obfuscated|scrambled|nzbgeek|chamele0n|buymore|asrequested)$', '', nzbname, re.IGNORECASE)
    nzbname = re.sub('(?i)[._-](obfuscated|scrambled|nzbgeek|chamele0n|buymore|asrequested)$', '', nzbname, re.IGNORECASE)
except:
    sys.exit(1)

print "1"
print nzbname
print
print
print
print
print

sys.exit(0)
