# zoffline-helper

Scripts to configure Zwift client (for Windows 10) to use zoffline server, connect to Strava and download Zwift profile.

## To install zwift-offline:

* Download **zoffline_1.0.XXXXX.exe** from https://github.com/zoffline/zwift-offline/releases
* Download **zoffline_helper.zip** from https://github.com/oldnapalm/zoffline-helper/releases
* Run **configure_client**.
* Run **zoffline_1.0.XXXXX** and allow it in Windows Firewall.
  * Once run, zoffline will create a ``storage`` directory in the same folder it's in to store your Zwift progress.
* Keep zoffline window open and run Zwift.
  * If Zwift launcher was already open (icon in taskbar tray), close it and run Zwift again.

#### Enabling/Disabling zwift-offline

To use Zwift online like normal, open the **Edit hosts** shortcut and comment out or remove the line with Zwift servers before starting Zwift.

## To upload activities to Strava (optional):

* Run **strava_auth** and allow it in Windows Firewall.
* Open http://localhost:8000/ and authorize.
* Move the resulting strava_token.txt into the ``storage\<player_id>`` directory.

Only activities **longer than 5 km** will be uploaded to Strava.

## To download your Zwift profile (optional):

* Run **get_profile**, type your Zwift login (e-mail) and password.
* Move the resulting profile.bin into the ``storage`` directory (it will be moved to ``storage\player_id`` when you run zwift-offline).

zwift-offline **must be disabled** (without Zwift servers in hosts file) before running get_profile.

## To enable ghosts (optional):

* Create a file called "enable_ghosts.txt" inside the ``storage`` directory.
* When you save an activity the ghost will be saved in ``storage\<player_id>\ghosts``.
* Copy ghost files to ``storage\<player_id>\ghosts\load`` and they will be loaded in the next activity.

You must ensure that the loaded ghost files are from the same map and route you are going to ride.
