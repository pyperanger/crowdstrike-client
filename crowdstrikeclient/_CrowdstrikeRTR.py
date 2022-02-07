import json

def RealTimeResponseBatchInitSession(self, ids, timeout=30, timeout_duration="30s", batch=None):
    '''/real-time-response/combined/batch-init-session/v1'''
    body = {
        "host_ids": ids if type(ids) == list else [ids],
        "queue_offline": True
    }
    if batch:
          body["existing_batch_id"] = batch

    return json.loads(self.PostAPI("real-time-response/combined/batch-init-session/v1?timeout={}&timeout_duration={}".format(str(timeout), timeout_duration), body))

def RealTimeResponseCombinedBatchRefreshSession(self, batch, ids=[], timeout=30, timeout_duration="30s"):
    '''/real-time-response/combined/batch-refresh-session/v1'''
    body = {
        "batch_id": batch, 
        "host_ids": ids if type(ids) == list else [ids]
    }
    
    return json.loads(self.PostAPI("real-time-response/combined/batch-refresh-session/v1?timeout={}&timeout_duration={}".format(str(timeout), timeout_duration), body))


def RealTimeResponseCombinedBatchAdminCommand(self, base_command, batch, command_string, ids=[], timeout=30, timeout_duration="30s"):
    '''/real-time-response/combined/batch-refresh-session/v1'''
    body = {
        "base_command" : base_command,
        "batch_id": batch, 
        "command_string": command_string,
        "optional_hosts": ids if type(ids) == list else [ids],
        "persist_all": True
    }
    
    return json.loads(self.PostAPI("real-time-response/combined/batch-admin-command/v1?timeout={}&timeout_duration={}".format(str(timeout), timeout_duration), body))

def RealTimeResponseQueriesSessions(self):
    '''/real-time-response/queries/sessions/v1'''
    return json.loads(self.GetAPI("real-time-response/queries/sessions/v1"))

def RealTimeResponseQueriesScripts(self):
    '''/real-time-response/queries/scripts/v1'''
    return json.loads(self.GetAPI("real-time-response/queries/scripts/v1"))
    

def RealTimeResponseEntitiesScripts(self, ids):
    '''/real-time-response/entities/scripts/v1'''
    if type(ids) == str:
        payload = ids
    elif type(ids) == list:
        payload = ids[0]
        for id in ids[1:]:
            payload += "&ids=" + id
    else:
        return None
    print (payload)
    return json.loads(self.GetAPI("real-time-response/entities/scripts/v1?ids=" + payload))
