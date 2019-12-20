#! /bin/bash

# presence-detect.sh
# searches for the MAC address of known devices

# do arp_scan to get connected mac addresses
connectedDevices=$(sudo arp-scan -l)

knownDevices=("74:da:38:fc:eb:96" "xx:xx:xx:xx:xx:xx")

for device in "${knownDevices[@]}"
do
    if [[ "$connectedDevices" = *"$device"* ]]; then
        echo "$device is present!"
    else
        echo "$device is NOT present!"
    fi
done
