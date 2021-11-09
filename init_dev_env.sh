#!/bin/bash

dex2jar=dex2jar

if [[ -d "${dex2jar}" ]]; then
    echo -e "INFO: dex2jar already downloaded. Source folder is found\n"
else
    git submodule update --init --force
fi

cd ${dex2jar}
git checkout -f
rm ./gradle/wrapper/gradle-wrapper.properties

echo "#Thu Aug 16 13:56:17 CST 2018
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-5.6.2-all.zip

" > ./gradle/wrapper/gradle-wrapper.properties
./gradlew clean && ./gradlew distZip
rm -r ../dex-tools*
tar zxf ./dex-tools/build/distributions/dex-tools-*.zip
rm ./dex-tools/build/distributions/dex-tools-*.zip
mv ./dex-tools-* ../dex-tools
cd ..

sys=`uname -s`
ln -s ./jad-tools/${sys}/jad jad