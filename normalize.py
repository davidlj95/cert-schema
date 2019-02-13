import hashlib
import json
from cert_schema import normalize_jsonld
from cert_schema.jsonld_helpers import preloaded_context_document_loader

with open("sample.json", "r") as f:
    doc = json.load(f)

#del doc['signature']
normalized_doc = normalize_jsonld(doc)
print(normalized_doc)
hash_hex = hashlib.sha256(normalized_doc.encode('utf-8')).hexdigest()
