import sys, os, time, subprocess, uno
from com.sun.star.beans import PropertyValue
def pv(n,v):
    p=PropertyValue(); p.Name=n; p.Value=v; return p
src=os.path.abspath(sys.argv[1]); pdf=os.path.abspath(sys.argv[2])
port=2002+os.getpid()%500
prof='/tmp/lo_prof_%d'%os.getpid()
proc=subprocess.Popen(['soffice','--headless','--invisible','--nologo','--norestore','-env:UserInstallation=file://'+prof,f'--accept=socket,host=localhost,port={port};urp;'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
ctx=uno.getComponentContext(); res=ctx.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',ctx)
for i in range(60):
    try: c=res.resolve(f'uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext'); break
    except Exception: time.sleep(1)
desk=c.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',c)
doc=desk.loadComponentFromURL(uno.systemPathToFileUrl(src),'_blank',0,(pv('Hidden',True),))
idx=doc.getDocumentIndexes()
for i in range(idx.getCount()): idx.getByIndex(i).update()
doc.getTextFields().refresh()
for i in range(idx.getCount()): idx.getByIndex(i).update()
doc.storeToURL(uno.systemPathToFileUrl(pdf),(pv('FilterName','writer_pdf_Export'),))
if len(sys.argv)>3:  # also save docx with populated TOC
    doc.storeToURL(uno.systemPathToFileUrl(os.path.abspath(sys.argv[3])),(pv('FilterName','MS Word 2007 XML'),))
doc.close(True)
try: desk.terminate()
except Exception: pass
proc.wait(timeout=30)
print('ok',pdf)
