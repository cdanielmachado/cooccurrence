#!/bin/bash

curl https://oc.embl.de/index.php/s/uQ0N1ofipNFdoCd/download --output ancestrality.zip
curl https://oc.embl.de/index.php/s/MOMmYmpxcIzBxZJ/download --output communities.zip
curl https://oc.embl.de/index.php/s/SbhoQa9YJoa748V/download --output data.zip
curl https://oc.embl.de/index.php/s/PdSjEbnAQMOv7yy/download --output simulation.zip

unzip ancestrality.zip
unzip communities.zip
unzip data.zip
unzip simulation.zip

rm ancestrality.zip
rm communities.zip
rm data.zip
rm simulation.zip
rm -rf __MACOSX/
