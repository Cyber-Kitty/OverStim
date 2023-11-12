# OverStim
[Click here for download instructions](https://github.com/Cyber-Kitty/OverStim/releases)

Controls your Lovense toy or connected vibrator based on what's happening in Overwatch 2, using computer vision. Won't trigger anti-cheat, because all it's doing is recording the screen like Discord screenshare and OBS does.

Requires [Intiface Central 2.3.0](https://intiface.com/central/](https://github.com/intiface/intiface-central/releases/tag/v2.3.0)  if you want to use it with a toy.

Default Settings (all triggers can be disabled or have their intensities/durations changed in the config):
- **Elimination:** +30% intensity for 6 seconds
- **Assist:** +15% intensity for 3 seconds
- **Mercy:**
  - **Resurrect:** +100% intensity for 4 seconds
  - **Heal beam:** +10% intensity while active
  - **Damage boost beam:** +30% intensity while active
- **Zenyatta:**
  - **Harmony orb:** +15% intensity while active
  - **Discord orb:** +20% intensity while active
- **Sombra:**
  - **Hacked by Sombra:** Disables your toy for the hack duration. (Can be changed to control your toy randomly for the duration, or do nothing)
- **Widowmaker:**
  - **Vibrate while Zoomed in as Widowmaker:** +13% intensity while active
  - **Vibrate while Widowmakers Ultimate is active:** +60% intensity while active
  - **Vibrate when Widowmakers poison bomb is TRIGGERED:** +22% intensity while bomb damages opponent

Optional Settings (all disabled by default):
- **Saved someone:** +50% intensity for 4 seconds
- **Being beamed by Mercy:** +30% intensity while active
- **Being orbed by Zenyatta:** +30% intensity while active
- **Hacked by Sombra:** By default, the toy is disabled when you get hacked. (You can change it to do nothing or randomly vibrate)

Join the Discord!(https://discord.gg/AVpcVhQQhu) - Here you can get help and make suggestions.

Known Issues:
- Auto Detection is not working well. I will likely be removing this from this fork, but I may fix it too.
- **VIBE_FOR_WIDOW_BOMB:**
  - Detection sometimes fails due to the nature of detecting the moving hud element. Play around with WIDOW_BOMB_DISCONNECT_BUFFER in the config if you wish. But be aware I have chosen what I think is best by default.
- Some features don't work with colourblind settings enabled.
- Doesn't work at aspect ratios other than 16:9.
- High latency to the game server causes Mercy's beam to reconnect to people slower when switching beam types. This can cause temporary gaps in vibration.
- Only Windows is officially supported.
