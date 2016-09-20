import blackrum
import subprocess

sourcecode = """
npp ppp ppp pp
onp ppp ppp ppp pnp ppp ppp ppp pnp ppp ppp ppp pnp pp pp
ppp pppn ppp ppp ppp ppp npp ppn ppp ppp pnp ppp ppp ppp npp ppp ppp
ppp npp ppp pp
ppp pnp ppp ppp ppp pnp ppp npp ppp ppp ppp pnp ppp ppp ppp pnp ppp ppp
ppp pnp ppp ppp ppp pnp ppp ppp ppp npp pnp ppp nbb bbb bbb bbb bbb bbb
bbb mc
npp npp ppn mmm mmn nmm mmn mnpp npnm mnm mnp npp ppn mnp npp ppn mmn np
ppn mn
bbb bbb bbb bbb bbb bbb bb
nrn rnr nrn rnr nrn rnr nrn rn rnrn rnr nrnr nrnr
"""

# The above giberish translates to: print 'Hello, world!'
# Below command translates the gibberis to ^^^
# I want to run the output like raw python.

command = blackrum.evaluate(sourcecode) 

#out = subprocess.call(["python", "blackrum.py", "run.br"])
#out
#p = subprocess.Popen(['python', 'blackrum.py', 'work.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#out, err = p.communicate()
#code = out
#print out
#exec code
#exec out
