import json
import sys
sys.path.append('c:/flowkit')
from agent.services import flow_batch as fb

with open('scratch/jwpduf_response.txt', 'r', encoding='utf-8') as f:
    text = f.read()

payload = fb.first_payload(text, fb.RPC_OPERATION)
print("Payload from jwpduf:")
print(json.dumps(payload, indent=2)[:500])

op = fb.read_operation(payload)
print("\nParsed operation:")
print("op_id:", op.operation_id)
print("status:", op.status)
print("done:", op.done)
print("complaint:", op.complained, op.error)
