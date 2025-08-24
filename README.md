# 🔊➜💥 dB to LCD to Action
> Measure dB level, display, and take action.

My first project published on [r/raspberry_pi](https://www.reddit.com/r/raspberry_pi/) got very nice feedback and made it to the Top 10 of 2025 posts.
Published with the tongue in cheek title ["Raspberry Pi decibel monitor + SNMP = instant parental justice"](https://www.reddit.com/r/raspberry_pi/comments/1moiw8k/raspberry_pi_decibel_monitor_snmp_instant/), it
showed how I hooked a dB sensor and an LCD screen to throttle bandwidth on the network switch to a loud gaming kid. _"More yell ? More ping :Þ"_ <br/>
Here are all the details and code.

<img width="1178" height="385" alt="Sans-titre-3" src="https://github.com/user-attachments/assets/5417b710-e914-4440-8563-bf96aec9ab13" />

---

# 💡 Concept

This project has been a lot of fun _with_ my kid actually (details in the Reddit thread comments). The idea was the following :

- Measure noise level in dB
- Display noise level
- Take measure accordingly : throttle bandwidth on the network to induce lag if threshold surpassed

# ⚠️ Disclaimer : it won't work for you

Per popular demand I'm publishing all my code, but... It's not like there a magical universal command to adjust bandwidth on your home network switch. It's dependant on your
network switch, if capable at all.

The code presented here will serve more as a starting point for your own project. Light some LEDs ? Fiddle with an SNMP capable switch ? Play a warning sound ? It all depends on your needs and hardware capability.

# 🖥️ Hardware I used

- Sound sensor from [PCB Artist](https://pcbartists.com/product/i2c-decibel-sound-level-meter-module/) (~$22)
- 1.28 inch round LCD screen from [Waveshare](https://www.waveshare.com/1.28inch-lcd-module.htm) (~$15)
- A Raspberry (I used a Pi 3 A+ for the record)
- (A network switch with SNMP support)

# 🧩 Setup and code

Out of the box, the "measure and display" parts are fully functional. Everything can be configured via an `.env` file : copy [`.env-example`](https://github.com/ozh/db_lcd_action/blob/master/.env-example) and adjust.

* [`utils/sensor.py`](https://github.com/ozh/db_lcd_action/blob/master/utils/sensor.py) has the very simple code to measure dB level
* In [`utils/lcd.py`](https://github.com/ozh/db_lcd_action/blob/master/utils/lcd.py) you will find everything to display on the LCD screen. It generates an image on the fly with all the info, using a template image found in [`assets/db_levels`](https://github.com/ozh/db_lcd_action/tree/master/assets/db_levels)
* You will want to edit and customize [`utils/actions.py`](https://github.com/ozh/db_lcd_action/blob/master/utils/actions.py) to code what action you will want to take. There are placeholders
and messages logged to help you through it, but you will be on your own.<br/>
You will find the exact code I used to throttle and restore the bandwidth on my network switch but, again, this won't work for you.

# 📷 Pictures

Prototype :

<img width="960" height="843" alt="image" src="https://github.com/user-attachments/assets/38289c11-971e-431b-a6fb-7afccbb569be" />

# 📝 License

My second Python project 🎉 

Everything licensed under the WTF Public License. [![WTFPL](https://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png)](http://www.wtfpl.net/about/)
Feel free to do whatever the hell you want with it.
