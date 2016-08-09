#!/bin/bash

# validate configFile
if [ ! -r ${configFile} ]; then
	echo "error: config file missing (${configFile})"
fi

# read platformBase
platformBase=`grep platformBase /opt/webmodules/iac/conf/iac.conf | awk -F= '{print $2}'`
if [ -z "${platformBase}" ]; then
	echo "error: platformBase is NULL"
fi
export platformBase

# read apiBase
apiBase=`grep apiBase /opt/webmodules/iac/conf/iac.conf | awk -F= '{print $2}'`
if [ -z "${apiBase}" ]; then
	echo "error: apiBase is NULL"
fi
export apiBase

