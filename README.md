# Network Anamoly Detecter

Detects unauthorized device connecting to your network and issue Email based Alert.

## Requirements

    python >= 3.13
    pip
    Gmail account

## Setup

Step 1: Clone this repo

    git clone https://github.com/Anandprabhu530/NetworkAnomalyDetector.git

Step 2: Install dependecies

    pip install pyshark python-dotenv

Step 3: Add your environment variables to a dotenv file
This code focuses on the Gmail alerts

    EMAIL_ADDRESS="abc123@gmail.com"

    #Password obtained from Gmail (Look below)
    EMAIL_PASSWORD="app_password"

    # list of know device MAC Address seperated by ","
    ADDRESS_LIST="aa:bb:cc:dd:ee,aa:vv:bb:nn:mm"

    FILE_NAME="abc.txt"
    RECIPIENTS="testuser01@gmail.com"

Step 4: Run both the sniffer.py and reader.py files indvidually

## Concept

This projects work by capturing ETH packets from pyshark and extracting source MAC Address.

    for packet in capture.sniff_continuously():
        if 'ETH' in packet:
            # rest of the code...

You can also consider using TCP packets here instead of ETH.
If a new unauthorized device is identified add it to log and sleep for a second (to prevent overload).

Issue Email alert only once for a single unauthorized device. This helps in reducing mail received for same device multiple times.

## Customizations

Before running the code know the interface that you need to capture

For Windows: run ipconfig to find available Interface adapters.

Alternatively you can use [tshar](https://www.wireshark.org/docs/man-pages/tshark.html) to find the same. You can install tshark with wireshark.

    tshark -D

**Important**

Before attempting to send any Email you need to verify that your account has 2-factor authentication enabled.
Add a new app in App security in your Google account page.
Copy the password and paste it in .env file.

And now you are good to go..

## Improvments

- More packet information can be captured like domain that you visit, data sent.
- Can integrate more features and add a dashboard.
- Can also take preventive measures once an unauthorized device is connected.
