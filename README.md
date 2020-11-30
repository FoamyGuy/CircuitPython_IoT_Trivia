![image](https://github.com/mytechnotalent/CircuitPython_IoT_Trivia/blob/main/CircuitPython%20IoT%20Trivia%20ESP32-S2%20OLED%20Version.png?raw=true)

# CircuitPython IoT Trivia ESP32-S2 OLED Version
An IoT Trivia app that shows you how to take a JSON web API such as the opentdb.com API and stream and display it on a FeatherS2 in an OLED display.

* This direct code is a collaborative effort between @mytechnotalent on Twitter, mytechnotalent on GitHub, @MakeMyAndroidAp on Twitter, FoamyGuy on GitHub.

## Schematic
![image](https://github.com/mytechnotalent/CircuitPython_IoT_Trivia/blob/main/schematic.png?raw=true)

## Parts
[FeatherS2 - ESP32-S2 Feather Development Board](https://www.adafruit.com/product/4769)<br>
[Assembled Adafruit FeatherWing OLED - 128x32 OLED Add-on For Feather](https://www.adafruit.com/product/3045)<br>
[FeatherWing Doubler - Prototyping Add-on For All Feather Boards](https://www.adafruit.com/product/2890)

## Installation
```bash
git clone https://github.com/mytechnotalent/CircuitPython_IoT_Trivia.git
```

## Copy Files From Repo To FeatherS2
```bash
lib\
code.py 
secrets.py
SourceSansPro-Regular.bdf
SourceSansPro-Regular.bdf.license
trivia.json
test_wrap_nicely.py [ORIGINAL SOURCE: https://github.com/adafruit/Adafruit_CircuitPython_PyPortal/blob/master/adafruit_pyportal.py]
unittest.py [SOURCE: https://github.com/micropython/micropython-lib/blob/master/unittest/unittest.py]
wrap_nicely.py
call_wifi.py
fetch_question.py
display_helpers.py 
test_call_wifi.py
test_fetch_question.py
test_display_helpers.py 
```

## STEP 1: Modify secrets.py
Edit the `secrets.py` file with your credentials.

## STEP 2: Power Device
This is the FUN part where you get to fire up your new trivia device! 
When you see the question press the C button on the OLED which takes you to answer mode then press the A button to scroll to your answer choice and then press the C button again to lock in your answer.

## 24/7 Community Of Support
If you have any questions regarding this app or implementing your own version of this app please visit us in the CircuitPython Discord channel [HERE](https://discord.com/invite/5FBsBHU) and visit the `help-with-circuitpython` room.

## Run Tests in REPL
```bash
import unittest
unittest.main('test_wrap_nicely')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
