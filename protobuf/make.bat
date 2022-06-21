del *_pb2.py *_pb2.pyc
protoc --python_out=. activity.proto
protoc --python_out=. profile.proto
protoc --python_out=. per-session-info.proto
protoc --python_out=. udp-node-msgs.proto

pause