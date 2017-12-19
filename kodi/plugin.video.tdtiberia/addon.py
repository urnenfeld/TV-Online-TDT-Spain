import sys
import os
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

import channelproviders
import icons

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')

thisAddon = xbmcaddon.Addon()

# Empty strings evaluate to False, but everything else evaluates to True. 
iconsWanted = thisAddon.getSetting('retrieve_icons') == 'true'
includeDisabled = thisAddon.getSetting('include_disabled_channels') == 'true'

# Paths
thisPluginPath=thisAddon.getAddonInfo('path')
resourcesPath=os.path.join(thisPluginPath, 'resources')
iconsPath=os.path.join(resourcesPath, 'icons')

provider = channelproviders.GitHubJSON(includeDisabled)
# provider = channelproviders.TvOnlineAPP()
# provider = channelproviders.GitHubMD()

channelList = provider.retrieveList()

for channel in channelList:

	channelListItem = xbmcgui.ListItem(channel[0])
	if iconsWanted:
		iconfile = icons.getIcon(channel[0])
		if iconfile != None:
			channelListItem.setArt({ 'icon': os.path.join(iconsPath, iconfile), 'poster': os.path.join(iconsPath, iconfile), 'banner' : os.path.join(iconsPath, iconfile) })
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=channel[1], listitem=channelListItem)

xbmcplugin.endOfDirectory(addon_handle)
