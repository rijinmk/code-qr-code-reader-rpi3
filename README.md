## QR code reader on a Raspberry Pi 3

This guide will show you how to create a QR code reader by using the `zbarlight` python library and `fswebcam` to take the picture. We wont be using `open cv` or any other image processing libraries. 

### What you'll need

* Raspberry Pi 2 / 3
* MicroSD Card with Raspbian on it ([Tutorial](https://github.com/rijinmk/guide-to-install-any-os-terminal-rpi3))
* A USB webcam 
* Micro USB cable
* Keyboard, Mouse, Monitor
* HDMI cable for the monitor

If you are using the Raspberry Pi headless (Without a monitor, keyboard or mouse), You will need to connect to the internet using the ethernet port (for Raspberry Pi 2) or through the Wifi (on a Raspberry Pi 3 [[Tutorial](https://github.com/rijinmk/guide-to-wifi-terminal-rpi3)] ) and then you will have to use [SSH](https://github.com/rijinmk/guide-to-ssh-rpi3) to connect to your Raspberry Pi. 

### Installation process 

Here onwards everything will be on the terminals. Press `CTRL + ALT + T` to open up the terminals. 

#### STEP 1 - Initial installations

We always have to keep the apt-get updated. 

```bash 
sudo apt-get update -y && sudo apt-get upgrade -y
```

This will take some time depending on your internet speed and also the amount of package's that are installed onto your Raspberry Pi's OS.

#### STEP 2 - Installing and running `fswebcam` 

You will need to install this to access the webcam from the commandline. To install this you will need to use `apt-get`. 

```bash
sudo apt-get install fswebcam
```

This will install fswebcam. Now insert your USB webcam, to check if it's connected, enter in the commad

```bash
ls /dev/ | grep video
```

If `video0` is the output that means you are good to go, The webcam is connected. Now enter: 

```bash
sudo fswebcam image.jpg
```

This will take a picture named `image.jpg`. To check if you have taken the image, Enter: 

```bash
ls | grep image
```

If you see a file named `image.jpg`, that means your web cam is working. But if your above output for `ls /dev/ | grep video` was something else, for example `video2`. We have to pass an additional argument to `sudo fswebcam image.jpg`. Which is: 

```bash
sudo fswebcam -d /dev/video2 image.jpg
```

There is one more argument that we pass through to this command which is `-q` which means `quite`, This is to avoid the extra wordings that come when the photo is being taken. 

#### STEP 3 - Installing `zbarlight`

This is the brain of our QR code reader. This library helps us to decode an image into their basic codes. 

First we have to install the following: 

```bash
sudo apt-get install libzbar0 libzbar-dev
```

Then we have to install the `zbarlight`

```bash 
sudo pip install zbarlight
```

After this you can run the `reader.py` python program that I have written to test if it works. But before you do that, we need create a folder named `qr_codes` right outside the `reader.py` file, This folder will store all the QR codes. 

This `reader.py` program does the following: 

* Runs the command `fswebcam -q image_name.ext`
* Checks if it has QR Codes 
* Stores the QR code onto the `qr_codes/` folder
* If there is no QR code present after we run it through `zbarlight`, the image is deleted. 
* Else the image stays there, and a `qr_code_messages.txt` file is created with the QR code message onto it. 
* This file seperates the messages with certain delimiters

This is all you need to do / know for the QR code reader to work, If you want the detailed explationation of the code, I will be writing it soon. 


