# OverStim
[Click here for download instructions](https://github.com/Cyber-Kitty/OverStim/releases)

Controls your vibrator/vibrating toy based on what's happening in Overwatch 2, using computer vision. Won't trigger anti-cheat, because all it's doing is recording the screen like Discord screenshare and OBS does.

**Before Playing:** *Ensure you have edited the config.ini to your preferences for a more personalized experience!*

Requires [Intiface Central v2.3.0](https://intiface.com/central/](https://github.com/intiface/intiface-central/releases/tag/v2.3.0)  if you want to use it with a toy.

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
  - **Hacked by Sombra:** Disable all vibes for hacked duration. (option in config to instead make this randomly vibrate or do nothing)**
- **Widowmaker:**
  - **Vibrate while Zoomed in as Widowmaker:** +13% intensity while active
  - **Vibrate while Widowmaker's Ultimate is active:** +13% intensity while active
  - **Vibrate when Widowmaker's poison bomb is TRIGGERED!:** +22% intensity while the opponent is taking damage.


Optional Settings (all disabled by default):
- **Saved someone:** +50% intensity for 4 seconds
- **Being beamed by Mercy:** +30% intensity while active
- **Being orbed by Zenyatta:** +30% intensity while active
- **Hacked by Sombra:** Sombra controls your vibrator for the hacked duration (random vibes. Or an option in config to instead make this disable vibrations or do nothing)*

**Join the Discord:** (https://discord.gg/AVpcVhQQhu)
*Here, you can talk to us about features you want or bugs you encounter!*

Known Issues:
- Hero Auto Detection is Buggy in General - Will likely be removed from this fork
- **Widowmaker - Poison Bomb:**
  - Sometimes when your poison bomb is triggered, the detection fails. (This is due to it moving around your hud when you look around. If you are moving too fast it wont catch a frame with it in time)
    - *Adjust the WIDOW_BOMB_DISCONNECT_BUFFER: to experiment with this window of capturing the frame. Though keep in mind I have selected default values that seem to perform the best*
- Some features won't work with colorblind settings enabled.
- Doesn't work at aspect ratios other than 16:9.
- High latency to the game server causes Mercy's beam to reconnect to people slower when switching beam types. This can cause temporary gaps in vibration.
- Only Windows is officially supported.
