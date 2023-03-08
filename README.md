# zoffline-helper

Scripts to configure Zwift client (for Windows) to use zoffline, connect to Strava and download Zwift profile.

## To install zwift-offline:

* Download **zoffline_1.0.XXXXXX.exe** from https://github.com/zoffline/zwift-offline/releases/latest
* Download **zoffline_helper.zip** from https://github.com/oldnapalm/zoffline-helper/releases/latest
* Run **configure_client**.
* Run **zoffline_1.0.XXXXXX** and allow it in Windows Firewall.
  * Once run, zoffline will create a ``storage`` directory in the same folder it's in to store your Zwift progress.
* Keep zoffline window open and run Zwift.
  * If Zwift launcher was already open (icon in taskbar tray), close it and run Zwift again.

#### Enabling/Disabling zwift-offline

To use Zwift online like normal, open the **hosts** shortcut and comment out or remove the line with Zwift servers before starting Zwift.

## To upload activities to Strava (optional):

* Run **strava_auth** and allow it in Windows Firewall.
* Open http://localhost:8000/ and authorize.
* Move the resulting strava_token.txt into the ``storage\1`` directory.
* If testing, ride at least 300 meters, shorter activities won't be uploaded.

Join the **zoffline** Strava group https://www.strava.com/clubs/zoffline

## To download your Zwift profile (optional):

* Disable zwift-offline (see [Enabling/Disabling zwift-offline](https://github.com/oldnapalm/zoffline-helper#enablingdisabling-zwift-offline) above).
* Run **get_profile**, type your Zwift login (e-mail) and password.
* Move the resulting profile.bin and achievements.bin into the ``storage\1`` directory.
