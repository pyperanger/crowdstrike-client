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
