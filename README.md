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

The code presented here will serve more as a starting point for your own project. Fiddle with an SNMP capable switch ? Light some LEDs ? Play a warning sound ? It all depends on your needs and hardware capability.

# 🖥️ Hardware I used

- Sound sensor from [PCB Artist](https://pcbartists.com/product/i2c-decibel-sound-level-meter-module/) (~$22)
- 1.28 inch round LCD screen from [Waveshare](https://www.waveshare.com/1.28inch-lcd-module.htm) (~$15)
- A Raspberry (I used a Pi 3 A+ for the record)
- (A network switch with SNMP support)

