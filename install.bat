set PKG_PATH="C:\Program files\Cloudbase Solutions\Cloudbase-init\"
set PYLib=%PKG_PATH%\Python\Lib\site-packages
COPY .\baseopenstackservice.py %PYLib%\cloudbaseinit\metadata\services\baseopenstackservice.py
COPY .\writeinjectedfiles.py %PYLib%\cloudbaseinit\plugins\common\
COPY .\cloudbase-init.conf %PKG_PATH%\conf\
COPY .\cloudbase-init.conf %PKG_PATH%\conf\cloudbase-init-unattend.conf
COPY .\boot_telegraf.cmd %PKG_PATH%\LocalScripts
