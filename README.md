# What is Hustlebot-5000?

Hustlebot-5000 is your best friend for defeating the capitalist overlord pigs (may their steaks now and forever be overcooked).

## A bit more, please?

Picture this scenario:

- You're a remote (or partially remote) worker.
- You primarily work on your computer.
- Your capitalist overlord pigs monitor your computer's "uptime" or "away status", probably by measuring when was the last time you typed something or moved your mouse.
- Your capitalist overlord pigs have locked down things like scripts or PowerShell, easy-to-use tools that jiggle your mouse or whatnot.
- You, like most workers, don't actually have forty hours of work to do, and you'd rather be doing other things than pretending to work.
- You would like nothing more than to GET OUT OF THIS UNCEASING HELL.

If this is you...you're in luck! You just stumbled upon your way out of this capitalist dystopian nightmare, and it's not going to cost you a thing (except maybe a small bit; read on to find out more).

## The actual technical explanation

The code on this repository gets loaded onto a [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/), a very small, very cheap computer (actually, a microcontroller, but who's nitpicking?). It costs about $5.

The code turns the Pico into a keyboard, in a way. It tells the computer that it's a Microsoft Wired Keyboard, in exactly the same way that other such USB devices do. In fact, from the computer's point of view, the Pico that you just plugged in is absolutely identical to other USB keyboards.

And then...then, the fun begins.

Ten seconds after you plug in the Pico, it'll start TYPING. It's actually typing stuff from a spec that's used to evaluate circuit boards. Very boring stuff. But it looks professional.

And it the Pico will just do that, forever.

From the point of view of your capitalist overlord pigs, it looks like you're being wildly productive, typing and typing and never stopping. Hell, they'll think that you're peeing in your pants as you type, because you're just such a dedicated worker and you never stop. Meanwhile, you're actually playing Zelda or taking a nap.

It's a win-win!

## How do I make it go?

First, get yourself a Raspberry Pi Pico.

Download the latest version of CircuitPython, [which is available here](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython).

Install CircuitPython onto the Pico [by following these instructions](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython).

Copy and paste all of the files in this repository onto the Pico [by following these instructions](https://learn.adafruit.com/welcome-to-circuitpython/the-circuitpy-drive). Overwrite the files on the Pico if necessary.

Open a text editor, wait 10 seconds, and hold on to your hat.

If you want to edit the code, you'll have to put the Pico into BOOTSEL mode and upload [this flash nuke onto it](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython#flash-resetting-uf2-3083182). After that, start from the very top of these instructions again.

### Happy Hustlebotting!
