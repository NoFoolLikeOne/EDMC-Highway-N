# Highway-N plugin for EDMC
After every jump, this plugin locates the nearest Neutron star within a 200ly Radius and displays the name and distance. 
You can click on the name to copy it to the clipboard.

# NB

This is not ready for general release and is only made available for review by EDSM

# Installation
Copy the files to a directroy called Highway-N in your plugins directory

* Windows: `%LOCALAPPDATA%\EDMarketConnector\plugins` (usually `C:\Users\you\AppData\Local\EDMarketConnector\plugins`).
* Mac: `~/Library/Application Support/EDMarketConnector/plugins` (in Finder hold ⌥ and choose Go &rarr; Library to open your `~/Library` folder).
* Linux: `$XDG_DATA_HOME/EDMarketConnector/plugins`, or `~/.local/share/EDMarketConnector/plugins` if `$XDG_DATA_HOME` is unset.

You will need to re-start EDMC for it to notice the plugin.

# Use with caution
Some queries may take longer than it takes to start your next jump the plugin does not run queries in the background. This is not ready for general release

```
{
  "timestamp": "2017-09-01T23:36:44Z",
  "event": "FSDJump",
  "StarSystem": "Celaeno",
  "StarPos": [
    -81.094,
    -148.313,
    -337.094
  ],
  "SystemAllegiance": "",
  "SystemEconomy": "$economy_None;",
  "SystemEconomy_Localised": "None",
  "SystemGovernment": "$government_None;",
  "SystemGovernment_Localised": "None",
  "SystemSecurity": "$SYSTEM_SECURITY_low;",
  "SystemSecurity_Localised": "Low Security",
  "JumpDist": 17.279,
  "FuelUsed": 1.370331,
  "FuelLevel": 13.16893,
  "EDDMapColor": -65536
}```

