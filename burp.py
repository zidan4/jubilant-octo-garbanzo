from burp import IBurpExtender
from burp import IContextMenuFactory
from javax.swing import JMenuItem
from java.util import List, ArrayList
from java.net import URL

import socket
import urllib
import json
import re
import base64

bing_api_key = "YOURKEY"
class BurpExtender(IBurpExtender, IContextMenuFactory):
  def registerExtenderCallbacks(self, callbacks):
  self._callbacks = callbacks
  self._helpers = callbacks.getHelpers()
  self.context = None
  
  # we set up our extension
  callbacks.setExtensionName("BHP Bing")
  callbacks.registerContextMenuFactory(self)
  return
  
  def createMenuItems(self, context_menu):
  self.context = context_menu
  menu_list = ArrayList()
  menu_list.add(JMenuItem("Send to Bing", actionPerformed=self.bing_¬
  menu))

  return menu_list
