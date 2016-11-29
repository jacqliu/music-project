Pairing the Controller to your PC
=================================

The PS Move connects via two methods:

* **USB**: Used for Bluetooth pairing; can set rumble and LEDs, cannot read sensors
* **Bluetooth**: Used for wireless connectivity; can set rumble, LEDs and read sensors


Bluetooth pairing
-----------------

The ``psmovepair`` utility is used for Bluetooth pairing -- it will write the
Bluetooth host address of the computer it's running on to PS Move controllers
connected via USB.

It optionally takes a single command-line parameter that is an alternative
Bluetooth host address. For example, if you want to pair your PS Move controller
to your phone, but it does not have USB Host Mode, you can use this on your PC::

    ./psmovepair aa:bb:cc:dd:ee:ff

Where ``aa:bb:cc:dd:ee:ff`` is the Bluetooth host address of your phone. Note
that depending on the phone, you also need to run pairing code there.

Depending on the operating system, you might need to run the utility as
Administrator (Windows), enter your password (OS X) or run using ``sudo``
(Linux) to let the utility modify the system Bluetooth settings and whitelist
the PS Move for connection.

.. note::
   You only need to pair the controller to your PC once, from then on
   it will always try to connect to your PC. Only when you connect your
   controller to a PS3 or pair with another PC will you have to re-do
   the pairing process on your computer.


Connecting via Bluetooth
------------------------

Unplug the USB cable and press the PS button on the controller. The red status
LED will start blinking and should eventually remain lit to indicate a working
Bluetooth connection. If it continues blinking, it might not be paired via
Bluetooth, or - if you can see the connection on your computer - the battery
is low and needs charging via USB or a charger. To verify the connection,
check the Bluetooth devices list of your computer and see if there is an
entry for "Motion Controller".

On recent versions of OS X, a dialog might pop up asking for a PIN. Close it
and pair the controller again using ``psmovepair``. After that, it should
connect successfully.


Troubleshooting
---------------

Here are some advanced tips if you can't get pairing working out of the box:

Mac OS X
~~~~~~~~

If ``psmovepair`` doesn't work or you get a PIN prompt when you press the PS
button on your controller, follow these steps:

* Right after you run ``psmovepair`` write down the adress you find after
  "controller address:" in the form "aa:bb:cc:dd:ee:ff"
* Disable Bluetooth (or the modifications that follow won’t work)
* Wait for the Bluetooth process to quit (``pgrep blued``); repeat until nothing
  prints anymore (e.g. the process "blued" has quit) - this can take up to a minute
* Authorize the controller’s MAC address:
  ``sudo defaults write /Library/Preferences/com.apple.Bluetooth HIDDevices -array-add "<aa-bb-cc-dd-ee-ff>"``
  (where <aa-bb-cc-dd-ee-ff> is the MAC address you wrote down at 8.2 but with hyphens for separators)
* Enable Bluetooth again then press the PS button on the controller. The PIN request should
  not pop up this time and the Move should now appear in the bluetooth devices as "Motion Controller".


Ubuntu Linux
~~~~~~~~~~~~

If you wish to access the PSMove controller via USB or Bluetooth without
requiring root-level permissions then it is necessary to copy the
``contrib/99-psmove.rules`` file to ``/etc/udev/rules.d/``::

   sudo cp contrib/99-psmove.rules /etc/udev/rules.d/
   sudo udevadm trigger


Windows
~~~~~~~

You might have to try pairing multiple times for the Bluetooth connection to
work on Windows. Also, be sure to use the Microsoft Bluetooth Stack and do
not install any third party drivers (e.g. MotionInJoy) that would interfere
with proper operation of PS Move API on Windows.
