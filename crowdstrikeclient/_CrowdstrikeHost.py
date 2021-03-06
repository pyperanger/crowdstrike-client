import json

def DevicesQueriesDevices(self, query):
    '''/devices/queries/devices/v1'''
    return json.loads(self.GetAPI("devices/queries/devices/v1?"+query))

def DevicesEntitiesDevices(self, ids):
    '''/devices/entities/devices/v1'''
    Param = ""
    for ids in ids:
        Param += "ids="+ids+"&"    
    return json.loads(self.GetAPI("devices/entities/devices/v1?"+Param))

def DevicesCombinedDevicesLoginhistory(self, DeviceList):
    '''/devices/combined/devices/login-history/v1'''
    return json.loads(self.PostAPI("devices/combined/devices/login-history/v1", ({"ids": DeviceList}) ))

def DevicesCombinedDevicesNetworkAddressHistory(self, DeviceList):
    '''/devices/combined/devices/network-address-history/v1'''
    return json.loads(self.PostAPI("devices/combined/devices/network-address-history/v1", ({"ids": DeviceList}) ))

def DevicesEntitiesDevicesActions(self, action, hosts_ids):
    '''/devices/entities/devices-actions/v2'''
    if type(hosts_ids) == str:
        hosts_ids = [hosts_ids]
    
    payload = {
        "action_parameters":[{
            "name": "string",
            "value": "string"
        }],
        "ids": hosts_ids
    }
    
    return json.loads(self.PostAPI("devices/entities/devices-actions/v2?action_name=" + action, payload))
