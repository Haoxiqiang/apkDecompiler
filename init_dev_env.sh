#!/bin/bash

dex2jar=dex2jar

if [[ -d "${dex2jar}" ]]; then
    echo -e "INFO: dex2jar already downloaded. Source folder is found\n"
else
    git submodule update --init --force
fi

cd ${dex2jar}

./gradlew clean && ./gradlew distZip
# ln dex-tools
ln -s ./dex-tools/build/scripts/dex-tools dex-tools

sys=`uname -s`
ln -s ./jad-tools/${sys}/jad jad