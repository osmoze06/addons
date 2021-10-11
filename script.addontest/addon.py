import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
password    = addon.getSettings('password')

xbmcgui.Dialog().input('Enter Password', hashlib.md5(password.encode('utf-8')).hexdigest(), type=xbmcgui.INPUT_NUMERIC, option=xbmcgui.PASSWORD_VERIFY)
