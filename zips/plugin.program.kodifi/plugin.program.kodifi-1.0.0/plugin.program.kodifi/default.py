
import xbmc
import xbmcaddon
import xbmcgui

ADDON_ID = 'plugin.program.openwizard'
BUILD_URL = 'https://flash993.github.io/kodi-fi-repo/builds.txt'

def openwizard():
    xbmc.executebuiltin('RunAddon({})'.format(ADDON_ID))
    xbmc.executebuiltin('Notification(Kodi-Fi, Launching OpenWizard with preloaded URL..., 4000)')
    xbmc.sleep(1000)
    xbmc.executebuiltin('Container.Refresh')

def main():
    try:
        addon = xbmcaddon.Addon(ADDON_ID)
        addon.setSetting('buildfile', BUILD_URL)
        openwizard()
    except:
        xbmcgui.Dialog().ok("Kodi-Fi Installer", "OpenWizard is not installed. Please install it first.")

if __name__ == '__main__':
    main()
