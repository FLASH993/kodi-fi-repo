import xbmc
import xbmcgui

xbmc.executebuiltin('RunAddon(plugin.program.openwizard)')
xbmcgui.Dialog().ok("Kodi-Fi Installer", "Launching OpenWizard to install your build...")
